# Wagtail UP

A quick start develoment Wagtail project template with a frontend framework.

Backend

- [Wagtail CMS](https://wagtail.org)
- Docker
- Postgres

Frontend

- [Codyhouse Framework](https://codyhouse.co)
- Gulp and NPM

Github

- Basic github actions

## Installation

Clone this repository to your local machine.

```bash
git clone https://github.com/nickmoreton/wagtail-up
```

In github you can use the repo as a template for your project.

### Python environment

Pipenv:

```bash
pipenv install
pipenv shell

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0:8000
```

Virtualenv:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0:8000
```

Docker:

```bash
docker-compose up

# in a new terminal
docker-compose exec app bash
python manage.py migrate
python manage.py createsuperuser
```

The site will be avaiable at `http://localhost:8000`

### Node environment

NPM:

```bash
npm install
npm start
```

The site will be available at `http://localhost:3000`

### Developer tools

- Black
- Flake8
- Isort
- Pre-commit

To install the tools:

```bash
pre-commit install
```

Pre-commit will run when you commit changes.

## TODO

- Basic wagtail apps
- Inital wagtail/django tests
