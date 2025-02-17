from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProductAdd(BaseModel):
    name:str
    add:bool
    Quantity:int
    price:float
    date_added:datetime

class Product(BaseModel):
    id:int
    name:str
    add:bool
    Quantity:int
    price:float
    date_added:datetime
    class Config:
        orm_mode = True