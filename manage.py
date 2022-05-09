from flask_script import Manager
from flask_migrate import MigrateCommand

from api import app
from api.v1.models import *

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    r = requests.get('http://www.google.com')
    print('test')

if __name__ == '__main__':
    manager.run()


