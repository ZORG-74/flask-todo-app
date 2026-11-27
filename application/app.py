# -*- coding: utf-8 -*-

import sys
import os

# Добавляем корень проекта в пути поиска
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from controllers import blueprints
from configs import config
from extensions import db


def create_app(config_name=None):
    if config_name is None:
        config_name = 'default'

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # db
    db.init_app(app)

    # blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app
