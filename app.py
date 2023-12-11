
from flask import Flask
from flask-wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Devops & Cloud LAB"