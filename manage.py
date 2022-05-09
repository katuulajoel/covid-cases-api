from flask_script import Manager
from flask_migrate import MigrateCommand

from api import create_app
from api.v1.models import *

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
     print('test')

if __name__ == '__main__':
    manager.run()


