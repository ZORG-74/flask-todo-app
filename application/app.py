# -*- coding: utf-8 -*-

import sys
import os

# Добавляем в пути папку, где лежит сам этот файл (то есть папку application)
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

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
