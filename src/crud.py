from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Task
from utils import Status, Role
from datetime import datetime

def create_user(db: Session, name: str, email: str, password_hash: str, role: Role):
    user = User(username=name, email=email, password_hash=password_hash, role=role, created_at=datetime.now())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Get user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Get multiple users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Update user
def update_user_name(db: Session, user_id: int, new_name: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = new_name
        db.commit()
    return user

# Delete user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def create_task(db: Session, title: str, description: str, user_id: int):
    task = Task(title=title, description=description, user_id=user_id, created_at=datetime.now())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

def get_task(db: Session, title: str):
    return db.query(Task).filter(Task.title == title).first()

def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def mark_task_done(db: Session, title: str):
    task = db.query(Task).filter(Task.title == title).first()
    if task:
        task.status = Status.Done
        db.commit()
    return task