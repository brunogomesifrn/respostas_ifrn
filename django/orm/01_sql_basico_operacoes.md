# SQL básico × Django ORM — `FROM`, `WHERE` e `ORDER BY`

Documento de apoio da aula. Cada bloco mostra **o SQL** e, logo abaixo, **o
equivalente no ORM do Django**, com uma explicação curta. A ordem vai do comando
mais simples até o mais completo. Quando existe mais de um jeito de escrever a
mesma consulta, as duas versões aparecem (a simples e a mais elaborada).

## Os models usados nos exemplos

```python
class Area(models.Model):
    nome = models.CharField("Nome", max_length=50)

class PublicoAlvo(models.Model):
    nome = models.CharField("Nome", max_length=50)

class Curso(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    ch = models.IntegerField("Carga-horária")
    data = models.DateField("Data de início", null=True, blank=True)
    vagas = models.IntegerField("Vagas")
    imagem = models.ImageField("Imagem", upload_to='cursos/', null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(PublicoAlvo)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True)
```

Nos exemplos em SQL as tabelas são chamadas de `cursos_curso`, `cursos_area`,
`cursos_publicoalvo` e `cursos_curso_publicos` — é o nome que o Django dá por
padrão: `<app>_<model em minúsculo>`. Se o app tiver outro nome, troque o prefixo.

> **Dica de ouro para a aula:** todo queryset sabe mostrar o SQL que ele vai
> executar. Use isso o tempo todo para conferir se a tradução está certa:
>
> ```python
> qs = Curso.objects.filter(ch__gte=40)
> print(qs.query)
> ```

---

## 1. Trazer tudo — `SELECT *` + `FROM`

```sql
SELECT * FROM cursos_curso;
```

```python
Curso.objects.all()
```

`Curso.objects` é o *manager* (a porta de entrada do model para o banco) e `all()`
devolve um **QuerySet** com todas as linhas da tabela. O `FROM` some porque o
Django já sabe de qual tabela se trata: é a do model que você usou.

Uma coisa importante: o SQL **ainda não foi executado** nessa linha. O QuerySet é
*preguiçoso* (lazy) — ele só vai ao banco quando você percorre, conta, fatia ou
imprime o resultado:

```python
qs = Curso.objects.all()      # nada aconteceu no banco ainda
for curso in qs:              # AGORA o SELECT é enviado
    print(curso.titulo)
```

---

## 2. Escolher as colunas — `SELECT campo1, campo2`

```sql
SELECT titulo, ch FROM cursos_curso;
```

**Opção simples — dicionários:**

```python
Curso.objects.values('titulo', 'ch')
# <QuerySet [{'titulo': 'Python básico', 'ch': 40}, ...]>
```

**Opção com tuplas:**

```python
Curso.objects.values_list('titulo', 'ch')
# <QuerySet [('Python básico', 40), ...]>
```

**Uma coluna só, como lista simples:**

```python
Curso.objects.values_list('titulo', flat=True)
# <QuerySet ['Python básico', 'Django na prática', ...]>
```

**Opção que continua devolvendo objetos `Curso`:**

```python
Curso.objects.only('titulo', 'ch')    # busca só essas colunas (+ id)
Curso.objects.defer('descricao')      # busca todas, MENOS essa
```

Qual usar? `values()`/`values_list()` quando você só quer os dados (relatório,
JSON, um `<select>`). `only()`/`defer()` quando você ainda precisa dos métodos do
objeto, mas quer evitar carregar um `TextField` gigante como a `descricao`.

---

## 3. Limitar a quantidade — `LIMIT` e `OFFSET`

```sql
SELECT * FROM cursos_curso LIMIT 5;
SELECT * FROM cursos_curso LIMIT 5 OFFSET 10;
```

```python
Curso.objects.all()[:5]       # LIMIT 5
Curso.objects.all()[10:15]    # LIMIT 5 OFFSET 10
```

O fatiamento do Python vira `LIMIT`/`OFFSET` **no banco** — ele não traz tudo para
a memória e corta depois. É exatamente isso que o `Paginator` do Django faz por
baixo dos panos.

Cuidado: depois de fatiar, o QuerySet não aceita mais `filter()` nem `order_by()`.
Filtre e ordene primeiro, fatie por último.

---

## 4. Uma condição — `WHERE campo = valor`

```sql
SELECT * FROM cursos_curso WHERE ch = 40;
```

```python
Curso.objects.filter(ch=40)
```

O `filter()` é o `WHERE`. O nome do argumento é o campo; o valor é a comparação.
Escrever `ch=40` é o mesmo que escrever `ch__exact=40` — o `exact` é o padrão
quando você não diz nada.

---

## 5. Trazer **um** registro só

```sql
SELECT * FROM cursos_curso WHERE id = 3;
```

**Se você tem certeza de que existe exatamente um:**

```python
Curso.objects.get(id=3)
# ou, como é a chave primária:
Curso.objects.get(pk=3)
```

**Se pode não existir (e você não quer tratar exceção):**

```python
Curso.objects.filter(id=3).first()   # devolve None se não achar
```

**Na view, quando "não existe" deve virar erro 404:**

```python
from django.shortcuts import get_object_or_404
curso = get_object_or_404(Curso, pk=3)
```

A diferença: `get()` devolve **o objeto** e estoura `DoesNotExist` se não achar (ou
`MultipleObjectsReturned` se achar mais de um); `filter()` devolve **um QuerySet**,
que pode vir vazio sem nenhum problema.

---

## 6. Duas ou mais condições — `WHERE ... AND ...`

```sql
SELECT * FROM cursos_curso WHERE ch = 40 AND vagas = 30;
```

**Opção simples — os dois filtros no mesmo `filter()`:**

```python
Curso.objects.filter(ch=40, vagas=30)
```

**Opção encadeada — um `filter()` depois do outro:**

```python
Curso.objects.filter(ch=40).filter(vagas=30)
```

As duas geram o mesmo SQL aqui. A versão encadeada é útil quando as condições são
**opcionais**, que é o caso clássico de uma tela com filtros:

```python
cursos = Curso.objects.all()

if titulo:
    cursos = cursos.filter(titulo__icontains=titulo)
if area:
    cursos = cursos.filter(area_id=area)
```

Cada `filter()` devolve um **novo** QuerySet; o original não é alterado. E, como o
QuerySet é preguiçoso, o banco só é consultado uma vez, no fim, com todos os
`AND` já montados.

---

## 7. Negar uma condição — `WHERE NOT` / `<>`

```sql
SELECT * FROM cursos_curso WHERE ch <> 40;
```

```python
Curso.objects.exclude(ch=40)
```

`exclude()` é o oposto do `filter()`. Um detalhe que costuma pegar: se o campo
aceita `NULL`, as linhas com `NULL` **não** aparecem nem no `filter` nem no
`exclude` — em SQL, `NULL <> 40` não é verdadeiro, é desconhecido.

---

## 8. Ordenar — `ORDER BY`

```sql
SELECT * FROM cursos_curso ORDER BY titulo;           -- crescente
SELECT * FROM cursos_curso ORDER BY titulo DESC;      -- decrescente
SELECT * FROM cursos_curso ORDER BY ch DESC, titulo;  -- por dois campos
```

```python
Curso.objects.order_by('titulo')
Curso.objects.order_by('-titulo')          # o "-" é o DESC
Curso.objects.order_by('-ch', 'titulo')    # desempata pelo título
```

**Ordenação padrão do model** (vale para todas as consultas, sem repetir
`order_by`):

```python
class Curso(models.Model):
    ...
    class Meta:
        ordering = ['titulo']
```

Com o `Meta.ordering` definido, `Curso.objects.all()` já sai ordenado. Para
inverter essa ordem padrão use `Curso.objects.reverse()`, e para **desligar**
qualquer ordenação use `Curso.objects.order_by()` (sem argumentos) — isso importa
porque ordenar tem custo.

**Ignorando maiúsculas/minúsculas:**

```python
from django.db.models.functions import Lower
Curso.objects.order_by(Lower('titulo'))    # ORDER BY LOWER(titulo)
```

**Onde colocar os nulos** (a `data` pode ser `NULL`):

```python
from django.db.models import F
Curso.objects.order_by(F('data').asc(nulls_last=True))
Curso.objects.order_by(F('data').desc(nulls_first=True))
```

**Ordem aleatória:**

```python
Curso.objects.order_by('?')      # ORDER BY RANDOM() — pesado em tabela grande
```

---

## 9. Sem repetições — `DISTINCT`

```sql
SELECT DISTINCT ch FROM cursos_curso;
```

```python
Curso.objects.values_list('ch', flat=True).distinct()
```

O `DISTINCT` olha **todas as colunas** que estão no `SELECT`. Por isso
`Curso.objects.distinct()` quase nunca muda alguma coisa: o `id` já torna cada
linha única. O `distinct()` fica realmente útil depois de um `values()` ou depois
de um `JOIN` que duplica linhas (veja o item 12).

---

## 10. Contar — `COUNT(*)`

```sql
SELECT COUNT(*) FROM cursos_curso WHERE ch >= 40;
```

```python
Curso.objects.filter(ch__gte=40).count()
```

Para apenas **saber se existe**, não use `count()` nem `len()`:

```python
Curso.objects.filter(ch__gte=40).exists()   # SELECT 1 ... LIMIT 1
```

`exists()` manda o banco parar no primeiro registro encontrado; é bem mais barato.

---

## 11. `FROM` com junção — chave estrangeira (`INNER JOIN`)

Filtrar cursos pelo **nome da área** (que está em outra tabela):

```sql
SELECT c.*
  FROM cursos_curso c
 INNER JOIN cursos_area a ON a.id = c.area_id
 WHERE a.nome = 'Informática';
```

```python
Curso.objects.filter(area__nome='Informática')
```

O `__` (dois underscores) é o "ponto" do ORM: atravessa o relacionamento e o
Django escreve o `JOIN` sozinho. Dá para atravessar quantos níveis existirem:
`curso__area__nome`, e assim por diante.

**Se o filtro é pelo id, nem precisa de JOIN:**

```python
Curso.objects.filter(area_id=1)      # a FK já guarda o id na própria tabela
Curso.objects.filter(area=area_obj)  # mesma coisa, passando o objeto
```

**Trazendo os dados da área junto (para não fazer N consultas):**

```python
Curso.objects.select_related('area')
```

Sem o `select_related`, um laço que faz `curso.area.nome` dispara **uma consulta
por curso** (o famoso problema do N+1). Com ele, o Django faz o `JOIN` e traz tudo
de uma vez. Vale para `ForeignKey` e `OneToOne`.

**Ordenando por campo da tabela relacionada:**

```sql
SELECT c.* FROM cursos_curso c
  JOIN cursos_area a ON a.id = c.area_id
 ORDER BY a.nome, c.titulo;
```

```python
Curso.objects.order_by('area__nome', 'titulo')
```

---

## 12. `FROM` com junção — muitos-para-muitos

O `ManyToManyField` cria uma terceira tabela (`cursos_curso_publicos`) com
`curso_id` e `publicoalvo_id`. Para achar os cursos de um público-alvo:

```sql
SELECT DISTINCT c.*
  FROM cursos_curso c
  JOIN cursos_curso_publicos cp ON cp.curso_id = c.id
  JOIN cursos_publicoalvo p     ON p.id = cp.publicoalvo_id
 WHERE p.nome = 'Discente';
```

```python
Curso.objects.filter(publicos__nome='Discente').distinct()
```

O `distinct()` aqui **é necessário**: se o curso estiver ligado a dois públicos que
casam com o filtro, ele apareceria duas vezes.

**Carregando os públicos de cada curso sem cair no N+1:**

```python
Curso.objects.prefetch_related('publicos')
```

Para muitos-para-muitos o Django não usa `JOIN`, e sim uma **segunda consulta** que
traz todos os públicos de uma vez e junta tudo em memória. Por isso o nome é
diferente: `select_related` para FK, `prefetch_related` para M2M e relações
inversas.

**Caminho inverso** (a partir do público, chegar nos cursos):

```python
publico = PublicoAlvo.objects.get(pk=1)
publico.curso_set.all()          # nome padrão da relação inversa
```

---

## 13. Juntando tudo

Uma consulta completa, do jeito que aparece numa view de listagem com filtros:

```sql
SELECT DISTINCT c.*
  FROM cursos_curso c
  JOIN cursos_area a            ON a.id = c.area_id
  JOIN cursos_curso_publicos cp ON cp.curso_id = c.id
  JOIN cursos_publicoalvo p     ON p.id = cp.publicoalvo_id
 WHERE a.nome = 'Informática'
   AND p.nome = 'Discente'
   AND c.vagas > 0
 ORDER BY c.data DESC, c.titulo
 LIMIT 10;
```

```python
cursos = (Curso.objects
          .select_related('area')
          .prefetch_related('publicos')
          .filter(area__nome='Informática',
                  publicos__nome='Discente',
                  vagas__gt=0)
          .order_by('-data', 'titulo')
          .distinct()[:10])
```

Repare na ordem em que as coisas foram escritas — ela imita a leitura do SQL:
de onde vem (`select_related`/`prefetch_related`), o que filtra (`filter`), como
ordena (`order_by`) e quanto traz (fatiamento no fim).

---

## Resumo rápido

| SQL | Django ORM |
|---|---|
| `SELECT * FROM tabela` | `Model.objects.all()` |
| `SELECT a, b FROM tabela` | `.values('a', 'b')` / `.values_list('a', 'b')` / `.only('a', 'b')` |
| `WHERE campo = valor` | `.filter(campo=valor)` |
| `WHERE id = 3` (um registro) | `.get(pk=3)` / `.filter(pk=3).first()` |
| `WHERE a = 1 AND b = 2` | `.filter(a=1, b=2)` ou `.filter(a=1).filter(b=2)` |
| `WHERE campo <> valor` | `.exclude(campo=valor)` |
| `ORDER BY campo` | `.order_by('campo')` |
| `ORDER BY campo DESC` | `.order_by('-campo')` |
| `DISTINCT` | `.distinct()` |
| `COUNT(*)` | `.count()` (ou `.exists()` para só checar) |
| `LIMIT 5 OFFSET 10` | `[10:15]` |
| `JOIN` por FK | `campo_relacionado__campo` + `.select_related()` |
| `JOIN` por M2M | `m2m__campo` + `.prefetch_related()` + `.distinct()` |
| ver o SQL gerado | `print(qs.query)` |
