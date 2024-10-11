from fastapi import APIRouter, HTTPException
from models import Item
from database import items_collection
from bson import ObjectId
from datetime import date

router = APIRouter()




@router.post("/items")
async def create_item(item: Item):
    item_data = item.dict()
    await items_collection.insert_one(item_data)
    return {"msg": "Item added successfully"}

@router.get("/items/{id}")
async def get_item(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/filter")
async def filter_items(email: str = None, expiry_date: date = None, insert_date: date = None, quantity: int = None):
    filters = {}
    if email:
        filters["email"] = email
    if expiry_date:
        filters["expiry_date"] = {"$gt": expiry_date}
    if insert_date:
        filters["insert_date"] = {"$gt": insert_date}
    if quantity:
        filters["quantity"] = {"$gte": quantity}

    items = await items_collection.find(filters).to_list(100)
    return items

@router.get("/items/aggregation")
async def aggregate_items():
    pipeline = [
        {"$group": {"_id": "$email", "total_items": {"$sum": 1}}}
    ]
    results = await items_collection.aggregate(pipeline).to_list(100)
    return results

@router.delete("/items/{id}")
async def delete_item(id: str):
    result = await items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"msg": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{id}")
async def update_item(id: str, item: Item):
    result = await items_collection.update_one({"_id": ObjectId(id)}, {"$set": item.dict(exclude_unset=True)})
    if result.modified_count == 1:
        return {"msg": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")
