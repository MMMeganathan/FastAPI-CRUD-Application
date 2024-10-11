from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class Item(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date
    insert_date: Optional[date] = Field(default_factory=date.today)

class ClockIn(BaseModel):
    email: str
    location: str
    insert_datetime: Optional[datetime] = Field(default_factory=datetime.now)
