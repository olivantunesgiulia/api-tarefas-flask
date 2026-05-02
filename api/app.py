# Desenvolvi uma API REST com Flask para gerenciamento de tarefas, com operações de CRUD, persistência em JSON, validação de dados e tratamento de erros. A API utiliza identificadores únicos para cada recurso, garantindo operações seguras de atualização e exclusão.

from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import os

CAMINHO = os.path.join(os.path.dirname(__file__), 'tarefas.json')

app = Flask(__name__)
CORS(app)

def carregar_tarefas():
    try:
        with open(CAMINHO, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_tarefas(tarefas):
    with open(CAMINHO, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def gerar_novo_id(tarefas):
    if not tarefas:
        return 1
    return max(t["id"] for t in tarefas) + 1

def buscar_tarefa_por_id(tarefas, id_tarefa):
    for t in tarefas:
        if t["id"] == id_tarefa:
            return t
    return None

@app.route('/')
def home():
    return "API de tarefas funcionando!"

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = carregar_tarefas()
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    tarefas = carregar_tarefas()
    dados = request.get_json()

    if not dados or "nome" not in dados or not dados["nome"].strip():
        return {"erro": "Campo 'nome' é obrigatório"}, 400
    
    nova_tarefa = {
        "id": gerar_novo_id(tarefas),
        "nome": dados["nome"],
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id_tarefa>', methods=['PUT'])
def concluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:
        tarefa["concluida"] = True
        salvar_tarefas(tarefas)
        return jsonify(tarefa), 200
    
    return {"erro": "Tarefa não encontrada"}, 404

@app.route('/tarefas/<int:id_tarefa>', methods=['DELETE'])
def deletar_tarefa(id_tarefa):
    tarefas = carregar_tarefas()

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:
        tarefas.remove(tarefa)
        salvar_tarefas(tarefas)
        return jsonify(tarefa), 200

    return {"erro": "Tarefa não encontrada"}, 404

if __name__ == '__main__':
    app.run(debug=True)