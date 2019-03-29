# coding:utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from frf_demo import create_app, db


app = create_app('develope')

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

