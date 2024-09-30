# presentation/controllers/user_controller.py
from fastapi import APIRouter, Depends
from application.dtos.UsuarioDTO import UsuarioDTO
from infrastructure.user_repository import UsuarioRepositoryImpl
from application.services.user_service import UserService

router = APIRouter()

# Proporcionar el servicio de usuario con el repositorio concreto
def obtener_servicio_usuario():
    repo = UsuarioRepositoryImpl()
    return UserService(repo)

@router.get("/usuarios/{usuario_id}", response_model=UsuarioDTO)
def obtener_usuario(usuario_id: str, servicio: UserService = Depends(obtener_servicio_usuario)):
    usuario = servicio.obtener_usuario(usuario_id)
    # Usar model_validate en lugar de from_orm
    return UsuarioDTO.model_validate(usuario)

@router.post("/usuarios/", response_model=UsuarioDTO)
def crear_usuario(usuario: UsuarioDTO, servicio: UserService = Depends(obtener_servicio_usuario)):
    nuevo_usuario = servicio.crear_usuario(usuario)
    # Usar model_validate en lugar de from_orm
    return UsuarioDTO.model_validate(nuevo_usuario)
