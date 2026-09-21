# Material do Prof. Bruno Gomes - IFRN Campus Canguaretama

# SQL × Django ORM — operadores de comparação, lógicos e de caracteres

Continuação de `01_sql_basico_operacoes.md`. Lá o `WHERE` só apareceu com o
igual (`=`); aqui ele ganha todos os operadores. Como no primeiro documento,
cada bloco traz **o SQL**, o **equivalente no ORM** e uma explicação curta, do
mais simples para o mais complexo — com as alternativas quando existe mais de um
jeito de escrever a mesma coisa.

Os models são os mesmos (`Area`, `PublicoAlvo`, `Curso`) e as tabelas continuam
sendo `cursos_curso`, `cursos_area`, `cursos_publicoalvo` e
`cursos_curso_publicos`.

## A ideia central: *lookups*

No ORM, o operador vira um **sufixo** colado no nome do campo com dois
underscores:

```
filter(  campo  __  lookup  =  valor  )
              │        │
              │        └── o operador: gt, lt, in, contains, ...
              └── o campo (pode atravessar relação: area__nome)
```

Quando você não escreve sufixo nenhum, o Django assume `exact` (o `=` do SQL).
Então `filter(ch=40)` e `filter(ch__exact=40)` são a mesmíssima coisa.

E vale lembrar sempre: `print(qs.query)` mostra o SQL que o queryset vai executar.

---

# Parte 1 — Operadores de comparação

## 1.1 Igual — `=`

```sql
SELECT * FROM cursos_curso WHERE ch = 40;
```

```python
Curso.objects.filter(ch=40)
Curso.objects.filter(ch__exact=40)   # forma explícita, idêntica
```

## 1.2 Diferente — `<>` / `!=`

O ORM **não tem** um lookup `ne`. Existem duas formas:

```sql
SELECT * FROM cursos_curso WHERE ch <> 40;
```

**Opção simples — `exclude()`:**

```python
Curso.objects.exclude(ch=40)
```

**Opção com `Q` e negação** (útil quando a condição está no meio de outras):

```python
from django.db.models import Q
Curso.objects.filter(~Q(ch=40))
```

> ⚠️ **Cuidado com `NULL`.** Linhas em que o campo é `NULL` não entram nem no
> `filter` nem no `exclude`, porque em SQL `NULL <> 40` não é verdadeiro nem
> falso — é desconhecido. Se você quer "diferente de 40 **ou** vazio", precisa
> pedir isso explicitamente:
>
> ```python
> Curso.objects.filter(Q(data__isnull=True) | ~Q(data='2026-03-01'))
> ```

## 1.3 Maior, maior ou igual, menor, menor ou igual

```sql
SELECT * FROM cursos_curso WHERE ch >  40;
SELECT * FROM cursos_curso WHERE ch >= 40;
SELECT * FROM cursos_curso WHERE ch <  40;
SELECT * FROM cursos_curso WHERE ch <= 40;
```

```python
Curso.objects.filter(ch__gt=40)     # greater than
Curso.objects.filter(ch__gte=40)    # greater than or equal
Curso.objects.filter(ch__lt=40)     # less than
Curso.objects.filter(ch__lte=40)    # less than or equal
```

Funciona igual para números, datas e texto (em texto a comparação é alfabética):

```python
Curso.objects.filter(data__gte='2026-01-01')
Curso.objects.filter(titulo__gt='M')     # títulos depois de "M" no alfabeto
```

## 1.4 Faixa de valores — `BETWEEN`

```sql
SELECT * FROM cursos_curso WHERE ch BETWEEN 20 AND 60;
```

**Opção simples — `range` (inclui as duas pontas, igual ao `BETWEEN`):**

```python
Curso.objects.filter(ch__range=(20, 60))
```

**Opção equivalente, com dois lookups:**

```python
Curso.objects.filter(ch__gte=20, ch__lte=60)
```

Com datas é o caso mais comum — cursos que começam no primeiro semestre:

```python
from datetime import date
Curso.objects.filter(data__range=(date(2026, 1, 1), date(2026, 6, 30)))
```

**Partes de data**, que no SQL exigiriam funções (`EXTRACT`, `strftime`...):

```python
Curso.objects.filter(data__year=2026)             # WHERE EXTRACT(YEAR FROM data) = 2026
Curso.objects.filter(data__month=3)
Curso.objects.filter(data__year=2026, data__month__gte=7)   # 2º semestre
```

## 1.5 Lista de valores — `IN`

```sql
SELECT * FROM cursos_curso WHERE ch IN (20, 40, 60);
```

```python
Curso.objects.filter(ch__in=[20, 40, 60])
```

O contrário (`NOT IN`):

```sql
SELECT * FROM cursos_curso WHERE ch NOT IN (20, 40, 60);
```

```python
Curso.objects.exclude(ch__in=[20, 40, 60])
```

Isso é exatamente o que uma tela de filtro com caixas de seleção múltipla precisa:

```python
ids = request.GET.getlist('areas')          # ['1', '3', '7']
if ids:
    cursos = cursos.filter(area_id__in=ids)
```

**Versão mais complexa — `IN` com subconsulta.** Em vez de uma lista pronta, o
`in` aceita **outro queryset**, e o Django gera uma subconsulta de verdade:

```sql
SELECT * FROM cursos_curso
 WHERE area_id IN (SELECT id FROM cursos_area WHERE nome LIKE 'Inf%');
```

```python
areas = Area.objects.filter(nome__startswith='Inf')
Curso.objects.filter(area__in=areas)
# ou, deixando claro que é só o id:
Curso.objects.filter(area_id__in=areas.values('id'))
```

## 1.6 Vazio ou não — `IS NULL` / `IS NOT NULL`

```sql
SELECT * FROM cursos_curso WHERE data IS NULL;
SELECT * FROM cursos_curso WHERE data IS NOT NULL;
```

```python
Curso.objects.filter(data__isnull=True)
Curso.objects.filter(data__isnull=False)
```

`isnull` é o único jeito certo de perguntar por vazio. **Não** escreva
`filter(data=None)` esperando outra coisa (o Django até traduz isso para
`IS NULL`, mas a intenção fica muito menos clara) e muito menos `filter(data='')`,
que compara com string vazia — coisa diferente de `NULL`.

Em texto, "vazio" pode ser as duas coisas ao mesmo tempo:

```python
from django.db.models import Q
Curso.objects.filter(Q(descricao__isnull=True) | Q(descricao=''))
```

## 1.7 Comparar dois campos da mesma linha — `F()`

Até aqui comparamos campo com **valor**. Para comparar campo com **campo**, o
valor precisa ser um `F()`, senão o Django trataria `'vagas'` como texto:

```sql
SELECT * FROM cursos_curso WHERE vagas > ch;
```

```python
from django.db.models import F
Curso.objects.filter(vagas__gt=F('ch'))
```

O `F()` também aceita conta:

```sql
SELECT * FROM cursos_curso WHERE vagas >= ch * 2;
```

```python
Curso.objects.filter(vagas__gte=F('ch') * 2)
```

## Resumo — comparação

| SQL | Lookup | Exemplo |
|---|---|---|
| `=` | `exact` (padrão) | `filter(ch=40)` |
| `<>` / `!=` | — | `exclude(ch=40)` / `filter(~Q(ch=40))` |
| `>` | `gt` | `filter(ch__gt=40)` |
| `>=` | `gte` | `filter(ch__gte=40)` |
| `<` | `lt` | `filter(ch__lt=40)` |
| `<=` | `lte` | `filter(ch__lte=40)` |
| `BETWEEN a AND b` | `range` | `filter(ch__range=(20, 60))` |
| `IN (...)` | `in` | `filter(ch__in=[20, 40])` |
| `NOT IN (...)` | — | `exclude(ch__in=[20, 40])` |
| `IS NULL` | `isnull` | `filter(data__isnull=True)` |
| campo × campo | `F()` | `filter(vagas__gt=F('ch'))` |

---

# Parte 2 — Operadores lógicos

## 2.1 `AND`

```sql
SELECT * FROM cursos_curso WHERE ch >= 40 AND vagas > 0;
```

**Opção simples — argumentos no mesmo `filter()`:**

```python
Curso.objects.filter(ch__gte=40, vagas__gt=0)
```

**Opção encadeada:**

```python
Curso.objects.filter(ch__gte=40).filter(vagas__gt=0)
```

**Opção com `Q`:**

```python
from django.db.models import Q
Curso.objects.filter(Q(ch__gte=40) & Q(vagas__gt=0))
```

As três dão o mesmo resultado aqui. Regra prática: use a primeira no dia a dia, a
segunda quando os filtros são opcionais (`if` na view) e a terceira quando o `AND`
precisa conviver com um `OR`.

> **Exceção importante:** em campos **muitos-para-muitos**, `filter(a, b)` e
> `filter(a).filter(b)` **não** são a mesma coisa.
>
> ```python
> # um MESMO vínculo que atenda às duas condições:
> Curso.objects.filter(publicos__nome='Discente', publicos__id=2)
> # dois vínculos diferentes, um para cada condição:
> Curso.objects.filter(publicos__nome='Discente').filter(publicos__id=2)
> ```
>
> A primeira faz **um** `JOIN`; a segunda faz **dois**. Para "curso que atende ao
> público A **e** ao público B" é a segunda que você quer.

## 2.2 `OR` — os objetos `Q`

Com argumentos normais só dá para fazer `AND`. Para `OR` é obrigatório usar `Q`:

```sql
SELECT * FROM cursos_curso WHERE ch >= 40 OR vagas > 100;
```

```python
from django.db.models import Q
Curso.objects.filter(Q(ch__gte=40) | Q(vagas__gt=100))
```

Um `Q` é só "um pedaço de `WHERE`" guardado numa variável. Os operadores são:

| SQL | Python |
|---|---|
| `AND` | `&` |
| `OR` | `\|` |
| `NOT` | `~` |

**Alternativa sem `Q`:** juntar dois querysets com `|` (união). Funciona, mas
gera um SQL diferente (e costuma ser menos eficiente):

```python
Curso.objects.filter(ch__gte=40) | Curso.objects.filter(vagas__gt=100)
```

## 2.3 `NOT`

```sql
SELECT * FROM cursos_curso WHERE NOT (ch >= 40);
```

```python
Curso.objects.exclude(ch__gte=40)        # forma usual
Curso.objects.filter(~Q(ch__gte=40))     # forma com Q
```

A diferença aparece quando a negação é **parte** de uma expressão maior — aí só o
`~Q` resolve:

```sql
WHERE vagas > 0 AND NOT (ch = 40)
```

```python
Curso.objects.filter(Q(vagas__gt=0) & ~Q(ch=40))
```

## 2.4 Parênteses — misturando `AND` e `OR`

Esta é a parte em que mais se erra. No SQL, `AND` tem precedência sobre `OR`;
no ORM, quem manda são os parênteses que você escreve.

```sql
SELECT * FROM cursos_curso
 WHERE (ch = 20 OR ch = 40)
   AND vagas > 0;
```

```python
Curso.objects.filter(Q(ch=20) | Q(ch=40), vagas__gt=0)
```

Ou, tudo em `Q`, deixando os parênteses explícitos:

```python
Curso.objects.filter((Q(ch=20) | Q(ch=40)) & Q(vagas__gt=0))
```

Repare na primeira versão: **os `Q` vêm antes** dos argumentos nomeados. Isso é
regra do Python — argumento posicional não pode vir depois de nomeado — e o
Django junta tudo com `AND`.

> ⚠️ Em Python, `&` e `|` têm precedência **maior** que `=` e que os comparadores.
> Por isso os `Q` precisam de parênteses individuais:
> `Q(a=1) | Q(b=2)` ✅ — e nunca algo como `Q(a=1 | b=2)` ❌.

## 2.5 Montando o `WHERE` dinamicamente

O grande motivo para aprender `Q` é este: dá para **construir** a condição aos
poucos, como texto de busca que procura em vários campos ao mesmo tempo.

```python
from django.db.models import Q

def cursos(request):
    busca = request.GET.get('busca', '').strip()
    area = request.GET.get('area')

    qs = Curso.objects.select_related('area')

    if busca:
        qs = qs.filter(
            Q(titulo__icontains=busca) |
            Q(descricao__icontains=busca) |
            Q(area__nome__icontains=busca)
        )
    if area:
        qs = qs.filter(area_id=area)

    return render(request, 'cursos.html', {'cursos': qs.order_by('titulo')})
```

E, quando a lista de condições é variável, dá para acumular num laço:

```python
condicoes = Q()                       # vazio = "não filtra nada"
for palavra in busca.split():
    condicoes &= Q(titulo__icontains=palavra)   # todas as palavras precisam bater
Curso.objects.filter(condicoes)
```

## Resumo — lógicos

| SQL | Django ORM |
|---|---|
| `A AND B` | `filter(A, B)` / `filter(A).filter(B)` / `filter(Q(A) & Q(B))` |
| `A OR B` | `filter(Q(A) \| Q(B))` |
| `NOT A` | `exclude(A)` / `filter(~Q(A))` |
| `(A OR B) AND C` | `filter((Q(A) \| Q(B)) & Q(C))` |
| `A AND NOT B` | `filter(A).exclude(B)` / `filter(Q(A) & ~Q(B))` |

---

# Parte 3 — Operadores de caracteres

Todos aqui se apoiam no `LIKE` do SQL, em que `%` significa "qualquer coisa" e
`_` significa "um caractere qualquer".

## 3.1 Começa com — `LIKE 'texto%'`

```sql
SELECT * FROM cursos_curso WHERE titulo LIKE 'Python%';
```

```python
Curso.objects.filter(titulo__startswith='Python')
```

## 3.2 Termina com — `LIKE '%texto'`

```sql
SELECT * FROM cursos_curso WHERE titulo LIKE '%avançado';
```

```python
Curso.objects.filter(titulo__endswith='avançado')
```

## 3.3 Contém — `LIKE '%texto%'`

```sql
SELECT * FROM cursos_curso WHERE titulo LIKE '%dados%';
```

```python
Curso.objects.filter(titulo__contains='dados')
```

## 3.4 Ignorando maiúsculas/minúsculas — o `i` na frente

Todo lookup de texto tem uma versão que **ignora a caixa**: é só colocar um `i`
na frente. No SQL isso vira `ILIKE` (PostgreSQL) ou `UPPER(campo) LIKE UPPER(...)`.

```sql
SELECT * FROM cursos_curso WHERE titulo ILIKE '%dados%';
-- em bancos sem ILIKE:
SELECT * FROM cursos_curso WHERE UPPER(titulo) LIKE UPPER('%dados%');
```

```python
Curso.objects.filter(titulo__icontains='dados')
Curso.objects.filter(titulo__istartswith='python')
Curso.objects.filter(titulo__iendswith='AVANÇADO')
Curso.objects.filter(titulo__iexact='python básico')   # = , mas sem ligar para a caixa
```

**`icontains` é o lookup mais usado em campo de busca de tela**, porque o usuário
nunca digita exatamente como está no banco.

> Observação sobre o SQLite: por padrão ele já ignora a caixa em `LIKE` com
> caracteres ASCII, então `contains` e `icontains` parecem iguais durante o
> desenvolvimento e passam a se comportar diferente quando o projeto vai para o
> PostgreSQL. Escreva o que você realmente quer, não o que "funcionou no teste".

## 3.5 Não contém — `NOT LIKE`

```sql
SELECT * FROM cursos_curso WHERE titulo NOT LIKE '%teste%';
```

```python
Curso.objects.exclude(titulo__icontains='teste')
```

## 3.6 `%` e `_` dentro do texto procurado

Esta é a vantagem silenciosa do ORM: ele **escapa** os caracteres especiais para
você. Procurar literalmente por "100%":

```sql
SELECT * FROM cursos_curso WHERE titulo LIKE '%100\%%' ESCAPE '\';
```

```python
Curso.objects.filter(titulo__contains='100%')   # o Django escapa sozinho
```

Se a busca vier do usuário (e vem), é mais um motivo para nunca montar SQL na
mão com concatenação de string — isso é a porta de entrada do SQL injection.

## 3.7 Um caractere qualquer e padrões mais livres — `_` e expressão regular

O ORM não tem lookup para o `_` do `LIKE`. Quando o padrão é mais complicado,
use expressão regular:

```sql
-- títulos que começam com "Curso" seguido de um dígito
SELECT * FROM cursos_curso WHERE titulo REGEXP '^Curso [0-9]';
```

```python
Curso.objects.filter(titulo__regex=r'^Curso [0-9]')
Curso.objects.filter(titulo__iregex=r'^curso [0-9]')   # ignorando a caixa
```

Use com moderação: `regex` costuma impedir o uso de índices e deixa a consulta
lenta em tabelas grandes.

## 3.8 Funções de texto — `UPPER`, `LOWER`, `LENGTH`, `||`

Quando o texto precisa ser **transformado** antes de comparar (ou exibir), entram
as funções do `django.db.models.functions`:

```sql
SELECT * FROM cursos_curso WHERE LENGTH(titulo) > 50;
```

```python
from django.db.models.functions import Length

Curso.objects.annotate(tam=Length('titulo')).filter(tam__gt=50)
```

O `annotate()` calcula a função no `SELECT` e dá um nome a ela (`tam`); daí para
frente esse nome é usado como se fosse um campo qualquer. Se você usa isso o tempo
todo, dá para registrar a função como lookup uma única vez (em `apps.py`, no
`ready()`) e passar a escrever `titulo__length__gt=50`:

```python
from django.db.models import CharField
from django.db.models.functions import Length
CharField.register_lookup(Length)
```

Concatenar título e nome da área numa coluna nova (`||` no SQL padrão,
`CONCAT` no MySQL):

```sql
SELECT c.titulo || ' - ' || a.nome AS rotulo
  FROM cursos_curso c JOIN cursos_area a ON a.id = c.area_id;
```

```python
from django.db.models import Value
from django.db.models.functions import Concat

Curso.objects.annotate(
    rotulo=Concat('titulo', Value(' - '), 'area__nome')
).values('rotulo')
```

O `annotate()` cria uma coluna calculada no `SELECT`, e o `Value()` é como se
escreve "texto literal" dentro de uma expressão do ORM (sem ele, o Django acharia
que `' - '` é nome de campo). Essa coluna nova pode ser usada normalmente em
`filter()` e `order_by()`:

```python
Curso.objects.annotate(
    rotulo=Concat('titulo', Value(' - '), 'area__nome')
).filter(rotulo__icontains='informática').order_by('rotulo')
```

## Resumo — caracteres

| SQL | Lookup | Exemplo |
|---|---|---|
| `LIKE 'x%'` | `startswith` | `filter(titulo__startswith='Python')` |
| `ILIKE 'x%'` | `istartswith` | `filter(titulo__istartswith='python')` |
| `LIKE '%x'` | `endswith` | `filter(titulo__endswith='2026')` |
| `ILIKE '%x'` | `iendswith` | `filter(titulo__iendswith='2026')` |
| `LIKE '%x%'` | `contains` | `filter(titulo__contains='dados')` |
| `ILIKE '%x%'` | `icontains` | `filter(titulo__icontains='dados')` |
| `NOT LIKE '%x%'` | — | `exclude(titulo__icontains='teste')` |
| `=` sem ligar para a caixa | `iexact` | `filter(titulo__iexact='python básico')` |
| `REGEXP` | `regex` / `iregex` | `filter(titulo__regex=r'^Curso [0-9]')` |
| `LENGTH(campo)` | `Length` | `annotate(tam=Length('titulo')).filter(tam__gt=50)` |
| `campo1 \|\| campo2` | `Concat` | `annotate(x=Concat('titulo', Value(' - '), 'area__nome'))` |

---

# Fechando: uma consulta com os três tipos de operador

"Cursos de informática ou de gestão, com carga horária entre 20 e 60 horas, que
ainda tenham vaga, cujo título fale em 'dados', tirando os que são teste, do mais
novo para o mais antigo."

```sql
SELECT DISTINCT c.*
  FROM cursos_curso c
  JOIN cursos_area a ON a.id = c.area_id
 WHERE (a.nome ILIKE 'Inform%' OR a.nome ILIKE 'Gest%')
   AND c.ch BETWEEN 20 AND 60
   AND c.vagas > 0
   AND c.titulo ILIKE '%dados%'
   AND c.titulo NOT ILIKE '%teste%'
   AND c.data IS NOT NULL
 ORDER BY c.data DESC, c.titulo;
```

```python
from django.db.models import Q

cursos = (Curso.objects
          .select_related('area')
          .filter(
              Q(area__nome__istartswith='Inform') | Q(area__nome__istartswith='Gest'),
              ch__range=(20, 60),
              vagas__gt=0,
              titulo__icontains='dados',
              data__isnull=False,
          )
          .exclude(titulo__icontains='teste')
          .order_by('-data', 'titulo')
          .distinct())
```

Leia de cima para baixo e compare com o SQL: o `OR` virou `Q(...) | Q(...)` e veio
**antes** dos demais argumentos; o `BETWEEN` virou `range`; os `>`, `IS NOT NULL`
e `ILIKE` viraram `gt`, `isnull` e `icontains`; o `NOT ILIKE` virou `exclude()`.
E, como sempre, confira o resultado com:

```python
print(cursos.query)
```
