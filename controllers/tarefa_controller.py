from models import Tarefa
from models import db

class TarefaController:
    
    @staticmethod
    def get_listar_tarefas():
        return Tarefa.query.all()
    
    @staticmethod
    def get_listar_tarefas_id(tarefa_id):
        return Tarefa.query.get(tarefa_id)
    
    @staticmethod
    def post_criar_tarefa(id, titulo, concluida):
        nova_tarefa = Tarefa(id=id, titulo=titulo, concluida=concluida)
        db.session.add(nova_tarefa)
        db.session.commit()
        return nova_tarefa
    
    @staticmethod
    def delete_remover_tarefa(tarefa_id: int):
        tarefa = Tarefa.query.get(tarefa_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
            return True
        return False

    @staticmethod
    def put_atualizar_tarefa(tarefa_id: int, dados: dict):
        tarefa = Tarefa.query.get(tarefa_id)
        if not tarefa:
            return None
        if 'titulo' in dados:
            tarefa.titulo = dados['titulo']
        if 'concluida' in dados:
            tarefa.concluida = dados['concluida']
        db.session.commit()
        return tarefa