from pydantic import BaseModel


class TodoItemBase(BaseModel):
    title: str
    details: str
    priority: int
    created_at: str
    is_completed: bool


class TodoItem(TodoItemBase):
    item_id: int

    class Config:
        from_attributes = True


class TodoItemCreate(TodoItemBase):
    item_id: int

    class Config:
        from_attributes = True