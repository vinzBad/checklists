# checklists
prototype webapp to create manage checklist templates

## getting started
* clone this repo
* create virtualenv: python -m virtualenv venv
* activate venv: source venv/bin/activate
* install requirements: pip install -r requirements.txt
* setup db: FLASK_APP=app flask init-db
* fill db with testdata: FLASK_APP=app flask db-testmodel
* start development server: FLASK_APP=app;FLASK_ENV=development flask run
