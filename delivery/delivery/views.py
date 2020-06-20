"""Extensão Flask"""

def init_app(app):
    """
        Factory de Inicialização de extensões
    """
    @app.route("/")
    def index():
        return "<h1>Hello World</h1>"

    @app.route("/sobre")
    def sobre():
        return "<h1>Melhor site de delivery !!!</h1>"