from backend.models.models import Item
from sqlalchemy.orm import Session
from fastapi import HTTPException

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, name: str):
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
