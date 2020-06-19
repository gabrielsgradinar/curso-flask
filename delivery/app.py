from flask import Flask

app = Flask(__name__)
# __name__ = nome do módulo

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/sobre")
def sobre():
    return "<h1>Melhor site de delivery !!!</h1>"
