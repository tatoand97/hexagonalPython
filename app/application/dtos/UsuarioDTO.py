from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    id: str
    nombre: str
    email: str

    # Configurar el modelo para soportar la conversión desde ORM
    model_config = {
        "from_attributes": True  # Reemplaza orm_mode con from_attributes
    }
