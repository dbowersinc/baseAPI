from flask_sqlalchemy import SQLAlchemy
import click
from flask import current_app
from flask.cli import with_appcontext

db = SQLAlchemy()


def shutdown_session(exception=None):
    db.session.remove()


def init_db():
    # import all model here
    from .cafes_table import Cafe
    db.create_all()


def drop_all_db():
    # import all model here
    db.drop_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(shutdown_session)
    app.cli.add_command(init_db_command)