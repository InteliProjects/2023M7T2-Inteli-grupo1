from fastapi import APIRouter, Depends
from .controller import controller_predict
from auth.dependencies import get_jwt_payload
from pydantic import BaseModel

router = APIRouter(prefix="/predict", tags=["predict"])

# class InputPredict(BaseModel):
    # aircraftSerNum_1: str | None = None
    
@router.post("/classifier")
async def predict_and_save(serial: str):
    return await controller_predict(serial)