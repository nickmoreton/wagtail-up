import subprocess
from shlex import quote

from invoke import run, task


@task
def up(c, detached=False):
    """Start the docker containers | -d: detached mode"""

    if not detached:
        run("docker-compose up")
    else:
        run("docker-compose up -d")


@task
def down(c, volume=False):
    """Stop the docker containers | -v: volume mode"""
    if not volume:
        run("docker-compose down")
    else:
        run("docker-compose down -v")


@task
def exec(c, command="bash", app="app"):
    """Execute a command in the docker containers | app: app name | command: command to execute"""
    subprocess.run(["docker-compose", "exec", app, command])


@task
def test(c, command="python manage.py test", app="app"):
    """Run the tests"""
    run(f"docker-compose exec -T {quote(app)} bash -c {quote(command)}")
