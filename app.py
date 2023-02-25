#Importamos las librerias utilizadas para el desarrollo de la prueba.

from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore
from base import user

# Firebase_admin, nos permite administrar los recursos de conexion
# y acceder o enviar los datos a nuestra base.

# Ahora vamos inicializar Firebase, pasando como parametro la clave privada generada en la plataforma firebase.
# Es importnte que en esta parte del codigo vayamos a firebase y creemos el proyecto y luego descarguemos la clave.
# En esta caso seria ('prueba-backend-neero-firebase-adminsdk-3mx7y-7079acfd5b.json').

credencial = credentials.Certificate('prueba-backend-neero-firebase-adminsdk-3mx7y-7079acfd5b.json')
firebase_admin.initialize_app(credencial)
# Crear un token personalizado para el usuario con UID "user123"
custom_token = auth.create_custom_token("VrY8rRQTaLe83TP6x52OwbXCaHZ2")

# Iniciamos la aplicación Flask.
app = Flask(__name__)

# Realizamos la conexión a la base de datos de Firebase.
db = firestore.client()
# Obtenemos todos los datos de la colecciónes creadas previamenten en la plataforma
Productos = db.collection('Productos')
Establecimientos = db.collection('Establecimientos')
User = db.collection('User')
Catalogos = db.collection('Catalogos')




"""-----CONSULTA E INGRESO DE PRODUCTOS-----"""

# Esta ruta permitira obtener los productos registrados en la base de datos.
@app.route('/productos', methods=['GET'])
def obtener_productos():
    #Accedemos los datos de la base.
    product = Productos.get()
    #Creamos una lista para iterar la cantida de productos encontrados en base.
    lista_productos = []
    #Realizamos el recorrido de los datos obtenidos de la conexion.
    for producto in product:
        #Y los agregamos a la lista.
        lista_productos.append(producto.to_dict())
    # Aqui creamos una condicion de salida.
    if(len(lista_productos)>0):
        # Si hay productos en la base, devolvemos los productos en formato JSON.
        return jsonify(lista_productos)
    # De lo contrario un mensaje.
    return "*** Upps aun no hay datos cargados :("

# Esta es la ruta para agregar un nuevo producto.
@app.route('/agregarproducto', methods=['POST'])
def agregar_producto():
    # Creamos el modelo del producto a ingresar.
    nuevo_producto = {
        "nombre":request.json["nombre"],
        "precio":request.json["precio"],
        "tipo":request.json["tipo"]
    }
    # Agregar el nuevo producto a la colección 'Productos' previamente creada en la plataforma.
    Productos.add(nuevo_producto)
    # Para mostrar todos los producto ingresados, accedemos a los datos de la base.
    product = Productos.get()
    #Creamos una lista para iterar la cantida de productos encontrados en base.
    lista_productos = []
    #Realizamos el recorrido de los datos obtenidos de la conexion.
    for producto in product:
        #Y los agregamos a la lista.
        lista_productos.append(producto.to_dict())
    # Devolvemos los productos en formato JSON.
    return jsonify(lista_productos)




"""-----CONSULTA E INGRESO DE ESTABLECIMIENTOS-----"""

# Esta ruta permitira obtener los establecimientos registrados en la base de datos.
@app.route('/establecimientos', methods=['GET'])
def obtener_establecimientos():
    #Accedemos los datos de la base.
    Establecimiento = Establecimientos.get()
    #Creamos una lista para iterar la cantida de establecimientos encontrados en base.
    lista_de_Establecimientos = []
    #Realizamos el recorrido de los datos obtenidos de la conexion.
    for Locales in Establecimiento:
        #Y los agregamos a la lista.
        lista_de_Establecimientos.append(Locales.to_dict())
    # Aqui creamos una condicion de salida.
    if(len(lista_de_Establecimientos)>0):
        # Si hay establecimientos en la base, devolvemos los establecimientos en formato JSON.
        return jsonify(lista_de_Establecimientos)
    # De lo contrario un mensaje.
    return "*** Upps aun no hay datos cargados :("

# Ruta para la creacion de establecimiento
@app.route("/agregarestablecimiento", methods = ["POST"])
def agregar_establecimiento():
    # Creamos el modelo del establecimiento a ingresar.
    nuevo_establecimiento = {
        "nombre":request.json["nombre"],
        "direccion":request.json["direccion"],
        "tipo_de_establecimiento":request.json["tipo_de_establecimiento"]
    }
    # Agregar el nuevo establecimiento a la colección 'Establecimiento' previamente creada en la plataforma.
    Establecimientos.add(nuevo_establecimiento)
    # Para mostrar todos los establecimientos ingresados, accedemos los datos de la base.
    Establecimiento = Establecimientos.get()
    #Creamos una lista para iterar la cantida de establecimientos encontrados en base.
    lista_de_Establecimientos = []
    #Realizamos el recorrido de los datos obtenidos de la conexion.
    for Locales in Establecimiento:
        #Y los agregamos a la lista.
        lista_de_Establecimientos.append(Locales.to_dict())
    # Devolvemos los establecimientos en formato JSON.
    return jsonify(lista_de_Establecimientos)




"""-----CREACION DE CATALOGO-----"""

# Ruta para la creacion de catalogo
@app.route("/agregarcatalogo", methods = ["POST"])
def agregar_agregarcatalogo():
    # Creamos el modelo del catalogo a ingresar.
    nuevo_catalogo = {
        "nombre":request.json["nombre"],
        "tipologia":request.json["tipologia"]
    }
    # Agregar el nuevo catalogo a la colección 'Catalogos' previamente creada en la plataforma.
    Catalogos.add(nuevo_catalogo)
    # Para mostrar todos los catalogos ingresados, accedemos los datos de la base.
    Catalogo = Catalogos.get()
    #Creamos una lista para iterar la cantida de catalogos encontrados en base.
    lista_de_catalogos = []
    #Realizamos el recorrido de los datos obtenidos de la conexion.
    for i in Catalogo:
        #Y los agregamos a la lista.
        lista_de_catalogos.append(i.to_dict())
    # Devolvemos los catalogos en formato JSON.
    return jsonify(lista_de_catalogos)


"""-----INGRESO DE USUARIO-----"""

#Ruta para ingresar al sistema con autenticacion de usuario y contraseña
@app.route("/login/",methods =["POST"])
def login():
    #Variable que almacena los datos JSON enviados desde el formulario html
    consulta = {
        #Requisitos de autenticacion nombre y contraseña
        "name": request.json["name"],
        "password": request.json["password"]
    }
    #Recorido de la base para leer datos
    for u in user:
        #Lista que contendra los datos obtenidos a tratar
        buscarU = []
        #Condicional de validacion
        if u["name"] == consulta["name"] and u["password"] == consulta["password"]:
            #Agregamos el usuario referenciado a la lista
            buscarU.append(u)
     #Validamos que la lista contenga datos cargados       
    if(len(buscarU)>0):
        #Retornamos el ingreso exitoso
        return jsonify({"WELCOME":buscarU[0]["name"]})
    #Caso nulo de la validacion
    return jsonify({"ERROR":"USER INVALID"})


if __name__ == '__main__':
    app.run(debug=True)
