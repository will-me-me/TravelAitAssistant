from anthropic import AsyncAnthropic
import os
from typing import Dict, Any, List
from database import db
from bson import ObjectId


async def get_travel_documentation(query: str) -> Dict[str, Any]:
    try:
        # Ensure the API key is set
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Anthropic API key is not set in environment variables.")

        system_prompt = """You are a travel documentation expert assistant. When users ask about travel requirements between countries, provide comprehensive, accurate, and well-structured information.
        Always structure your response in the following format:
        1. **Visa Requirements**
        2. **Passport Requirements**
        3. **Additional Documentation**
        4. **Important Notes**
        5. **Processing Time**
        6. **Useful Tips**
        Ensure your information is current as of 2024 and provide disclaimers about checking with official sources."""

        client = AsyncAnthropic(api_key=api_key)
        response = await client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1500,
            temperature=0.7,
            system=system_prompt,  # ✅ correct placement
            messages=[
                {"role": "user", "content": f"Please provide travel documentation requirements for: {query}"}
            ]
        )

        print(f"Claude API Response: {response.content}")
        return {
            "success": True,
            "response": response.content[0].text,
            "model": "claude-3-sonnet-20240229"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "response": "I apologize, but I'm unable to process your request right now. Please try again later."
        }
    
async def get_query_history() -> List[Dict[str, Any]]:
    try:
        # Fetch all travel documents from the database
        travel_docs = db.travel_collection.find()
        print(f"Fetched Travel Documents: {travel_docs}")
        history = []
        for doc in travel_docs:
            history.append({
                "id": str(doc["_id"]),
                "query": doc["query"],
                "response": doc["response"],
                "success": doc["success"],
                "user_id":  doc.get("user_id"),
                "created_at": doc["created_at"].isoformat()
            })
        return history
    except Exception as e:
        print(f"Error fetching query history: {e}")
        return []
    
async def get_travel_documentation_by_id(travel_id: str) -> Dict[str, Any]:
    try:
        # Fetch the travel document by ID
        from bson import ObjectId
        travel_doc = db.travel_collection.find_one({"_id": ObjectId(travel_id)})
        print(f"Fetched Travel Document: {travel_doc}")
        if not travel_doc:
            return {
                "success": False,
                "error": "Travel documentation not found",
                "response": ""
            }
        return {
            "id": str(travel_doc["_id"]),
            "success": True,
            "query": travel_doc["query"],
            "response": travel_doc["response"],
            "created_at": travel_doc["created_at"].isoformat()
        }
    except Exception as e:
        print(f"Error fetching travel documentation by ID: {e}")
        return {
            "success": False,
            "error": str(e),
            "response": ""
        }
    
async def delete_travel_documentation(travel_id: str) -> Dict[str, Any]:
    try:
        result = db.travel_collection.delete_one({"_id": ObjectId(travel_id)})
        if result.deleted_count == 0:
            return {
                "success": False,
                "error": "Travel documentation not found",
                "response": ""
            }
        return {
            "success": True,
            "response": "Travel documentation deleted successfully"
        }
    except Exception as e:
        print(f"Error deleting travel documentation: {e}")
        return {
            "success": False,
            "error": str(e),
            "response": ""
        }
    
    

    