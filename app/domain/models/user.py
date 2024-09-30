from mongoengine import Document

class Usuario(Document):
    def __init__(self, id: str, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

    def cambiar_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre