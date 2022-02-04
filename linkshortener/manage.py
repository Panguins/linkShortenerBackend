import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from linkshortener.extensions import db
    from linkshortener.models import User

    click.echo("create user")
    user = User(username="panguins", email="panguins@gmail.com", password="1111", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
