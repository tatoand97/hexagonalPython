from mongoengine import connect, disconnect

def iniciar_bd():
    # Iniciar la conexión con MongoDB
    connect(db="mi_base_de_datos", host="localhost", port=27017)

def cerrar_bd():
    # Cerrar la conexión con MongoDB
    disconnect()
