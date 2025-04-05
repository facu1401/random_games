from flask import Flask
import random
app = Flask(__name__)

@app.route("/lanzamiento")
def lanzamiento():
    resultado = "Cara" if random.choice([True, False]) else "Cruz"
    return f'<h1>Lanzamiento de moneda</h1><p>El resultado es: {resultado}</p>'

@app.route("/")
def index():
    return '<h1>Lanzamiento de moneda</h1><a href="/lanzamiento">¡Lanzar la moneda!</a>'

app.run(debug=True)
