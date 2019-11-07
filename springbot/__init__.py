from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_api(app)
    return app


def initialize_extensions(app):
    db.init_app(app)


def register_api(app):
    from springbot.resources import api
    api.init_app(app)