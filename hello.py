#1.- pipenv install flask -> py -m pipenv install flask, python -m pipenv install flask
#2.- pipenv shell -> py -m pipenv shell, python -m pipenv shell
#3.- python nombre_archivo.py -> python3 nombre_archivo.py, py nombre_archivo.py

from flask import Flask, render_template #Importando Flask para permitirnos crear una aplicación web

app = Flask(__name__) #Creando una nueva instancia de la clase Flask llamada "app"

@app.route('/') #El decorador '@' asocia esa ruta con la función que vamos tener inmediatamente, la ruta es la URL
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/hola/<nombre>') #Para mi ruta /hola/_____ cualquier cosa después de /hola/ se va a pasar como variable nombre
def hola(nombre):
    return f'<h1>Hola {nombre}, cómo estás?</h1>'

@app.route('/hello/<name>/<int:numero>')
def hello(name, numero):
    #En lugar de devolver una cadena, devolvemos el resultado de un render_template
    return render_template('hola.html', nombre=name, cantidad=numero)



if __name__=="__main__": #Asegura que el archivo se está ejecutando directamente y no desde un módulo diferente
    app.run(debug=True) #Ejecuta la aplicación