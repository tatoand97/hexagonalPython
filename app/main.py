from fastapi import FastAPI
from contextlib import asynccontextmanager
from presentation.controllers import user_controller
from infrastructure.database import iniciar_bd, cerrar_bd

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Evento de inicio de la aplicación (inicio de la conexión)
    iniciar_bd()
    yield
    # Evento de cierre de la aplicación (cierre de la conexión)
    cerrar_bd()

# Crear la aplicación FastAPI con el manejador de ciclo de vida
app = FastAPI(lifespan=lifespan)

# Registrar las rutas
app.include_router(user_controller.router)
