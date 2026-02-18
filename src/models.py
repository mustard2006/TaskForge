from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from database import Base
from utils import Role, Status
from typing import List

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(SQLEnum(Role), default=Role.User)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    tasks = relationship("Task", back_populates="user")

    def __str__(self):
        return f"User: {self.username} ({self.email}) {self.role.value}"

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, role={self.role})"

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(SQLEnum(Status), default=Status.Pending)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="tasks")

    def __str__(self):
        return f"Task: {self.title} - {self.status.value}"

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"