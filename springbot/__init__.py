from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    ma.init_app(app)


def register_blueprints(app):
    from springbot.api import bp as api_bp
    app.register_blueprint(api_bp)
