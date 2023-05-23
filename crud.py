from sqlalchemy.orm import Session

import models
import schemas


def get_item(db: Session, item_id: int):
    return db.query(models.Item).get(item_id)


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).get(item_id)
    if item:
        db.delete(item)
        db.commit()
        return True
    return False


def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = db.query(models.Item).get(item_id)
    if db_item:
        for field, value in item.dict().items():
            setattr(db_item, field, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    return None
