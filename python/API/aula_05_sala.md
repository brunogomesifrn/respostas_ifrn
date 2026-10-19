# Aula 05 (Atividade em sala): API de cadastro de usuários

> **Material do Prof. Bruno Gomes**
> Curso: Django REST Framework no projeto FIC (IFRN)

**Pré-requisito:** Atividade da Aula 04 concluída (API autenticando com JWT, rotas
`token/`, `token/refresh/` e `token/blacklist/` funcionando e `UsuarioSerializer` criado).

## O que vamos fazer hoje

Na aula passada, para testar o login, você usou um usuário cadastrado **pelo site**.
Hoje você vai criar a API para:

1. **Cadastrar** um usuário novo (`POST api/cadastro/`), com senha criptografada,
   confirmação de senha e validação do CPF. O usuário já sai do cadastro **com os tokens**.
2. **Ver e editar os próprios dados** (`GET` e `PUT api/eu/`), igual ao `meus_dados` do site.

No final, você vai criar um script Python para testar tudo.

Siga os passos **na ordem**. Ao final de cada passo, rode o `check`:

```bash
venv/Scripts/python.exe manage.py check
```

Deixe o `runserver` rodando em um terminal e use outro terminal para os testes.

---

## Passo 1: Veja como o site faz o cadastro

Abra `apps/core/forms.py` e veja o `UsuarioFormCadastro`. Ele herda de `UserCreationForm`,
que faz duas coisas que o nosso serializer vai ter que fazer **à mão**:

- pede a senha **duas vezes** e confere se são iguais;
- **criptografa** a senha antes de salvar.

Abra também `apps/usuarios/models.py` e repare: a chave primária do `Usuario` é o `cpf`,
e o `email` é único.

## Passo 2: Criar o `UsuarioCadastroSerializer`

Abra `apps/api/serializers.py` e crie, abaixo do `UsuarioSerializer`:

```python
class UsuarioCadastroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['cpf', 'username', 'first_name', 'last_name', 'email', 'nascimento', 'password', 'password2']
```

O que tem de novo:

- `write_only=True`: o campo é aceito na **entrada**, mas **nunca** aparece na resposta.
  A senha não volta para o cliente.
- `password2` **não existe** no model. É um campo só do serializer, para a confirmação.
- O `cpf` está em `fields` e **não** é somente leitura: no cadastro ele é obrigatório,
  já que é um registro novo.

Rode o `check`.

## Passo 3: Validar o CPF

Ainda no `UsuarioCadastroSerializer`, acrescente o método abaixo (dentro da classe, depois
do `Meta`):

```python
    def validate_cpf(self, valor):
        if not valor.isdigit() or len(valor) != 11:
            raise serializers.ValidationError('Informe o CPF com 11 números, sem pontos e traço.')
        return valor
```

É o mesmo tipo de validação do `validate_vagas` da aula 03: `validate_<nome_do_campo>`.
O model só limita o tamanho a 11 caracteres; aqui exigimos 11 **dígitos**.

## Passo 4: Conferir as duas senhas

Acrescente mais um método na classe:

```python
    def validate(self, dados):
        if dados['password'] != dados['password2']:
            raise serializers.ValidationError({'password2': 'As senhas não conferem.'})
        return dados
```

- O `validate` (sem nome de campo) valida o **objeto inteiro**. Ele é chamado depois das
  validações de cada campo e recebe um dicionário com todos os dados.
- Use quando a regra envolve **mais de um campo**, como aqui. É o `clean()` dos
  formulários Django.
- O dicionário `{'password2': ...}` faz o erro aparecer no campo `password2`.

## Passo 5: Salvar com a senha criptografada

Acrescente o último método na classe:

```python
    def create(self, dados):
        dados.pop('password2')
        return Usuario.objects.create_user(**dados)
```

- O `serializer.save()` chama o `create()` quando é um cadastro.
- O `create()` padrão faria `Usuario.objects.create(**dados)`, que grava a senha em
  **texto puro**. Por isso trocamos por `create_user()`, que criptografa a senha.
- O `password2` precisa sair do dicionário antes de salvar, porque não existe no model.

> Faça o experimento no final da atividade (Passo 10) para ver o problema acontecendo.

## Passo 6: Criar a view `cadastro`

Abra `apps/api/views.py` e acrescente os imports:

```python
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UsuarioSerializer, UsuarioCadastroSerializer
```

> Se o `AllowAny` ou o `UsuarioSerializer` já estiverem importados da aula passada, só
> complete a linha que já existe.

Agora crie a view:

```python
@api_view(['POST'])
@permission_classes([AllowAny])
def cadastro(request):
    serializer = UsuarioCadastroSerializer(data=request.data)
    if serializer.is_valid():
        usuario = serializer.save()
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'usuario': UsuarioSerializer(usuario).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Repare:

- `AllowAny`: quem está se cadastrando ainda não tem login.
- Usamos **dois** serializers: o `UsuarioCadastroSerializer` para **receber** os dados e o
  `UsuarioSerializer` para **devolver** (sem senha). Mesma ideia do `CursoSerializer` e
  `CursoLeituraSerializer` da aula 03.
- `RefreshToken.for_user(usuario)` gera os tokens **sem** pedir a senha de novo: o usuário
  acabou de se cadastrar. Assim ele já sai do cadastro logado.

## Passo 7: Criar a rota `cadastro/`

Abra `apps/api/urls.py` e acrescente no final da lista:

```python
    # aula 05
    path('cadastro/', cadastro, name='api_cadastro'),
```

Rode o `check`. Abra `http://127.0.0.1:8000/api/v1/cadastro/` no navegador e cadastre um usuário:

```json
{
    "cpf": "12345678901",
    "username": "maria",
    "first_name": "Maria",
    "last_name": "Silva",
    "email": "maria@ifrn.edu.br",
    "password": "senha123",
    "password2": "senha123"
}
```

Agora tente:

1. Mandar o **mesmo** cadastro de novo. Quais campos deram erro? Você escreveu alguma
   validação para eles?
2. Mandar `password2` diferente de `password`.
3. Mandar o CPF com letras, como `1234567890a`. E depois como `123.456.789-01`.
   A mensagem de erro foi a mesma nos dois casos?
4. Mandar `{}`.
5. Fazer login **no site** (`/login/`) com o usuário criado pela API.

> As validações de `cpf`, `username` e `email` repetidos vêm **de graça** do model
> (campos únicos).

## Passo 8: Criar a view `eu` (meus dados)

Agora o usuário logado vai poder ver e editar os próprios dados. Em `apps/api/views.py`:

```python
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def eu(request):
    if request.method == 'GET':
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    serializer = UsuarioSerializer(request.user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

E a rota em `apps/api/urls.py`:

```python
    path('eu/', eu, name='api_eu'),
```

Repare:

- **Não tem `id` na URL**: o usuário é sempre `request.user`, quem mandou o token.
  Assim ninguém consegue editar os dados de outra pessoa.
- `IsAuthenticated` bloqueia até o `GET`: são dados pessoais.
- Aqui usamos o `UsuarioSerializer`, que tem o `cpf` como **somente leitura**. Se o cliente
  mandar outro `cpf`, ele é ignorado.

> Cuidado: o `username` vai **dentro** do token (`USER_ID_FIELD = 'username'`). Se o
> usuário trocar o `username` pelo `PUT`, o token antigo para de funcionar e ele precisa
> fazer login de novo.

## Passo 9: Testar o `eu` na Browsable API

1. Faça login pelo site ou pelo `api-auth/` (a sessão continua funcionando na Browsable API).
2. Abra `http://127.0.0.1:8000/api/v1/eu/`. Aparecem os seus dados?
3. Mude o `first_name` e faça um **PUT**.
4. Tente mudar o `cpf`. O que aconteceu?
5. Faça logout e abra `api/eu/` de novo. Qual o `status_code`?

## Passo 10: Experimento: por que o `create_user()`?

1. No método `create` do `UsuarioCadastroSerializer`, troque **temporariamente** o
   `create_user` por `create`:
   ```python
   def create(self, dados):
       dados.pop('password2')
       return Usuario.objects.create(**dados)
   ```
2. Cadastre um usuário novo pela API (outro `cpf`, `username` e `email`).
3. Abra o shell e veja a senha gravada:
   ```bash
   venv/Scripts/python.exe manage.py shell
   ```
   ```python
   from apps.usuarios.models import Usuario
   print(Usuario.objects.get(username='NOME_QUE_VOCE_USOU').password)
   ```
4. Tente fazer login com esse usuário em `api/token/`. Funcionou?
5. **Volte** para o `create_user`, cadastre outro usuário e compare a senha no shell.

Anote o que apareceu nos dois casos. (Dica: o Django **nunca** guarda a senha, só o *hash*,
algo como `pbkdf2_sha256$...`.)

> Curiosidade: se você apagar o método `create` inteiro, o erro é outro:
> `Usuario() got unexpected keyword arguments: 'password2'`. O `create()` padrão tenta
> salvar o `password2` no model. Mais um motivo para o `dados.pop('password2')`.

---

## Atividade: Script `teste_cadastro.py`

Agora é com você. Crie o arquivo `teste_cadastro.py` que teste a API de cadastro de
usuários. Use dados **novos** (um `cpf`, `username` e `email` que ainda não existam no banco).

O script deve, **nesta ordem**, imprimir o `status_code` e o JSON de cada item:

1. `POST api/cadastro/` com `password2` **diferente** de `password`. (Esperado: `400`)
2. `POST api/cadastro/` com o CPF **com letras** (ex.: `1234567890a`). (Esperado: `400`
   com a mensagem do `validate_cpf`)
3. `POST api/cadastro/` com os dados **corretos**. Guarde o `access` e o `refresh` que vieram
   na resposta. (Esperado: `201`)
4. Confira que a resposta do item 3 **não** tem `password` nem `password2`. Imprima
   `True` ou `False`.
5. `POST api/cadastro/` com os **mesmos** dados do item 3. (Esperado: `400`)
6. `GET api/eu/` **sem** token. (Esperado: `401`)
7. `GET api/eu/` com o `access` do item 3. (Esperado: `200`)
8. `PUT api/eu/` mudando o `first_name` e mandando um `cpf` diferente. Imprima o
   `first_name` e o `cpf` da resposta. (Esperado: `200`, `first_name` novo e `cpf` antigo)
9. `POST api/token/` com o `username` e a senha cadastrados. (Esperado: `200`)
10. `POST api/token/blacklist/` com o `refresh` (logout). (Esperado: `200`)

Dicas:

- Monte os dados em um dicionário e altere só o que precisa em cada teste:
  ```python
  novo = {
      'cpf': '...',
      'username': '...',
      ...
  }
  ```
- O cabeçalho do token é o mesmo da aula passada:
  `headers={'Authorization': 'Bearer ' + access}`.
- No `PUT`, mande **todos** os campos do `UsuarioSerializer` (o `PUT` substitui o objeto inteiro).
- Para rodar o script várias vezes, mude o `cpf`, `username` e `email` antes de cada execução
  (ou apague o usuário pelo admin).

Responda como comentário no final do script:

- Por que o `cpf` não mudou no item 8?
- Qual a diferença entre o `UsuarioCadastroSerializer` e o `UsuarioSerializer`? Por que
  usamos os dois na view `cadastro`?
- Por que o usuário não precisou chamar `api/token/` logo depois do cadastro?

---

## Desafios (se terminar antes)

1. **Trocar a senha:** crie `PUT api/eu/senha/` que recebe `password` e `password2`.
   Use um serializer com os dois campos e o mesmo `validate()` do cadastro. Na view, use
   `request.user.set_password(...)` e `request.user.save()`.
   Pergunta: depois de trocar a senha, o `access` antigo continua funcionando?
2. **Listar usuários:** crie `GET api/usuarios/` que lista todos os usuários (com o
   `UsuarioSerializer`), mas só para **superusuário**. Se não for, devolva `403`.
   (Dica: `if not request.user.is_superuser:`, igual ao `usuarios_listar` do site.)
3. **Validadores de senha do Django:** faça a API recusar senhas fracas acrescentando
   `validators=[validate_password]` no campo `password` do `UsuarioCadastroSerializer`
   (`from django.contrib.auth.password_validation import validate_password`). O que acontece
   com `senha123`? Por quê? (Dica: veja o `AUTH_PASSWORD_VALIDATORS` no `settings.py`.)

---

## Problemas comuns

| Sintoma | Solução |
|---|---|
| A senha aparece na resposta | Faltou `write_only=True` no campo `password` |
| `Usuario() got unexpected keyword arguments: 'password2'` | Faltou `dados.pop('password2')` no `create` |
| Usuário cadastrado pela API não consegue fazer login | O `create` não usa `create_user()`: a senha foi gravada em texto puro |
| `POST cadastro/` pede login | Faltou `@permission_classes([AllowAny])` (abaixo do `@api_view`) |
| `name 'RefreshToken' is not defined` | Faltou `from rest_framework_simplejwt.tokens import RefreshToken` |
| `401` no `api/eu/` mesmo com token | Confira o formato: `'Bearer ' + access` (com espaço) e se mandou o `access`, não o `refresh` |
| `401 User not found` depois do `PUT api/eu/` | O `username` foi trocado e ele está dentro do token: faça login de novo |
| `400` no `PUT api/eu/` pedindo campos | O `PUT` precisa de todos os campos obrigatórios (`username`, `email`...) |
| `400` com "já existe" no cadastro | `cpf`, `username` ou `email` repetidos: use dados novos |
