# Development environments

## Virtual Environments (backend)

### Pipenv

```bash
pipenv install
pipenv shell

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0:8000
```

### Virtualenv

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0:8000
```

## Docker

Fabric (https://www.fabfile.org/) is available to run docker commands. View available commands with:

```bash
fab -l
```

Or run the docker containers with:

```bash
docker-compose up

# in a new terminal
docker-compose exec app bash
python manage.py migrate
python manage.py createsuperuser
```

The site will be avaiable at `http://localhost:8000`

## Node environment (frontend)

### NPM

```bash
npm install
npm start
```

The site will be available at `http://localhost:3000`

## Developer tools

### Pre-commit

Install with:

```bash
pre-commit install
```

Pre-commit will run when you commit changes and will run checks with:

- Black
- Flake8
- Isort

Uninstall with:

```bash
pre-commit uninstall
```
