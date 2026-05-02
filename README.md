# 📌 Sistema de Gerenciamento de Tarefas

## Descrição

Aplicação completa de gerenciamento de tarefas composta por:

* **Backend (API REST)** desenvolvido com Flask
* **Frontend** em HTML, CSS e JavaScript

O sistema permite criar, listar, concluir e remover tarefas, com persistência de dados em JSON e uso de identificadores únicos (ID).

---

## Tecnologias utilizadas

### Backend:

* Python
* Flask
* JSON

### Frontend:

* HTML
* CSS
* JavaScript

---

## Estrutura do projeto

```
seu-projeto/
│
├── api/
│   ├── app.py
│   └── tarefas.json (ignorado pelo Git)
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore
```

---

## Como executar o projeto

### Backend (API)

1. Acesse a pasta:

```
cd api
```

2. Instale as dependências:

```
pip install flask
```

3. Execute a API:

```
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

### Frontend

1. Acesse a pasta:

```
cd frontend
```

2. Abra o arquivo:

```
index.html
```

Ou utilize uma extensão como Live Server no VS Code.

---

## 🔗 Endpoints da API

### Listar tarefas

GET /tarefas

---

### Criar tarefa

POST /tarefas

Exemplo:

```json
{
  "nome": "Estudar Flask"
}
```

---

### Marcar como concluída

PUT /tarefas/{id}

---

### Remover tarefa

DELETE /tarefas/{id}

---

## Aprendizados

* Desenvolvimento de API REST com Flask
* Integração entre frontend e backend
* Manipulação de dados em JSON
* Estruturação de projetos em camadas
* Boas práticas com Git e GitHub

---

## 📌 Melhorias futuras

* Integração com banco de dados (SQLite)
* Sistema de autenticação de usuários
* Interface mais interativa

---

## Autora

Giulia Antunes de Oliveira
