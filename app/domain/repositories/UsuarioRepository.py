from abc import ABC, abstractmethod

class UsuarioRepository(ABC):
    @abstractmethod
    def obtener_usuario(self, usuario_id: str):
        pass

    @abstractmethod
    def crear_usuario(self, usuario):
        pass
