
def init_app(app):

    @app.before_first_request
    def init_everything():
        print("Estou Iniciando a APP!!! Antes do primeiro request!!!")