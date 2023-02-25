from fastapi import FastAPI
from routes import ping

app = FastAPI()
app.include_router(ping.router)

@app.get("/")
async def root():
    return {"message": "Hello DDNS!"}
