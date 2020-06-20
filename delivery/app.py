import views
from flask import Flask

def create_app():
    """
        Factory Principal
    """
    app = Flask(__name__)
    views.init_app(app)
    # __name__ = nome do módulo
    return app