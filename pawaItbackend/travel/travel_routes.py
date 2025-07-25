from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from database import db
import uuid
from travel.travel_model import TravelQueryRequest, TravelQueryResponse
import travel.travel_services as travel_services
from bson import ObjectId
import auth.jwt_auth as auth


router = APIRouter()

@router.get("/")
async def read_root():
    message = {
        "message": "Welcome to the Travel Routes API! Use the endpoints to manage travel routes."
    }
    return message

@router.post("/query", response_model=TravelQueryResponse)
async def process_travel_query(request: TravelQueryRequest, current_user: dict = Depends(auth.get_current_user)):
    try:
        print(f'current_user: {current_user}')
        if not request.query or len(request.query.strip()) < 5:
            raise HTTPException(
                status_code=400, 
                detail="Query must be at least 5 characters long"
            )
        # user = 
        ai_response = await travel_services.get_travel_documentation(request.query)
        # print(f"AI Response: {ai_response}")
        if not ai_response["success"]:
            raise HTTPException(
                status_code=500,
                detail="AI service temporarily unavailable"

            )
        now = datetime.utcnow()
        print(f"Current User: {current_user.get('_id')}")
        # ✅ Save to MongoDB
        travel_doc = {
            "_id": ObjectId(), 
            "query": request.query,
            "response": ai_response["response"],
            "success": ai_response["success"],
            "user_id": str(current_user.get("_id")),
            "created_at": now
        }
        db.travel_collection.insert_one(travel_doc)
        
        final_response = TravelQueryResponse(
            id=str(travel_doc["_id"]),
            query=travel_doc["query"],
            response=travel_doc["response"],
            success=travel_doc["success"],
            user_id=travel_doc["user_id"],
            created_at=travel_doc["created_at"].isoformat()
        )
        print(f"Final Response: {final_response}")
        return final_response
    
        
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )
    
@router.get("/history", response_model=List[TravelQueryResponse])
async def get_query_history(current_user: dict = Depends(auth.get_current_user)):
    try:
        history = await travel_services.get_query_history()
        if not history:
            raise HTTPException(
                status_code=404,
                detail="No query history found"
            )
        return history
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )
    
@router.get("/documentation/{travel_id}", response_model=TravelQueryResponse)
async def get_travel_documentation_by_id(travel_id: str, current_user: dict = Depends(auth.get_current_user)):
    try:
        travel_doc = await travel_services.get_travel_documentation_by_id(travel_id)
        if not travel_doc["success"]:
            raise HTTPException(
                status_code=404,
                detail=travel_doc["error"]
            )
        return TravelQueryResponse(
            id=str(travel_doc["id"]),
            query=travel_doc["query"],
            response=travel_doc["response"],
            success=travel_doc["success"],
            created_at=travel_doc["created_at"]
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )
    
@router.delete("/documentation/{travel_id}", response_model=dict)
async def delete_travel_documentation(travel_id: str, current_user: dict = Depends(auth.get_current_user)):
    try:
        result = await travel_services.delete_travel_documentation(travel_id)
        if not result["success"]:
            raise HTTPException(
                status_code=404,
                detail=result["error"]
            )
        return {"message": result["response"]}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )
    
    