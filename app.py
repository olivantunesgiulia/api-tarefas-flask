# Desenvolvi uma API REST com Flask para gerenciamento de tarefas, com operações de CRUD, persistência em JSON, validação de dados e tratamento de erros. A API utiliza identificadores únicos para cada recurso, garantindo operações seguras de atualização e exclusão.

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def gerar_novo_id(tarefas):
    if not tarefas:
        return 1
    return max(t["id"] for t in tarefas) + 1

def buscar_tarefa_por_id(tarefas, id):
    for t in tarefas:
        if t["id"] == id:
            return t
    
    return None

tarefas = carregar_tarefas()

@app.route('/')
def home():
    return "API de tarefas funcionando!"

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    dados = request.get_json()

    if not dados or "nome" not in dados:
        return {"erro": "Campo 'nome' é obrigatório"}, 400
    
    nova_tarefa = {
        "id": gerar_novo_id(tarefas),
        "nome": dados["nome"],
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def concluir_tarefa(id):
    tarefa = buscar_tarefa_por_id(tarefas, id)

    if tarefa:
        tarefa["concluida"] = True
        salvar_tarefas(tarefas)
        return jsonify(tarefas)
    
    return {"erro": "Tarefa não encontrada"}, 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = buscar_tarefa_por_id(tarefas, id)

    if tarefa:
        tarefas.remove(tarefa)
        salvar_tarefas(tarefas)
        return jsonify(tarefas)

    return {"erro": "Tarefa não encontrada"}, 404


if __name__ == '__main__':
    app.run(debug=True)