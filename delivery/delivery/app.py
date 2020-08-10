from flask import Flask

from delivery.ext import (
    admin,
    auth,
    cli,
    config,
    db,
    hooks,
    migrate,
    site,
    toolbar,
)


def create_app():
    """
        Factory Principal
    """
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)
    # __name__ = nome do módulo
    return app
