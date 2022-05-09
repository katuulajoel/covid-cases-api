import requests
import json
from flask_script import Manager
from flask_migrate import MigrateCommand

from api import app
from api.v1.models import *

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    r = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
    f = open("cases.json", "x")
    f.write(r.text)
    f.close()

@manager.command
def seed_database():
    with open('cases.json') as cases_file:
        data = json.load(cases_file)

    my_list = []
    for key in data:
        country_case = data[key]['All']
        dict = {
            'country': country_case.get('country'),
            'city': country_case.get('city'),
            'continent': country_case.get('continent'),
            'confirmed': country_case.get('confirmed'),
            'deaths': country_case.get('deaths'),
            'population': country_case.get('population'),
            'life_expectancy': country_case.get('life_expectancy'),
            'updated_at': country_case.get('updated')
        }
        my_list.append(dict)

    # Serializing json 
    json_object = json.dumps({"model": "models.CaseModel", "data": my_list}, indent = 4)

    with open("cases_seed.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    manager.run()


