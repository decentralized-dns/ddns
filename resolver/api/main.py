from fastapi import FastAPI
from api.routes.ping import router

def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app

app = get_application()
