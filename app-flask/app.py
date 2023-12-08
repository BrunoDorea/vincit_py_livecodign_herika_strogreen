from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<h1>Minha API com Flask</h1><p>PYTHON: Domando Dados com Estilo - Uma abordagem descontraída para a introdução a dados</p>"

@app.get("/login")
def login_get():
    return "<h1>Login</h1><p>Mostrou login</p>"

@app.post("/login")
def login_post():
    data = request.json
    return {
        "name": data['name'],
        "idade": data['idade'],
        "cidade": data['cidade']
    }

if __name__ == '__main__':
    app.run()
