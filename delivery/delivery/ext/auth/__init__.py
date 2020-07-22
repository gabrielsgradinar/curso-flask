from delivery.ext.auth import models
from delivery.ext.auth.commands import list_users, add_user

def init_app(app):
    """TODO: Inicializar Flask Simple Login + JWT"""
    app.cli.command()(list_users)
    app.cli.command()(add_user)

