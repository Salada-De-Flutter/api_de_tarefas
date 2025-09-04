from flask import Blueprint, request, jsonify
from controllers.tarefa_controller import TarefaController

tarefas_bp = Blueprint('tarefas', __name__)

# Essa Rota Funciona
@tarefas_bp.route('/api/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefaController.get_listar_tarefas()])

# Essa Rota Funciona
@tarefas_bp.route('/api/tarefas/<int:tarefa_id>', methods=['GET'])
def get_tarefa_id(tarefa_id):
    tarefa = TarefaController.get_listar_tarefas_id(tarefa_id)
    if tarefa:
        return jsonify(tarefa.to_dict())
    return jsonify({"error": "Tarefa não encontrada"}), 404

# Essa tem um probleminha no True e False
@tarefas_bp.route('/api/criar_tarefas', methods=['POST'])
def post_criar_tarefa():
    dados = request.get_json()
    id = dados.get('id')
    titulo = dados.get('titulo')
    concluida = dados.get('concluida', False)
    nova_tarefa = TarefaController.post_criar_tarefa(id, titulo, concluida)
    return jsonify(nova_tarefa.to_dict()), 201

# Rota para remover tarefa - Ta funcionando
@tarefas_bp.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_remover_tarefa(tarefa_id):
    sucesso = TarefaController.delete_remover_tarefa(tarefa_id)
    if sucesso:
        return jsonify({'mensagem': 'Tarefa removida com sucesso!'}), 200
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# Rota para atualizar tarefa - Ta duncionando hehehehehhe
@tarefas_bp.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def put_atualizar_tarefa(tarefa_id):
    dados = request.get_json()
    tarefa = TarefaController.put_atualizar_tarefa(tarefa_id, dados)
    if tarefa:
        return jsonify(tarefa.to_dict()), 200
    return jsonify({'erro': 'Tarefa não encontrada'}), 404