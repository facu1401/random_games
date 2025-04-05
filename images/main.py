from flask import Flask
import random

app = Flask(__name__)

# Lista de imágenes
IMAGENES = [
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/030.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/009.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/006.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/001.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/025.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/004.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/007.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/012.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/013.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/014.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/015.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/016.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/017.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/018.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/019.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/020.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/021.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/022.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/023.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/024.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/026.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/027.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/028.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/029.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/031.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/032.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/033.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/034.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/035.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/036.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/037.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/038.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/039.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/040.png",
    "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/041.png",
]

@app.route("/mostrar_imagen")
def mostrar_imagen():
    # Elegir una imagen aleatoria
    imagen = random.choice(IMAGENES)
    return '''
        <h1>Imagen Aleatoria</h1>
        <img src="{}" alt="Imagen Aleatoria">
        <br><br>
        <a href="/">Volver</a>
    '''.format(imagen)

@app.route("/")
def index():
    return '''
        <h1>¡Ver una Imagen Aleatoria!</h1>
        <a href="/mostrar_imagen">Clic aquí</a>
    '''
app.run(debug=True)
