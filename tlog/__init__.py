import os

from flask import Flask
from flask_bootstrap import Bootstrap


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tlog.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    @app.route('/index')
    def index():
        return 'Hello, world'
    
    from . import db, auth

    db.init_app(app)
    app.register_blueprint(auth.bp)

    return app
