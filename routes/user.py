from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate, User
from models.user import User
from configs.db import db

router = APIRouter()

@router.get("/testing")
async def testing():
    return {"message": "testing"}