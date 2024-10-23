from backend.models.models import Item, Inventory, Sales, User, Policy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    # Create the database and the tables
    from backend.database.init_db import init_db
    init_db()
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_item(db):
    from backend.controllers.controllers import create_item
    item = create_item(db, "Test Item")
    assert item.name == "Test Item"

def test_create_inventory(db):
    inventory = Inventory(item_id=1, quantity=100)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    assert inventory.quantity == 100

def test_create_sales(db):
    sales = Sales(item_id=1, quantity=5)
    db.add(sales)
    db.commit()
    db.refresh(sales)
    assert sales.quantity == 5
