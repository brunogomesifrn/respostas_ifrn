# Aula do Prof. Bruno Gomes

- Turma: TSI4V
- Disciplina: Desenvolvimento de Sistemas Corporativos

## Consumindo uma API REST com Python

### API: JSONPlaceholder

```
https://jsonplaceholder.typicode.com
```

Recursos disponíveis: `/posts`, `/comments`, `/albums`, `/photos`, `/todos`, `/users`.

### CMD / PROMPT / Power Shell

- Abrir o prompt e entrar na pasta da aula:

```bash
cd corporativos
cd api
venv\Scripts\activate
code .
```

### Arquivo Python

- Criar o arquivo: `02_aula_methds.py`

#### GET - vários posts

```python
import requests

URL = 'https://jsonplaceholder.typicode.com'

resposta = requests.get(URL+"/posts")

print("Status:", resposta.status_code)

posts = resposta.json()
print("Total de posts:", len(posts))

# Mostra todos os títulos
for post in posts:
    print(post['id']," - ",post['title'])

# Mostra só os 3 primeiros títulos
for post in posts[:3]:
    print(post['id']," - ",post['title'])
```

#### GET - buscando um post

```python
import requests

URL = 'https://jsonplaceholder.typicode.com'

resposta = requests.get(URL+"/posts/1")

print("Status:", resposta.status_code)

post = resposta.json()

print("Título:", post["title"])
print("Conteúdo:", post["body"])
```

#### POST - criando 1 post

```python
import requests

novo = {
    "title": "Aula API",
    "body": "Aprendendo API com BG!",
    "userId": 1,
}

URL = 'https://jsonplaceholder.typicode.com'

resposta = requests.post(URL+"/posts", json=novo)

print("Status:", resposta.status_code)

print("Resposta:", resposta.json())
```


#### PUT - atualizando um post

```python
import requests

atualizado = {
    "id": 1,
    "title": "Título atualizado",
    "body": "Conteúdo totalmente novo.",
    "userId": 1,
}

URL = 'https://jsonplaceholder.typicode.com'

resposta = requests.put(URL+"/posts/1", json=atualizado)

print("Status:", resposta.status_code)

print("Resposta:", resposta.json())

```

#### DELETE - removendo um post

```python
import requests

URL = 'https://jsonplaceholder.typicode.com'

resposta = requests.delete(URL+"/posts/1")

print("Status:", resposta.status_code)

print("Resposta:", resposta.json())
```


#### Tratando erros

```python
try:
    URL = 'https://jsonplaceholder.typicode.com'
    resposta = requests.get(URL+"/posts/1", timeout=5)
    resposta.raise_for_status() # gera erro se o status for 4xx ou 5xx
    print(resposta.json())
except requests.exceptions.Timeout:
    print("A API demorou para responder.")
except requests.exceptions.HTTPError as erro:
    print("Erro HTTP:", erro)
except requests.exceptions.ConnectionError:
    print("Não foi possível conectar. Verifique sua internet.")
```

## Para praticar

1. Liste todas as **tarefas** (`/todos`) do usuário de `userId` **2** e mostre quantas estão concluídas (`"completed": true`).
2. Busque o **usuário** de id **3** (`/users/3`) e exiba seu nome, e-mail e cidade (dica: a cidade fica em `address` → `city`).
3. Liste os **comentários** do post de id **5** (`/posts/5/comments`) mostrando o e-mail de quem comentou.
4. **Desafio:** escolha um endpoint e crie um menu no terminal (1 - Listar, 2 - Buscar, 3 - Criar, 4 - Atualizar, 5 - Excluir, 0 - Sair). Dica: usar função.