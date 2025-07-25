from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import travel.travel_routes as travel_routes
import users.users_routes as users_routes
from database import db
from dotenv import load_dotenv
load_dotenv()




app = FastAPI(
    title="Travel Documentation Assistant API",
    description="API for getting travel documentation requirements using AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
app.include_router(
    users_routes.router,
    prefix="/users",
    tags=["users"],
)


app.include_router(
    travel_routes.router,
    prefix="/travel",
    tags=["travel"],

)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}