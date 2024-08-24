from fastapi import FastAPI
from routes import hello, users

app = FastAPI()

app.include_router(hello.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/api/v1/")
async def say_hello():
    return {"message": "Hello, World!"}
