
# Import necessary modules and classes
from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from .database import get_db, Item, ItemCreate, ItemUpdate

def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all_items(request: Request, db: Session = Depends(get_db), ):
    db_items = db.query(Item)
    return db_items

def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    # find our item ID in the database and update fields specified in the 'item' argument
    itemsAffected = db.query(Item).filter(Item.id == item_id).update(dict(**item.model_dump(exclude_unset=True)))
    db.commit()
    return itemsAffected

def update_item_put(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    itemsAffected = db.query(Item).filter(Item.id == item_id).update(dict(**item.model_dump()))
    db.commit()
    return itemsAffected

def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_delete = db.query(Item).filter(Item.id == item_id).delete(synchronize_session="auto")
    db.commit()

    if db_delete == 0:
        raise HTTPException(status_code=404, detail="A record with that ID was not found")

    return 0
