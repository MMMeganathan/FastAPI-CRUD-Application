from fastapi import APIRouter, HTTPException
from models import ClockIn
from database import clock_in_collection
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/clock-in")
async def clock_in(clock_in_data: ClockIn):
    data = clock_in_data.dict()
    await clock_in_collection.insert_one(data)
    return {"msg": "Clock-in recorded"}

@router.get("/clock-in/{id}")
async def get_clock_in(id: str):
    record = await clock_in_collection.find_one({"_id": ObjectId(id)})
    if record:
        return record
    raise HTTPException(status_code=404, detail="Record not found")

@router.get("/clock-in/filter")
async def filter_clock_ins(email: str = None, location: str = None, insert_datetime: datetime = None):
    filters = {}
    if email:
        filters["email"] = email
    if location:
        filters["location"] = location
    if insert_datetime:
        filters["insert_datetime"] = {"$gt": insert_datetime}

    records = await clock_in_collection.find(filters).to_list(100)
    return records

@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"msg": "Clock-in record deleted"}
    raise HTTPException(status_code=404, detail="Record not found")

@router.put("/clock-in/{id}")
async def update_clock_in(id: str, clock_in_data: ClockIn):
    result = await clock_in_collection.update_one({"_id": ObjectId(id)}, {"$set": clock_in_data.dict(exclude_unset=True)})
    if result.modified_count == 1:
        return {"msg": "Clock-in record updated"}
    raise HTTPException(status_code=404, detail="Record not found")
