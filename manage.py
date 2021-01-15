# -*- coding: utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app.factory import create_app
from app.utils.core import db

app = create_app(config_name="DEVELOPMENT")
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

# Run local server
manager.add_command("runserver", Server(host="127.0.0.1", port=5000))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run(default_command="runserver")
