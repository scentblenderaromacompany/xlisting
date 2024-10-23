from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.models import Item
from backend.controllers.controllers import get_item, create_item
from backend.controllers.cross_listing import cross_list_item
from backend.controllers.inventory_sync import sync_inventory
from backend.database.init_db import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items/")
async def add_item(name: str, db: Session = Depends(get_db)):
    item = create_item(db, name)
    return item

@router.post("/cross-list/")
async def cross_list(item_data: dict, db: Session = Depends(get_db)):
    cross_list_item(item_data)
    sync_inventory(db, item_data['item_id'], -item_data['quantity'])
    return {"message": "Item cross-listed and inventory synchronized."}

@router.get("/sales/")
async def get_sales(db: Session = Depends(get_db)):
    sales = db.query(Sales).all()
    return sales

@router.get("/inventory/")
async def get_inventory(db: Session = Depends(get_db)):
    inventory = db.query(Inventory).all()
    return inventory
