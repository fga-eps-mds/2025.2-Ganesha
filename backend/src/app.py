# backend/src/app.py
from flask import Flask, jsonify
from dotenv import load_dotenv
import os
# Adicionando o SQLAlchemy e o Migrate
from flask_migrate import Migrate
from backend.src.extensions import db
from backend.src.models.usuario import Usuario  # Importa os modelos para que o Alembic os reconheça

# 1. Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# 2. Configurações Básicas do Aplicativo
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Inicializa o objeto DB e o Migrate
db.init_app(app)
migrate = Migrate(app, db)

# 4. Importar Modelos (Obrigatorio para que o Alembic os encontre)
# IMPORTANTE: Você precisa garantir que TODOS os seus modelos (Ex: User, Product)
# sejam importados aqui ou em algum lugar que o app.py carrega.
#
# Exemplo (Descomente quando criar o arquivo backend/src/model/user.py):
# from src.model.user import User

# 5. Importar e Registrar as Camadas/Rotas aqui
# from .controller.user_controller import user_bp
# app.register_blueprint(user_bp, url_prefix='/api/users')


@app.route('/', methods=['GET'])
def status():
    """Rota básica para verificar se o servidor está ativo."""
    return jsonify({"status": "Servidor Ganesha Backend OK", "environment": os.getenv('FLASK_ENV')}), 200

if __name__ == '__main__':
    # Bloco não é mais necessário aqui, pois o Flask-Migrate
    # já cuida da criação e atualização de tabelas.
    app.run(
        debug=os.getenv('FLASK_ENV') == 'development',
        port=os.getenv('PORT')
    )