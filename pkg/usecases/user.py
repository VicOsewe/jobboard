from sqlalchemy.orm import Session
from fastapi import Depends

from pkg.domain.dao.schemas.users import ShowUser, UserCreate
from pkg.infrastructure.db.session import get_db
from pkg.infrastructure.db.repository.users import create_user

def create_new_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_user(user=user,db=db)
    return user 