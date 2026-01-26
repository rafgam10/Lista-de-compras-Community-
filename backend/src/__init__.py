from flask import Flask
from src.settings.extersions import db, migrate

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    else:
        app.config.from_object("src.settings.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    # Importação dos Models (necessário pro SQLAlchemy registrar)
    from src.models.produto_model import Produto
    from src.models.user_model import User

    # Rotas
    from src.routes.produto_routes import produto_bp
    app.register_blueprint(produto_bp)

    return app
