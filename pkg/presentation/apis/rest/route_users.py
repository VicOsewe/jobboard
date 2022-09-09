from http.client import responses
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from pkg.domain.dao.schemas.users import ShowUser, UserCreate
from pkg.infrastructure.db.session import get_db
from pkg.usecases.user import create_new_user

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 