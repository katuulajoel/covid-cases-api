# WeConnect-App

Covid 19 create a platform to understand the impact of the pandemic on the world.

## Features

1. Users can view all covid 19 cases as provided by https://github.com/M-Media-Group/Covid-19-API
2. Users can view cases from a specfic continent
3. Users can view cases from a specific country
4. Users can see the totals (confirmed cases and deaths) of the pandemic on how it has affected the world.

| EndPoint                                             | Functionality                                    |
| ---------------------------------------------------- | ------------------------------------------------ |
| [GET   /cases_api/cases](https://)                    | Get all covid 19 cases                           |
| [GET   /cases_api/country/{country}](https://)                       | Get cases for a specific country                                  |
| [GET   /cases_api/country/{continent}](https://)                      | Get cases from a continent                                  |
| [GET   /cases_api/{case_id}](https://)              | Get cases by unquie ID                                   |
| [GET   /cases_api/summary](https://)                       | Summarise case totals across continents                              |
| [GET    /cases_api/countries_continent_list](https://)         | Get contries and continents in the database                       |

## Tested with

* [Python 3.9](https://www.python.org/downloads)
* [PostgreSQL 11](https://www.postgresql.org/download/)

## Requirements

* Install [Python](https://www.python.org/downloads/).
* Install [PostgreSQL](https://www.postgresql.org/download/).
* Run `pip install virtualenv` on command prompt.
* Run `pip install virtualenvwrapper-win` for Windows.
* Run `set WORKON_HOME=%USERPROFILES%\Envs` for Windows.

## Setup

* Run `git clone` this repository and `cd` into the project root.
* Run `mkvirtualenv venv` for Windows or `python3 -m venv ../wc-venv` for Unix/Mac.
* Run `workon venv` for Windows or `source ../wc-venv/bin/activate` for Unix/Mac.
* Run `pip install -r requirements.txt`.
* Run `createdb <weconnect_db>` and `createdb <test_weconnect_db>` on the psql bash terminal.
* Run `touch .env` to create a file for storing environment variables. Add the following lines (use `set` for Windows instead of `export`, used here for Unix/Mac) to it:

```env
export DATABASE_URL=postgresql://<db_user>:<password>@localhost/<db_name>
export SECRET_KEY=<some_secret_value>
export FLASK_ENV=development
export FLASK_APP=manage.py
```

* Run `source .env` to activate the environment variables on Unix/Mac.
* Run `env` to verify the above.
* Run the migrations:
  * `python manage.py db init` to create a migration repository.
  * `python manage.py db migrate` to update the migration script.
  * `python manage.py db upgrade` to apply the migration to the database.
  * `python manage.py seed_database ` to pull in data from the [covid 19 Api](https://github.com/M-Media-Group/Covid-19-API)
  * `python manage.py run_seeder` to migrate data pulled in from previous step into the database.
* Run `python manage.py runserver` or `python3 run.py` to run on the default ip and port.
* View the app on `http://127.0.0.1:5000/`.

## Use endpoints

* View the api on `http://127.0.0.1:5000/cases_api/`
* Test it's usage with postman

## Use api documentation

* View the api on [Heroku](https://)
* View the api on `http://127.0.0.1:5000/cases_api/docs`
