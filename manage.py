# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from application import create_app
from application.extensions import db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('runserver', Server(host='127.0.0.1', port=7345))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
