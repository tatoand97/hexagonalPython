# infrastructure/user_repository.py
from domain.repositories.UsuarioRepository import UsuarioRepository
from domain.models.user import Usuario

# Implementación del repositorio
class UsuarioRepositoryImpl(UsuarioRepository):
    def obtener_usuario(self, usuario_id: str) -> Usuario:
        usuario_mongo = Usuario.objects().first()
        if usuario_mongo:
            return Usuario(id=str(usuario_mongo.id), nombre=usuario_mongo.nombre, email=usuario_mongo.email)
        return None

    def crear_usuario(self, usuario: Usuario) -> Usuario:
        usuario_mongo = Usuario(nombre=usuario.nombre, email=usuario.email)
        usuario_mongo.save()
        return Usuario(id=str(usuario_mongo.id), nombre=usuario_mongo.nombre, email=usuario_mongo.email)
