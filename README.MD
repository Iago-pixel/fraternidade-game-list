<div align="center"><img src="./img/fraternidade-logo.jpeg"></div>

<h1 id="Sobre">Fraternidade Game List</h1>

## API feita para cadastrar jogos, permitir que os usuários votem neles e lista-los para ver os mais votados.

<br>

<h1 id="tabela-de-conteudo">Conteúdo</h1>

- [Sobre](#Sobre)
- [Tabela de Conteúdo](#tabela-de-conteudo)
- [Features](#features)
- [Tecnologias](#tecnologias)
- [Como usar](#como-usar)
  - [🎲 Rodando o Back End (servidor)](#rodar)
  - [Rotas](#rotas)

<h4 align="center"> 
	🚧  Em construção...  🚧
</h4>

<h3 id="features">Features</h3>

- [ ] CRUD usuário
- [x] CRUD jogo
- [x] Sistema de login
- [x] Sistema de voto

<h2 id="tecnologias">Tecnologias</h2>

- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Flask JWT Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)

<h2 id="como-usar">Como usar</h2>

Você terá que criar o arquivo .env baseado no .env.example e por o url de um banco de dados postgres. Perceba que a url tem que começar com postgresql! Você talvez queira criar um ambiente virtual também.

<h3 id="rodar">🎲 Rodando o Back End (servidor)</h3>

```bash
# Clone este repositório
$ git clone https://github.com/Iago-pixel/fraternidade-game-list.git

# Acesse a pasta do projeto no terminal/cmd
$ cd FRATERNIDADE-GAME-LIST

# Instale as dependências
$ pip install -r requirements.txt

# Execute a aplicação em modo de desenvolvimento
$ flask run

# O servidor inciará na porta:5000 - acesse http://localhost:5000
``
```

<h3 id="rotas">Rotas</h3>
<br>

#### **/users**

<br>

<p>POST 📬<p>

```
{
	"email": "test@test.com",
	"name": "Test",
	"password": "12345678iI*"
}
```

<p>201 CREATED ✔️</p>

```
{
	"email": "test@test.com",
	"is_adm": false,
	"name": "Test",
	"user_id": 1
}
```

<p>409 CONFLICT ❌</p>

```
{
	"msg": "email and name already exists"
}
```

<br>

<p>POST 📬</p>

```
{
	"email": "test2@test.com",
	"name": "Test",
	"password": "12345678iI*",
	"test":"test"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"invalid_keys": [
		"test"
	],
	"valid_keys": [
		"email",
		"name",
		"password"
	]
}
```

<br>

<P>POST 📬</P>

```
{
	"email": 3,
	"name": "Test3",
	"password": "12345678iI*"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Expected string in email, but received integer"
}
```

<br>

<p>POST 📬</p>

```
{
	"email": "test3@test.com",
	"name": "Test3",
	"password": "12345678"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "The password must contain at least 8 characters, 1 lowercase letter, 1 uppercase letter, 1 number and 1 special character"
}
```

<br>

<p>POST 📬</p>

```
{
	"email": "test3@test.com",
	"name": "Test3test3Test3test3Test3test3Test3test3Test3test3Test3test3Test3test3Test3test3Test3test3",
	"password": "12345678iI*"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "name accepts a maximum of 80 catacters"
}
```

<br>

<p>GET 📧</p>

```

```

<p>200 OK ✔️</p>

```
[
	{
		"email": "test@test.com",
		"is_adm": false,
		"name": "Test",
		"user_id": 1
	},
	{
		"email": "test222@test.com",
		"is_adm": false,
		"name": "Test2",
		"user_id": 2
	},
	{
		"email": "test3@test.com",
		"is_adm": false,
		"name": "Test3",
		"user_id": 3
	}
]
```

<br>

#### **/users/login**

<br>

<p>POST 📬</p>

```
{
	"email": "test3@test.com",
	"password": "12345678iI*"
}
```

<p>200 OK ✔️</p>

```
{
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4Mjk4NTY3MywianRpIjoiM2Y0NmMwN2EtODFlYi00YTFjLWJiMTctNzE1ZDQ4MzU5YTE4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QzQHRlc3QuY29tIiwibmJmIjoxNjgyOTg1NjczLCJleHAiOjE2ODI5ODY1NzN9.94MHkaLJX48Fqvhnt2a3n6hhhzW0uXcuCd1dnN-rRtw"
}
```

<p>404 NOT FOUND ❌</p>

```
{
	"msg": "User not found"
}
```

<p>401 UNAUTHORIZED ❌</p>

```
{
	"msg": "Unauthorized"
}
```

<br>

<p>POST 📬</p>

```
{
	"email": "test3@test.com",
	"password": "12345678iI*",
	"test": "test"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"invalid_keys": [
		"test"
	],
	"valid_keys": [
		"email",
		"password"
	]
}
```

<br>

#### **users/<<int:user_id>>**

<br>

<p>GET 📧</p>

```

```

<p>200 OK ✔️</p>

```
{
	"email": "test@test.com",
	"is_adm": false,
	"name": "Test",
	"user_id": 1
}
```

<p>404 NOT FOUND ❌</p>

```
{
    "msg": "User not found"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "novo_nome"
}
```

<p>204 NO CONTENT ✔️</p>

```

```

<p>404 NOT FOUND ❌</p>

```
{
	"msg": "User not found"
}
```

<p>401 UNAUTHORIZED ❌</p>

```
{
	"msg": "Unauthorized"
}
```

<br>

<P>PATCH 🔄</P>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "novo_nome",
	"test": "test"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"invalid_keys": [
		"test"
	],
	"valid_keys": [
		"email",
		"name",
		"password",
		"is_adm"
	]
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": 1
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Expected string in name, but received integer"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"password": "1234"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "The password must contain at least 8 characters, 1 lowercase letter, 1 uppercase letter, 1 number and 1 special character"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "novo_nomenovo_nomenovo_nomenovo_nomenovo_nomenovo_nomenovo_nomenovo_nomenovo_nome"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "name accepts a maximum of 80 catacters"
}
```

<br>

#### **/games**

<br>

<p>POST 📬</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley",
	"description": "RPG de fazenda",
	"votes": 0
}
```

<p>200 OK ✔️</p>

```
{
	"creator_id": 4,
	"description": "RPG de fazenda",
	"game_id": 1,
	"name": "Stardew Valley",
	"votes": 0
}
```

<p>409 CONFLICT ❌</p>

```
{
	"msg": "name already exists"
}
```

<br>

<P>POST 📬</P>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": true,
	"description": "RPG de fazenda",
	"votes": 0
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Expected string in name, but received boolean"
}
```

<br>

<p>POST 📬</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "nomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenomenome",
	"description": "blá blá blá",
	"votes": 0
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "name accepts a maximum of 80 catacters"
}
```

<br>

<p>POST 📬</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley 3",
	"description": "RPG de fazenda",
	"votes": 0,
	"test": "test"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"invalid_keys": [
		"test"
	],
	"valid_keys": [
		"name",
		"description",
		"votes"
	]
}
```

<br>

<p>POST 📬</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley 3",
	"description": "RPG de fazenda",
	"votes": 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Number of votes exceeds maximum supported by database"
}
```

<br>

<p>POST 📬</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley 3",
	"description": "RPG de fazenda",
	"votes": -1
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Votes cannot be a negative number"
}
```

<br>

<p>GET 📧</p>

```

```

<p>200 OK ✔️</p>

```
[
	{
		"creator_id": 4,
		"description": "RPG de fazenda",
		"game_id": 1,
		"name": "Stardew Valley",
		"votes": 0
	},
	{
		"creator_id": 4,
		"description": "Continuação do RPG de fazenda",
		"game_id": 2,
		"name": "Stardew Valley 2",
		"votes": 0
	}
]
```

<br>

#### **/games/ordered**

<br>

<p>GET 📧</p>

```

```

<p>200 OK ✔️</p>

```
[
	{
		"creator_id": 4,
		"description": "RPG de fazenda",
		"game_id": 1,
		"name": "Stardew Valley",
		"votes": 6
	},
	{
		"creator_id": 4,
		"description": "RPG de fazenda",
		"game_id": 2,
		"name": "Stardew Valley 2",
		"votes": 3
	},
	{
		"creator_id": 3,
		"description": "RPG de fantasia em um mundo medieval",
		"game_id": 3,
		"name": "Skyrim",
		"votes": 0
	}
]
```

<br>

#### **/games/<<int:game_id>>**

<br>

<p>GET 📧</p>

```

```

<p>200 OK ✔️</p>

```
{
	"creator_id": 4,
	"description": "RPG de fazenda",
	"game_id": 2,
	"name": "Stardew Valley 2",
	"votes": 0
}
```

<p>404 NOT FOUND ❌</p>

```
{
	"msg": "Game not found"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley: O retorno",
	"description": "RPG de fazenda"
}
```

<p>204 NO CONTENT ✔️</p>

```

```

<p>401 UNAUTHORIZED ❌</p>

```
{
	"msg": "Unauthorized"
}
```

<p>409 CONFLICT ❌</p>

```
{
	"msg": "name already exists"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley: A reviravolta",
	"description": "RPG de fazenda",
	"test": "test"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"invalid_keys": [
		"test"
	],
	"valid_keys": [
		"name",
		"description",
		"votes"
	]
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley: A reviravolta",
	"description": 10
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Expected string in description, but received integer"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"name": "Stardew Valley: A reviravoltaStardew Valley: A reviravoltaStardew Valley: A reviravoltaStardew Valley: A reviravoltaStardew Valley: A reviravoltaStardew Valley: A reviravoltaStardew Valley: A reviravoltaStardew Valley: A reviravolta"
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "name accepts a maximum of 80 catacters"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"votes": -1
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Votes cannot be a negative number"
}
```

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```
{
	"votes": 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
}
```

<p>400 BAD REQUEST ❌</p>

```
{
	"msg": "Number of votes exceeds maximum supported by database"
}
```

<br>

<p>DELETE 🔥</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```

```

<p>204 CONTENT ✔️</p>

```

```

<p>404 NOT FOUND ❌</p>

```
{
	"msg": "Game not found"
}
```

<p>401 UNAUTHORIZED ❌</p>

```
{
	"msg": "Unauthorized"
}
```

<br>

#### **/games/<<int:game_id>>/vote**

<br>

<p>PATCH 🔄</p>

HEADER `Authorization: Bearer ea1832e0-2548-400d-97a1-b8cc88fb0475`

```

```

<p>204 NO CONTENT ✔️</p>

```

```

<p>404 NOT FOUND ❌</p>

```
{
	"msg": "Game not found"
}
```

<p>409 CONFLICT ❌</p>

```
{
	"msg": "Current user has already voted for this game"
}
```

---

 <img style="border-radius: 50%;" src="./img/perfil.jpeg" width="100px;" alt=""/>
 <br />
 <sub><b>Iago Vinícius</b></sub>

Feito com ❤️ por Iago Vinícius 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Iago-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/iago-vinicius-souza/)](https://www.linkedin.com/in/iago-vinicius-souza/)
