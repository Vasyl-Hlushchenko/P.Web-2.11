from typing import List
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel


async def get_users(skip: int, limit: int, db: Session) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


async def get_user(user_id: int, db: Session) -> User:
    return db.query(User).filter(User.id == user_id).first()


async def create_user(body: UserModel, db: Session) -> User:
    user = User(first_name=body.first_name, 
    second_name=body.second_name, 
    email=body.email, 
    phone=body.phone, 
    birthaday=body.birthaday, 
    description=body.description)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def update_user(user_id: int, body: UserModel, db: Session) -> User| None:
    user= db.query(User).filter(User.id == user_id).first()
    if user:
        user.first_name = body.first_name
        user.second_name = body.second_name
        user.email = body.email
        user.phone = body.phone
        user.birthaday = body.birthaday
        user.description = body.description
        db.commit()
    return user


async def remove_user(user_id: int, db: Session)  -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


# async def get_users_by_first_name(first_name: str, db: Session) -> List[User]:
#     return db.query(User).filter(User.first_name.like(f'%{first_name}%')).all()


async def get_users_by_some_info(some_info: str, db: Session) -> List[User]:
    response = []
    info_by_first_name = db.query(User).filter(User.first_name.like(f'%{some_info}%')).all()
    if info_by_first_name:
        for n in info_by_first_name:
            response.append(n)
    info_by_second_name = db.query(User).filter(User.second_name.like(f'%{some_info}%')).all()
    if info_by_second_name:
        for n in info_by_second_name:
            response.append(n)
    info_by_email = db.query(User).filter(User.email.like(f'%{some_info}%')).all()
    if info_by_email:
        for n in info_by_email:
            response.append(n)
            
    return response


async def get_birthday_per_week(days: int, db: Session) -> User:
    response = []
    all_users = db.query(User).all()
    for user in all_users:
        if timedelta(0) <= ((user.birthaday.replace(year=int((datetime.now()).year))) - datetime.now().date()) <= timedelta(days):
            response.append(user)

    return response