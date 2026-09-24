# Material do Prof. Bruno Gomes
# Tutorial: do SQL para o Django (tipos de campos e restrições)

Guia rápido para transformar a estrutura de uma tabela SQL em um **model do Django** (e vice-versa).

> **Ideia principal:** no Django, você **não escreve** o `CREATE TABLE`. Você escreve uma **classe** (o model) e o Django gera o SQL por você com as *migrations*.

---

## 1. Tabela x Model: a ideia geral

| No banco (SQL)       | No Django                          |
|----------------------|------------------------------------|
| Tabela               | Classe (model)                     |
| Coluna               | Atributo da classe (campo)         |
| Linha (registro)     | Objeto da classe                   |
| Tipo da coluna       | Tipo do campo (`CharField`, etc.)  |
| Restrição (NOT NULL, UNIQUE...) | Parâmetro do campo (`null`, `unique`...) |

**Exemplo rápido:**

SQL:
```sql
CREATE TABLE aluno (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL
);
```

Django:
```python
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
```

Repare: o `id` **não aparece** no Django. Ele é criado **automaticamente**!

---

## 2. Tipos de campos

### 2.1 Textos

**Texto com limite de caracteres (ex.: 100)**
- No SQL: `VARCHAR(100)`
- No Django: `models.CharField(max_length=100)`

Exemplo: nome com 200 caracteres:
```python
nome = models.CharField(max_length=200)
```

> ⚠️ No `CharField`, o `max_length` é **obrigatório**.

**Texto longo, sem limite (ex.: descrição, observação)**
- No SQL: `TEXT`
- No Django: `models.TextField()`

Exemplo:
```python
descricao = models.TextField()
```

**E-mail**
- No SQL: `VARCHAR(254)`
- No Django: `models.EmailField()`

```python
email = models.EmailField()
```
> O Django ainda **verifica** se o texto parece um e-mail válido (tem `@`, etc.).

**Endereço de site (URL)**
- No SQL: `VARCHAR(200)`
- No Django: `models.URLField()`

```python
site = models.URLField()
```

**Slug (texto para URL, ex.: `meu-primeiro-post`)**
- No SQL: `VARCHAR(50)` + índice
- No Django: `models.SlugField()`

```python
slug = models.SlugField()
```

---

### 2.2 Números

**Número inteiro**
- No SQL: `INTEGER` (ou `INT`)
- No Django: `models.IntegerField()`

```python
idade = models.IntegerField()
```

**Inteiro pequeno** (ex.: quantidade de faltas)
- No SQL: `SMALLINT`
- No Django: `models.SmallIntegerField()`

**Inteiro muito grande**
- No SQL: `BIGINT`
- No Django: `models.BigIntegerField()`

**Inteiro que não pode ser negativo**
- No SQL: `INTEGER` com `CHECK (campo >= 0)` (no MySQL: `INT UNSIGNED`)
- No Django: `models.PositiveIntegerField()`

```python
quantidade_estoque = models.PositiveIntegerField()
```

**Número com casas decimais exatas (ex.: dinheiro)**
- No SQL: `DECIMAL(10, 2)` → até 10 dígitos no total, sendo 2 depois da vírgula
- No Django: `models.DecimalField(max_digits=10, decimal_places=2)`

```python
preco = models.DecimalField(max_digits=10, decimal_places=2)
# Guarda valores até 99999999.99
```

> 💡 **Para dinheiro, use sempre `DecimalField`**, nunca `FloatField`. O `Float` pode gerar erros de arredondamento (ex.: `0.1 + 0.2 = 0.30000000000000004`).

**Número com vírgula "aproximado" (ex.: medidas científicas)**
- No SQL: `FLOAT`, `REAL` ou `DOUBLE PRECISION`
- No Django: `models.FloatField()`

```python
altura = models.FloatField()
```

---

### 2.3 Verdadeiro ou falso

- No SQL: `BOOLEAN` (no MySQL vira `TINYINT(1)`)
- No Django: `models.BooleanField()`

```python
ativo = models.BooleanField(default=True)
```

---

### 2.4 Datas e horas

**Somente data** (ex.: `2026-09-24`)
- No SQL: `DATE`
- No Django: `models.DateField()`

```python
data_nascimento = models.DateField()
```

**Somente hora** (ex.: `14:30:00`)
- No SQL: `TIME`
- No Django: `models.TimeField()`

```python
horario_aula = models.TimeField()
```

**Data e hora juntas**
- No SQL: `DATETIME` (MySQL) ou `TIMESTAMP` (PostgreSQL)
- No Django: `models.DateTimeField()`

```python
criado_em = models.DateTimeField(auto_now_add=True)   # preenche sozinho ao CRIAR
atualizado_em = models.DateTimeField(auto_now=True)   # atualiza sozinho ao SALVAR
```

---

### 2.5 Arquivos e imagens

No banco, **o arquivo não fica salvo na tabela**. Só o **caminho** dele (um texto).

**Arquivo qualquer (PDF, DOC...)**
- No SQL: `VARCHAR(100)` (guarda o caminho)
- No Django: `models.FileField(upload_to='pasta/')`

```python
boletim = models.FileField(upload_to='boletins/')
```

**Imagem**
- No SQL: `VARCHAR(100)` (guarda o caminho)
- No Django: `models.ImageField(upload_to='pasta/')`

```python
foto = models.ImageField(upload_to='fotos/')
```
> ⚠️ Para usar `ImageField`, instale o Pillow: `pip install Pillow`

---

### 2.6 Chave primária (id)

- No SQL: `id BIGINT AUTO_INCREMENT PRIMARY KEY` (MySQL) ou `id BIGSERIAL PRIMARY KEY` (PostgreSQL)
- No Django: **nada!** O Django cria o `id` sozinho.

Se quiser escolher outro campo como chave primária:
```python
matricula = models.CharField(max_length=20, primary_key=True)
```
> Aí o Django **não cria** o `id` automático.

---

## 3. Tabela-resumo dos tipos

| O que quero guardar            | SQL                     | Django                                              |
|--------------------------------|-------------------------|-----------------------------------------------------|
| Texto curto (com limite)       | `VARCHAR(n)`            | `CharField(max_length=n)`                           |
| Texto longo                    | `TEXT`                  | `TextField()`                                       |
| E-mail                         | `VARCHAR(254)`          | `EmailField()`                                      |
| Site / link                    | `VARCHAR(200)`          | `URLField()`                                        |
| Inteiro                        | `INTEGER`               | `IntegerField()`                                    |
| Inteiro pequeno                | `SMALLINT`              | `SmallIntegerField()`                               |
| Inteiro grande                 | `BIGINT`                | `BigIntegerField()`                                 |
| Inteiro não negativo           | `INTEGER` + `CHECK >= 0`| `PositiveIntegerField()`                            |
| Dinheiro / decimal exato       | `DECIMAL(10,2)`         | `DecimalField(max_digits=10, decimal_places=2)`     |
| Decimal aproximado             | `FLOAT` / `REAL`        | `FloatField()`                                      |
| Verdadeiro/falso               | `BOOLEAN`               | `BooleanField()`                                    |
| Data                           | `DATE`                  | `DateField()`                                       |
| Hora                           | `TIME`                  | `TimeField()`                                       |
| Data e hora                    | `DATETIME`/`TIMESTAMP`  | `DateTimeField()`                                   |
| Arquivo                        | `VARCHAR(100)`          | `FileField(upload_to='...')`                        |
| Imagem                         | `VARCHAR(100)`          | `ImageField(upload_to='...')`                       |
| Chave primária automática      | `BIGINT AUTO_INCREMENT PRIMARY KEY` | *(automático)*                          |

---

## 4. Restrições (regras das colunas)

### 4.1 Obrigatório ou opcional: `NOT NULL` e `NULL`

No **SQL**, você escreve `NOT NULL` para dizer que o campo é obrigatório.

No **Django**, é o contrário: **todo campo já nasce obrigatório** (NOT NULL). Para deixar opcional, você libera:

| Situação             | SQL                          | Django                              |
|----------------------|------------------------------|-------------------------------------|
| Obrigatório          | `nome VARCHAR(100) NOT NULL` | `CharField(max_length=100)`         |
| Opcional (pode ficar vazio) | `apelido VARCHAR(100) NULL` | `CharField(max_length=100, null=True, blank=True)` |

**Qual a diferença entre `null` e `blank`?**
- `null=True` → regra do **banco**: a coluna aceita `NULL`.
- `blank=True` → regra do **formulário**: o usuário pode deixar o campo em branco.

> 💡 **Dica simples:** para campos opcionais, use os dois juntos: `null=True, blank=True`.
> Exceção: em campos de texto (`CharField`, `TextField`) muitos programadores usam só `blank=True`, e o valor vazio fica como `''` (texto vazio).

---

### 4.2 Valor único: `UNIQUE`

Não pode repetir (ex.: CPF, e-mail, matrícula).

- No SQL: `cpf VARCHAR(14) UNIQUE`
- No Django:
```python
cpf = models.CharField(max_length=14, unique=True)
```

**Único em conjunto** (ex.: o mesmo aluno não pode se matricular 2 vezes na mesma disciplina):

SQL:
```sql
UNIQUE (aluno_id, disciplina_id)
```

Django:
```python
class Meta:
    constraints = [
        models.UniqueConstraint(fields=['aluno', 'disciplina'], name='matricula_unica')
    ]
```

---

### 4.3 Valor padrão: `DEFAULT`

Se ninguém informar o valor, usa esse.

- No SQL: `ativo BOOLEAN DEFAULT TRUE`
- No Django:
```python
ativo = models.BooleanField(default=True)
```

> Observação: com `default`, quem preenche o valor é o **Django** na hora de salvar. Se quiser que o **banco** também tenha o DEFAULT, use `db_default=` (Django 5.0 ou mais novo).

---

### 4.4 Verificação: `CHECK`

Garante uma regra (ex.: preço não pode ser negativo).

SQL:
```sql
preco DECIMAL(10,2) CHECK (preco >= 0)
```

Django:
```python
class Produto(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(preco__gte=0),   # gte = maior ou igual
                name='preco_nao_negativo'
            )
        ]
```
> Em versões antigas do Django (antes da 5.1), escreva `check=` no lugar de `condition=`.

**Atalhos úteis do `models.Q`:**

| Django      | Significado     | SQL  |
|-------------|-----------------|------|
| `__gt`      | maior que       | `>`  |
| `__gte`     | maior ou igual  | `>=` |
| `__lt`      | menor que       | `<`  |
| `__lte`     | menor ou igual  | `<=` |

---

### 4.5 Lista de opções (ex.: turno)

No SQL puro isso seria um `CHECK (turno IN ('M', 'V', 'N'))` ou um `ENUM` (MySQL).

No Django usamos `choices`:
```python
class Aluno(models.Model):
    TURNOS = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]
    turno = models.CharField(max_length=1, choices=TURNOS)
```
- O primeiro valor (`'M'`) é o que vai **para o banco**.
- O segundo (`'Matutino'`) é o que aparece **para o usuário**.

> ⚠️ O `choices` é validado pelo Django (formulários e admin), **não** vira `CHECK` no banco automaticamente.

---

### 4.6 Índice: `INDEX`

Deixa as buscas mais rápidas em um campo muito pesquisado.

- No SQL: `CREATE INDEX idx_nome ON aluno (nome);`
- No Django:
```python
nome = models.CharField(max_length=200, db_index=True)
```

> Campos com `unique=True` e `ForeignKey` **já ganham índice** automaticamente.

---

### 4.7 Tabela-resumo das restrições

| Restrição SQL        | Django                                     |
|----------------------|--------------------------------------------|
| `NOT NULL`           | *(padrão, não precisa escrever)*           |
| `NULL`               | `null=True` (+ `blank=True`)               |
| `UNIQUE`             | `unique=True`                              |
| `UNIQUE (a, b)`      | `UniqueConstraint(fields=['a','b'], ...)`  |
| `DEFAULT valor`      | `default=valor`                            |
| `CHECK (...)`        | `CheckConstraint(condition=Q(...), ...)`   |
| `PRIMARY KEY`        | *(automático)* ou `primary_key=True`       |
| `CREATE INDEX`       | `db_index=True`                            |
| `FOREIGN KEY`        | `ForeignKey(...)` (veja abaixo)            |

---

## 5. Relacionamentos entre tabelas

### 5.1 Um para muitos (1:N) — `FOREIGN KEY`

Exemplo: **um curso tem muitos alunos**, e cada aluno pertence a **um** curso.

SQL:
```sql
CREATE TABLE aluno (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    curso_id BIGINT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES curso(id) ON DELETE CASCADE
);
```

Django:
```python
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
```

> Repare: no Django você escreve `curso`, mas no banco a coluna vira **`curso_id`**. O Django acrescenta o `_id` sozinho.

**O que acontece quando o "pai" é apagado? (`on_delete`)**

| Django                     | SQL equivalente         | O que faz                                                         |
|----------------------------|-------------------------|-------------------------------------------------------------------|
| `models.CASCADE`           | `ON DELETE CASCADE`     | Apaga o curso → apaga os alunos dele também                       |
| `models.PROTECT`           | `ON DELETE RESTRICT`    | Não deixa apagar o curso se ele tiver alunos                      |
| `models.SET_NULL`          | `ON DELETE SET NULL`    | Apaga o curso → o `curso_id` dos alunos vira `NULL` (precisa de `null=True`) |
| `models.SET_DEFAULT`       | `ON DELETE SET DEFAULT` | Coloca o valor padrão (precisa de `default=`)                     |
| `models.DO_NOTHING`        | *(nada)*                | Não faz nada (cuidado: pode dar erro no banco)                    |

> 💡 Curiosidade: no Django, quem executa o `on_delete` é o **próprio Django**, e não o banco. O resultado para você é o mesmo.

---

### 5.2 Um para um (1:1) — `FOREIGN KEY` + `UNIQUE`

Exemplo: **cada aluno tem um único perfil**.

SQL:
```sql
aluno_id BIGINT NOT NULL UNIQUE,
FOREIGN KEY (aluno_id) REFERENCES aluno(id)
```

Django:
```python
class Perfil(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
```

---

### 5.3 Muitos para muitos (N:N) — tabela intermediária

Exemplo: **um aluno cursa várias disciplinas**, e **uma disciplina tem vários alunos**.

No SQL, você precisa criar uma **terceira tabela** manualmente:
```sql
CREATE TABLE aluno_disciplina (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    aluno_id BIGINT NOT NULL,
    disciplina_id BIGINT NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES aluno(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplina(id),
    UNIQUE (aluno_id, disciplina_id)
);
```

No Django, basta **uma linha** (a tabela intermediária é criada sozinha):
```python
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    disciplinas = models.ManyToManyField(Disciplina)
```

---

## 6. Exemplo completo lado a lado

### No SQL
```sql
CREATE TABLE curso (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    carga_horaria INTEGER NOT NULL CHECK (carga_horaria > 0)
);

CREATE TABLE disciplina (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE aluno (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    nome VARCHAR(200) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    turno VARCHAR(1) NOT NULL CHECK (turno IN ('M', 'V', 'N')),
    media DECIMAL(4, 2) NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    foto VARCHAR(100) NULL,
    criado_em DATETIME NOT NULL,
    curso_id BIGINT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES curso(id) ON DELETE RESTRICT
);

CREATE TABLE aluno_disciplinas (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    aluno_id BIGINT NOT NULL,
    disciplina_id BIGINT NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES aluno(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplina(id),
    UNIQUE (aluno_id, disciplina_id)
);
```

### No Django (`models.py`)
```python
from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    carga_horaria = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(carga_horaria__gt=0),
                name='carga_horaria_positiva'
            )
        ]

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    TURNOS = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]

    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    turno = models.CharField(max_length=1, choices=TURNOS)
    media = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    disciplinas = models.ManyToManyField(Disciplina, blank=True)

    def __str__(self):
        return self.nome
```

> O método `__str__` não existe no SQL. Ele só define **como o objeto aparece** (por exemplo, no painel admin).

---

## 7. Nome das tabelas no Django

O Django dá nome às tabelas assim: **`nomedoapp_nomedomodel`** (tudo minúsculo).

Exemplo: model `Aluno` no app `escola` → tabela **`escola_aluno`**.

Para escolher outro nome:
```python
class Aluno(models.Model):
    ...
    class Meta:
        db_table = 'aluno'
```

---

## 8. Do model para o banco: os comandos

Depois de escrever ou alterar o `models.py`:

```bash
python manage.py makemigrations   # 1. Gera o "plano" das mudanças
python manage.py migrate          # 2. Aplica as mudanças no banco (executa o SQL)
```

**Quer ver o SQL que o Django gerou?** (ótimo para estudar!)
```bash
python manage.py sqlmigrate escola 0001
```
Troque `escola` pelo nome do seu app e `0001` pelo número da migration.

---

## 9. Erros comuns (e como resolver)

| Erro / problema                                            | Solução                                                       |
|------------------------------------------------------------|---------------------------------------------------------------|
| Esqueci o `max_length` no `CharField`                      | Todo `CharField` precisa de `max_length=...`                  |
| Usei `FloatField` para preço                               | Troque por `DecimalField(max_digits=..., decimal_places=...)` |
| Esqueci o `on_delete` no `ForeignKey`                      | É obrigatório: use `models.CASCADE`, `models.PROTECT`, etc.   |
| Usei `SET_NULL` e deu erro                                 | O campo precisa de `null=True`                                |
| Adicionei campo obrigatório numa tabela que já tem dados   | Dê um `default=` ou use `null=True`                           |
| Mudei o model e nada mudou no banco                        | Rode `makemigrations` **e** `migrate`                         |
| `ImageField` dá erro de Pillow                             | Rode `pip install Pillow`                                     |

---

## 10. Colinha final

```python
# Texto
models.CharField(max_length=100)       # VARCHAR(100)
models.TextField()                     # TEXT
models.EmailField()                    # VARCHAR(254)

# Números
models.IntegerField()                  # INTEGER
models.DecimalField(max_digits=10, decimal_places=2)  # DECIMAL(10,2)
models.FloatField()                    # FLOAT

# Outros
models.BooleanField(default=True)      # BOOLEAN DEFAULT TRUE
models.DateField()                     # DATE
models.DateTimeField(auto_now_add=True)  # DATETIME

# Restrições
null=True, blank=True                  # NULL (opcional)
unique=True                            # UNIQUE
default=valor                          # DEFAULT
db_index=True                          # INDEX

# Relacionamentos
models.ForeignKey(Outro, on_delete=models.CASCADE)      # 1:N
models.OneToOneField(Outro, on_delete=models.CASCADE)   # 1:1
models.ManyToManyField(Outro)                           # N:N
```
