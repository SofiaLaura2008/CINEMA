import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializando o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.secret_key = '17052008'
    project_dir = os.path.dirname(os.path.abspath(__file__))
    cinema_file = "sqlite:///{}".format(os.path.join(project_dir, "Cinema.db"))
    
    app.config["SQLALCHEMY_DATABASE_URI"] = cinema_file
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from cinema.models import Usuario
        return Usuario.query.get(int(user_id))
        
    db.init_app(app)
    
    return app
