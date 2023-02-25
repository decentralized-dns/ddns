from ddnsapi.routes.home import router as home_router
from ddnsapi.routes.ping import router as ping_router
from fastapi import FastAPI


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(home_router)
    app.include_router(ping_router)
    return app


app = get_application()
