from ddnsapi.routes.ping import router
from fastapi import FastAPI


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = get_application()
