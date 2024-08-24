from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_user():
    return {"users": ["Tatiana", "Raoni", "Liz"]}

@router.post("/users")
async def create_user(user: str):
    return {"user": user, "message": "User created successfuly!"}

