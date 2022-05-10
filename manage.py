import os

import requests
import json
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder

from api import app, db
from api.v1.models.cases import CaseModel

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def seed_database():

    data = None

    if os.environ.get("FLASK_ENV") == "production":
        r = requests.get('https://covid-api.mmediagroup.fr/v1/cases')
        data = json.loads(r.text)
    else:
        with open('static.sample_cases.json') as cases_file:
            data = json.load(cases_file)

    my_list = []
    for key in data:
        country_case = data[key]['All']
        if country_case.get('country'):
            dict = {
                'country': country_case.get('country'),
                'city': country_case.get('capital_city', ''),
                'continent': country_case.get('continent'),
                'confirmed': country_case.get('confirmed'),
                'deaths': country_case.get('deaths'),
                'population': country_case.get('population'),
                'life_expectancy': country_case.get('life_expectancy'),
                'updated_at': country_case.get('updated', None)
            }
            my_list.append(dict)

    # Serializing json
    json_object = json.dumps(
        {"model": "api.v1.models.cases.CaseModel", "data": my_list}, indent=4)

    with open("cases_seed.json", "w") as outfile:
        outfile.write(json_object)


@manager.command
def run_seeder():
    # load entities
    entities = load_entities_from_json('cases_seed.json')

    # Initializing Seeder
    seeder = Seeder(db.session)

    # Seeding
    seeder.seed(entities)

    #import pdb; pdb.set_trace()

    # Committing
    seeder.session.commit()


if __name__ == '__main__':
    manager.run()
