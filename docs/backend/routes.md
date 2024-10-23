# Backend Routes Documentation

## GET /items/{item_id}
- **Description:** Retrieve an item by its ID.
- **Parameters:**
  - item_id (int): The ID of the item to retrieve.
- **Responses:**
  - 200 OK: Returns the item data.
  - 404 Not Found: If the item does not exist.

## POST /items/
- **Description:** Create a new item.
- **Parameters:**
  - 
ame (str): The name of the item.
- **Responses:**
  - 200 OK: Returns the created item data.

## POST /cross-list/
- **Description:** Cross-list an item across multiple platforms and synchronize inventory.
- **Parameters:**
  - item_data (dict): Data of the item to cross-list.
- **Responses:**
  - 200 OK: Confirmation message.
