from sqlalchemy.orm import Session

from pkg.domain.dao.schemas.users import UserCreate
from pkg.domain.dto.models.users import User
from pkg.application.core.hashing import Hasher


def create_user(user:UserCreate,db:Session):
    user = User(username=user.username,
        email = user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user