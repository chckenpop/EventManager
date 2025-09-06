# http endpoints for authentication

from fastapi import APIRouter
from fastapi import Depends
from App.utils.db import get_db
from App.services.auth_services import signup, login
from App.utils.security import create_access_token,verify_token
router = APIRouter()

@router.post("/login")
def login_user(username: str, password: str,db = Depends(get_db):
    user = login(username,password,db)
    access_token = create_access_token(data={"sub": user_id})

    return login(username, password)

@router.post("/signup")
def signup_user(username: str, password: str, db = Depends(get_db)):
    return signup(username, password)