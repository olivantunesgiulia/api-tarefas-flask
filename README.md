# 📌 API de Gerenciamento de Tarefas

## Descrição

API REST desenvolvida com Flask para gerenciamento de tarefas, permitindo criar, listar, atualizar e remover tarefas.

O projeto inclui:

* Operações completas de CRUD
* Persistência de dados em arquivo JSON
* Uso de identificadores únicos (ID)
* Validação de dados e tratamento de erros

---

## Tecnologias utilizadas

* Python
* Flask
* JSON

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Instale as dependências:

```bash
pip install flask
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000/tarefas
```

---

## 🔗 Endpoints da API

### Listar todas as tarefas

GET /tarefas

---

### Criar nova tarefa

POST /tarefas

Exemplo de requisição:

```json
{
  "nome": "Estudar Flask"
}
```

Resposta:

```json
{
  "id": 1,
  "nome": "Estudar Flask",
  "concluida": false
}
```

---

### Marcar tarefa como concluída

PUT /tarefas/{id}

---

### Remover tarefa

DELETE /tarefas/{id}

---

## Estrutura do projeto

```bash
app.py
tarefas.json
```

---

## Aprendizados

* Criação de APIs REST com Flask
* Manipulação de dados em JSON
* Implementação de operações CRUD
* Uso de identificadores únicos (ID)
* Tratamento de erros e validação de entrada

---

## Melhorias futuras

* Integração com banco de dados (SQLite)
* Autenticação de usuários
* Organização em múltiplos arquivos (estrutura modular)

---

## Autora
Giulia Antunes de Oliveira
