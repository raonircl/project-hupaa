from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/")
async def say_hello():
    return {"message": "Hello, World!"}
