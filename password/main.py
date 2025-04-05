from flask import Flask
import random

app = Flask(__name__)

# Los caracteres para hacer la contraseña
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Función para crear la contraseña
def generar_contraseña():
    contraseña = ""
    for i in range(12):  # Hace la contraseña de 12 letras
        contraseña += random.choice(caracteres)
    return contraseña

@app.route("/generar_contraseña")
def mostrar_contraseña():
    contraseña = generar_contraseña()
    return f'''
        <h1>Contraseña Generada</h1>
        <p>Tu nueva contraseña es: {contraseña}</p>
        <a href="/">Volver</a>
    '''

@app.route("/")
def index():
    return '''
        <h1>Generador de Contraseñas</h1>
        <a href="/generar_contraseña">¡Genera una contraseña nueva!</a>
    '''

app.run(debug=True)
