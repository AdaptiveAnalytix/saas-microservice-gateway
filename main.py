from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="SaaS Core Gateway", version="1.0.0")

class Subscription(BaseModel):
    user_id: int
    plan_type: str
    is_active: bool

# Simulated Database
fake_db = {
    1: {"user_id": 1, "plan_type": "Enterprise", "is_active": True}
}

@app.get("/")
async def health_check():
    return {"status": "operational", "service": "gateway"}

@app.get("/api/v1/subscription/{user_id}", response_model=Subscription)
async def get_subscription_status(user_id: int):
    """
    Fetch subscription details for gatekeeping SaaS features.
    """
    result = fake_db.get(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result
