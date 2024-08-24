from fastapi import APIRouter

router = APIRouter

@router.get("/hello")
async def say_hello():
    return {"message": "hello from the hello route!"}