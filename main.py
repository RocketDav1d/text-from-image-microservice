from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import UpdateUser, User, Gender, Role, UpdateUser
from typing import Optional, List


app = FastAPI()

db: List[User] = [
    User(
    id=UUID("c3c51040-2278-499e-88b0-55c007ea2a01"), 
    first_name="David", 
    last_name="Korn", 
    gender=Gender.female, 
    roles=[Role.student]
    ),

    User(
    id=UUID("c3c51040-2278-499e-88b0-55c007ea2a01"),
    first_name="Lisa",
    last_name="M",
    gender=Gender.female,
    roles=[Role.admin]
    )
]


@app.get("/")
async def root():
    return {"hello": "Mundo"} 

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def  register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} doesnt exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, update_user: UpdateUser):
    for user in db:
        if user.id == user_id:
            if user.first_name is not None:
               user.first_name = update_user.first_name
            if user.last_name is not None:
                user.last_name = update_user.last_name
            if user.middle_name is not None:
                user.middle_name = update_user.middle_name
            if user.gender is not None:
                user.gender = update_user.gender
            if user.roles is not None:
                user.roles = update_user.roles
            return
    raise HTTPException(
        status_code=404,
        detail="the user with id {user_id} does not exist"
    )

