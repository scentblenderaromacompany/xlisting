# Backend Controllers Documentation

## get_item
- **Description:** Fetches an item from the database by its ID.
- **Parameters:**
  - db (Session): Database session.
  - item_id (int): ID of the item.
- **Returns:** Item object or None.

## create_item
- **Description:** Creates a new item in the database.
- **Parameters:**
  - db (Session): Database session.
  - 
ame (str): Name of the item.
- **Returns:** Created item object.

## cross_list_item
- **Description:** Cross-lists an item across multiple platforms.
- **Parameters:**
  - item_data (dict): Data of the item to cross-list.
- **Returns:** None.

## sync_inventory
- **Description:** Synchronizes inventory based on sales.
- **Parameters:**
  - db (Session): Database session.
  - item_id (int): ID of the item.
  - quantity_change (int): Quantity to adjust.
- **Returns:** None.

## Authentication Functions
- **verify_password:** Verifies a plain password against a hashed password.
- **get_password_hash:** Hashes a plain password.
- **authenticate_user:** Authenticates a user with username and password.
- **create_access_token:** Creates a JWT access token.
