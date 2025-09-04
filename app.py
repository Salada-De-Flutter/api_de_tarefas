from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from routes.tarefa_routes import tarefas_bp
from controllers.tarefa_controller import TarefaController

def criar_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    
    app.register_blueprint(tarefas_bp)
    
    return app
    
if __name__ == '__main__':
    app = criar_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
