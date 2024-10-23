# Backend Models Documentation

## Item
- **id**: Integer, primary key.
- **name**: String, indexed.

## Sales
- **id**: Integer, primary key.
- **item_id**: Integer, foreign key referencing Item.
- **quantity**: Integer, not nullable.
- **sale_date**: DateTime, defaults to current timestamp.

## Inventory
- **id**: Integer, primary key.
- **item_id**: Integer, foreign key referencing Item.
- **quantity**: Integer, not nullable.

## User
- **id**: Integer, primary key.
- **username**: String, unique, not nullable.
- **email**: String, unique, not nullable.
- **password_hash**: String, not nullable.
- **created_at**: DateTime, defaults to current timestamp.

## Policy
- **id**: Integer, primary key.
- **policy_type**: String, not nullable.
- **content**: String, not nullable.
- **created_at**: DateTime, defaults to current timestamp.
