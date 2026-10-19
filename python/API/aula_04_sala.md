# Aula 04 (Atividade em sala): Autenticação na API

> **Material do Prof. Bruno Gomes:**
> Django REST Framework no projeto FIC (IFRN)

**Pré-requisito:** Aula 03 concluída (APIs de `areas/`, `publicos/` e `cursos/` funcionando).

## O que vamos fazer hoje

Hoje a nossa API está **aberta**: qualquer pessoa cadastra, edita e remove áreas, públicos e cursos, sem login nenhum. Nesta atividade você vai:

1. **Parte 1:** proteger a API com a autenticação **tradicional do Django** (sessão + cookie),
   a mesma que o site já usa. No final, você vai criar um script Python para testar.
2. **Parte 2:** modificar o que foi feito na Parte 1 para usar **JWT** (token). No final,
   você vai criar outro script Python para testar.

Siga os passos **na ordem**.

Deixe o `runserver` rodando em um terminal e use outro terminal para os testes.

---

## Antes de começar: confirme que a API está aberta

Crie um arquivo `teste_aberta.py` (fora da pasta do projeto ou na raiz, tanto faz) e rode:

```python
import requests

URL = 'http://127.0.0.1:8000/api/v1/'

r = requests.post(URL + 'areas/', json={'nome': 'Qualquer coisa'})
print(r.status_code)
requests.delete(URL + f"areas/{r.json()['id']}/")
```

Anote o `status_code` que apareceu. Se foi `201`, qualquer pessoa consegue cadastrar.
É isso que vamos resolver.

Lembre da diferença:

| Conceito | Pergunta | No DRF |
|---|---|---|
| **Autenticação** | *Quem* está fazendo a requisição? | *Authentication classes* |
| **Permissão** | Essa pessoa *pode* fazer isso? | *Permission classes* |

---

# Parte 1: Autenticação simples (sessão do Django)

## Passo 1: Configurar a autenticação no `settings.py`

Abra `fic/settings.py` e acrescente no **final** do arquivo:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

O que cada parte faz:

- `SessionAuthentication`: o DRF descobre o `request.user` pela **sessão** (cookie
  `sessionid`), igual ao site. Ela também exige o **token CSRF** em `POST`, `PUT` e `DELETE`.
- `IsAuthenticatedOrReadOnly`: `GET` liberado para todos; `POST`, `PUT` e `DELETE` só para
  quem está logado.

Rode de novo o `teste_aberta.py`. Qual `status_code` apareceu agora?

> Repare que você **não mexeu em nenhuma view** e a API já ficou protegida.

## Passo 2: Login pela Browsable API

Abra `fic/urls.py` e acrescente a rota `api-auth/`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('cursos/', include('apps.cursos.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('api/', include('apps.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
```

Agora faça o teste no navegador:

1. Abra `http://127.0.0.1:8000/api/v1/areas/`.
2. Clique em **Log in** no canto superior direito e entre com um usuário já cadastrado no site.
3. Cadastre uma área pela caixa *Content* (botão **POST**).
4. Clique em **Log out** e tente cadastrar de novo. O que aconteceu?

> Teste também: faça login pelo site (`/login/`) e depois abra a API na mesma aba.
> Funciona porque é a **mesma sessão**.

## Passo 3: Criar o `UsuarioSerializer`

O login pela API vai devolver os dados do usuário. Abra `apps/api/serializers.py`,
acrescente o import e o serializer:

```python
from apps.usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'username', 'first_name', 'last_name', 'email', 'nascimento']
        read_only_fields = ['cpf']
```

- `password` **não** está em `fields`: a senha nunca sai na resposta.
- `read_only_fields = ['cpf']`: o `cpf` é a chave primária, então ele aparece na resposta,
  mas não pode ser alterado (mesma ideia do `meus_dados` do site).

## Passo 4: Criar as views `entrar` e `sair`

Abra `apps/api/views.py` e acrescente os imports:

```python
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UsuarioSerializer
```

> O `api_view` já estava importado. Basta acrescentar o `permission_classes` na mesma linha.

Agora crie as duas views:

```python
@api_view(['POST'])
@permission_classes([AllowAny])
def entrar(request):
    usuario = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
    if usuario is None:
        return Response({'detail': 'Usuário ou senha inválidos.'}, status=status.HTTP_401_UNAUTHORIZED)
    login(request, usuario)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)

@api_view(['POST'])
def sair(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
```

Compare com a view `autenticar` do site (`apps/core/views.py`): é o **mesmo**
`authenticate()` + `login()`. Muda só a entrada (`request.data`) e a saída (JSON).

Atenção a três detalhes:

- `@permission_classes([AllowAny])` libera o login para quem ainda **não** está logado.
  Sem ele, o padrão `IsAuthenticatedOrReadOnly` exigiria login para fazer login.
- O `@permission_classes` precisa ficar **abaixo** do `@api_view`.
- Não chame as views de `login` e `logout`: elas iriam substituir as funções do Django
  importadas acima. Por isso `entrar` e `sair`.

## Passo 5: Criar as rotas

Abra `apps/api/urls.py` e acrescente no final da lista:

```python
    # aula 04
    path('login/', entrar, name='api_login'),
    path('logout/', sair, name='api_logout'),
```

Abra `http://127.0.0.1:8000/api/v1/login/` no navegador e faça um `POST` com:

```json
{"username": "seu_usuario", "password": "sua_senha"}
```

Teste com a senha certa e com a senha errada.

## Passo 6: Entenda o que o cliente precisa mandar

Com sessão, um script Python precisa fazer o mesmo que o navegador faz sozinho:

| O navegador faz sozinho | No script Python você precisa |
|---|---|
| Guarda e reenvia os cookies | Usar `requests.Session()` no lugar de `requests` |
| Manda o token CSRF no formulário | Mandar o cabeçalho `X-CSRFToken` com o valor do cookie `csrftoken` |

Depois do login, o servidor devolve **dois** cookies:

- `sessionid`: diz quem é você.
- `csrftoken`: o token CSRF, que precisa ir no cabeçalho em todo `POST`, `PUT` e `DELETE`.

## Atividade 1: Script `teste_sessao.py`

Agora é com você. Crie o arquivo `teste_sessao.py` que teste a autenticação por sessão.
O script deve, **nesta ordem**, imprimir o `status_code` (e o JSON, quando houver) de cada item:

1. `GET api/areas/` **sem** login. (Esperado: `200`)
2. `POST api/areas/` **sem** login. (Esperado: `403`)
3. `POST api/login/` com a senha **errada**. (Esperado: `401`)
4. `POST api/login/` com a senha **certa**. Imprima também os cookies recebidos.
   (Esperado: `200`)
5. `POST api/areas/` logado, mas **sem** o cabeçalho `X-CSRFToken`. (Esperado: `403`)
6. `POST api/areas/` logado e **com** o `X-CSRFToken`. (Esperado: `201`)
7. `DELETE` da área criada no item 6. (Esperado: `204`)
8. `POST api/logout/`. Imprima os cookies de novo. (Esperado: `204`)
9. `POST api/areas/` depois do logout. (Esperado: `403`)

Dicas:

- `s = requests.Session()` e depois use `s.get(...)`, `s.post(...)`, `s.delete(...)`.
- Os cookies ficam em `s.cookies.get_dict()`.
- O cabeçalho: `headers={'X-CSRFToken': s.cookies['csrftoken']}`.
- O logout também é `POST`, então também precisa do CSRF.

Responda como comentário no final do script:

- Qual cookie sumiu depois do logout?
- Por que o item 5 deu erro, se você já estava logado?

---

# Parte 2: Modificando para JWT

A sessão funciona, mas veja o trabalho que o script teve: guardar cookies e mandar o
CSRF em toda requisição. Para apps e outros sistemas, o mais comum é usar **token**.
O formato mais usado é o **JWT** (*JSON Web Token*).

Como funciona:

1. O cliente manda usuário e senha para `api/token/` e recebe **dois** tokens:
   - `access`: vai em **toda** requisição, no cabeçalho. Vale pouco tempo.
   - `refresh`: serve só para pedir um `access` novo quando ele vencer. Vale mais tempo.
2. Nas requisições, o cliente manda o cabeçalho:
   `Authorization: Bearer <access>`
3. Não tem cookie e **não precisa de CSRF**.

## Passo 1: Instalar o Simple JWT

```bash
venv/Scripts/python.exe -m pip install djangorestframework-simplejwt
```

Acrescente no `requirements.txt` (mantenha o arquivo em UTF-8):

```
django
Pillow
django-widget-tweaks
djangorestframework
djangorestframework-simplejwt
```

Documentação: https://django-rest-framework-simplejwt.readthedocs.io/

## Passo 2: Registrar no `INSTALLED_APPS`

Em `fic/settings.py`, acrescente a linha do `token_blacklist`:

```python
INSTALLED_APPS = [
    ...
    'widget_tweaks',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'apps.core',
    'apps.usuarios',
    'apps.cursos',
    'apps.api',
]
```

O `token_blacklist` é a "lista negra" de tokens, usada no logout. Ele cria tabelas no banco,
então rode:

```bash
venv/Scripts/python.exe manage.py migrate
```

## Passo 3: Trocar a autenticação no `settings.py`

Substitua o `REST_FRAMEWORK` da Parte 1 por:

```python
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'USER_ID_FIELD': 'username',
}
```

> Coloque o `from datetime import timedelta` junto dos outros imports, no topo do arquivo.

Repare:

- O `JWTAuthentication` entrou em **1º lugar**. O `SessionAuthentication` continua em 2º só
  para a Browsable API funcionar no navegador.
- As **permissões não mudaram**.
- `USER_ID_FIELD = 'username'` é **obrigatório** no nosso projeto: o `Usuario` não tem `id`
  (a chave primária é o `cpf`). Sem essa linha, o login dá
  `AttributeError: 'Usuario' object has no attribute 'id'`.

> Por que não usar o `cpf`? O conteúdo do JWT pode ser lido por **qualquer pessoa**.
> Colocar o CPF no token seria expor um dado pessoal.

## Passo 4: Trocar as rotas `login/` e `logout/` pelas rotas de token

Abra `apps/api/urls.py`. Acrescente o import:

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
```

**Remova** as rotas `login/` e `logout/` da Parte 1 e coloque no lugar:

```python
    # aula 04
    path('token/', TokenObtainPairView.as_view(), name='api_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='api_token_blacklist'),
```

| Rota | Recebe | Devolve | Substitui |
|---|---|---|---|
| `POST api/token/` | `username` e `password` | `access` e `refresh` | `login/` |
| `POST api/token/refresh/` | `refresh` | um `access` novo | (não existia) |
| `POST api/token/blacklist/` | `refresh` | invalida o `refresh` | `logout/` |

> Essas views são **classes** da biblioteca (por isso o `.as_view()`). As nossas views
> continuam sendo funções.

## Passo 5: Apagar o que não é mais usado

Em `apps/api/views.py`, **apague**:

- as views `entrar` e `sair`;
- o import `from django.contrib.auth import authenticate, login, logout`.

> Se apagar as views e esquecer as rotas no `urls.py`, vai aparecer
> `NameError: name 'entrar' is not defined`.

Deixe o `UsuarioSerializer`: ele vai ser usado na próxima aula.

## Passo 6: Verificar

Rode o `check` e depois o `teste_aberta.py` de novo. Compare o `status_code` com o da
Parte 1. Mudou de `403` para `401`?

Teste também na Browsable API: abra `http://127.0.0.1:8000/api/v1/token/` e faça um `POST`
com seu usuário e senha. Copie o `access` e cole em https://jwt.io para ver o conteúdo do token.
Procure o campo `user_id`: o que aparece nele?

## Atividade 2: Script `teste_jwt.py`

Agora crie o arquivo `teste_jwt.py` que teste a autenticação com JWT. O script deve,
**nesta ordem**, imprimir o `status_code` (e o JSON, quando houver) de cada item:

1. `POST api/areas/` **sem** token. Imprima também o cabeçalho `WWW-Authenticate` da
   resposta. (Esperado: `401`)
2. `POST api/token/` com a senha **errada**. (Esperado: `401`)
3. `POST api/token/` com a senha **certa**. Guarde o `access` e o `refresh`.
   (Esperado: `200`)
4. Leia o conteúdo do `access` **em Python** e imprima o `user_id` e quanto tempo o token
   vale (`exp - iat`, em segundos).
5. `POST api/areas/` com o cabeçalho `Authorization`. (Esperado: `201`)
6. `DELETE` da área criada no item 5. (Esperado: `204`)
7. `GET api/areas/` com um token **inválido** (ex.: `'Bearer abc.def.ghi'`). (Esperado: `401`)
8. `POST api/token/refresh/` com o `refresh`. Troque o `access` antigo pelo novo.
   (Esperado: `200`)
9. `POST api/token/blacklist/` com o `refresh` (logout). (Esperado: `200`)
10. `POST api/token/refresh/` de novo com o mesmo `refresh`. (Esperado: `401`)
11. `POST api/areas/` com o `access` do item 8, depois do logout. Anote o resultado.

Dicas:

- Aqui **não** precisa de `requests.Session()`: não tem cookie para guardar.
- O cabeçalho: `headers={'Authorization': 'Bearer ' + access}` (com espaço depois de `Bearer`).
- No cabeçalho vai o **`access`**. O `refresh` só vai no corpo (`json=`) de
  `token/refresh/` e `token/blacklist/`.
- Para ler o conteúdo do token, ele tem 3 partes separadas por ponto
  (`cabeçalho.conteúdo.assinatura`). Pegue a parte do meio e use:
  ```python
  import base64, json

  conteudo = access.split('.')[1]
  conteudo += '=' * (-len(conteudo) % 4)
  print(json.loads(base64.urlsafe_b64decode(conteudo)))
  ```

Responda como comentário no final do script:

- No item 11, o `access` continuou funcionando depois do logout? Por quê?
  (Compare com o logout da sessão na Parte 1.)
- Por que no JWT não foi preciso mandar o token CSRF?
- O conteúdo do token é criptografado? O que impede alguém de alterar o `user_id`?

---

## Problemas comuns

| Sintoma | Solução |
|---|---|
| `403 CSRF Failed: CSRF token missing.` | Faltou o cabeçalho `X-CSRFToken` (Parte 1) |
| `KeyError: 'csrftoken'` | O login não deu certo: confira o `status_code` do `login/` |
| `POST login/` pede login | Faltou `@permission_classes([AllowAny])` no `entrar` |
| `@permission_classes` não faz efeito | Ele tem que ficar **abaixo** do `@api_view` |
| Browsable API sem o link **Log in** | Faltou `path('api-auth/', include('rest_framework.urls'))` |
| `No module named 'rest_framework_simplejwt'` | Instale com `venv/Scripts/python.exe -m pip install djangorestframework-simplejwt` |
| `'Usuario' object has no attribute 'id'` | Faltou `'USER_ID_FIELD': 'username'` no `SIMPLE_JWT` |
| `no such table: token_blacklist_outstandingtoken` | Faltou rodar o `migrate` |
| `401 Given token not valid for any token type` | Token errado ou vencido: faça login de novo ou use `token/refresh/` |
| Sem token continua vindo `403` em vez de `401` | O `SessionAuthentication` ficou antes do `JWTAuthentication` |
