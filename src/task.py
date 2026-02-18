import uuid
from datetime import datetime
from utils import *

class Task:
    def __init__(self, user_id, title, description):
        self.id = uuid.uuid4()
        self._user_id = user_id
        self.title = title
        self.description = description
        self.status: Status = Status.Pending
        self.created_at = datetime.now()
        self.updated_at = None

    def __str__(self):
        return f"Task: title={self.title}, description={self.description}, status={self.status}"

    def __repr__ (self):
        return f"Task: id={self.id}, user_id={self.user_id}, title={self.title}, description={self.description}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at}"

    # to json
    def to_dict(self):
        return{
            "id": str(self.id),
            "user_id": str(self._user_id),
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    # from json
    @classmethod
    def from_dict(cls, data):
        task = cls(data["user_id"], data["title"], data["description"])
        task.id = uuid.UUID(data["id"])
        task.status = Status(data["status"])
        return task

    def mark_pending(self) -> None:
        self.status = Status.Pending
        self.updated_at = datetime.now()

    def mark_done(self) -> None:
        self.status = Status.Done
        self.updated_at = datetime.now()

    # ------------------------
    # Read-only user_id property
    # ------------------------
    @property
    def user_id(self):
        return self._user_id
    