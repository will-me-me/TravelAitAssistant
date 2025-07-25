from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import logging
from bson import ObjectId




class TravelQueryRequest(BaseModel):
    query: str

class TravelQueryResponse(BaseModel):
    id: Optional[str] = None
    query: str
    response: str
    success: bool
    user_id: Optional[str] = None
    created_at: Optional[str] = None