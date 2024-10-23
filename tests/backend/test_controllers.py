from backend.controllers.controllers import get_item, create_item
from backend.models.models import Item
from sqlalchemy.orm import Session

def test_get_item(db):
    item = get_item(db, 1)
    assert item is not None
    assert item.name == "Test Item"
