from flask import Flask

from src.settings.config import Config
from src.settings.extersions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    return app
