from backend.models.models import Inventory
from sqlalchemy.orm import Session

def sync_inventory(db: Session, item_id: int, quantity_change: int):
    inventory = db.query(Inventory).filter(Inventory.item_id == item_id).first()
    if inventory:
        inventory.quantity += quantity_change
    else:
        inventory = Inventory(item_id=item_id, quantity=quantity_change)
        db.add(inventory)
    db.commit()
