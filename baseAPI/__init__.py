import os
from flask import Flask


def create_app(test_config=None):

    app = Flask('baseAPI', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///../cafes.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_SECRET_KEY='dev',
        API_KEY='79ttAQIBG89Gk2VEf4hrGQ',
    )

    if test_config is None:
        # load the instance config if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import cafes_api
    app.register_blueprint(cafes_api.bp)

    return app