from domain.models.user import Usuario
from domain.repositories import UsuarioRepository
from application.dtos import UsuarioDTO

class UserService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def obtener_usuario(self, usuario_id: str) -> Usuario:
        return self.repository.obtener_usuario(usuario_id)

    def crear_usuario(self, usuario_dto: UsuarioDTO) -> Usuario:
        nuevo_usuario = Usuario(id=None, nombre=usuario_dto.nombre, email=usuario_dto.email)
        return self.repository.crear_usuario(nuevo_usuario)
