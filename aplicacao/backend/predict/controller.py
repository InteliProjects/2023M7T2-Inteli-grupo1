from .service import PredictService
from fastapi import HTTPException
from prisma import errors

async def controller_predict(serial):
    if not serial:
        raise HTTPException(status_code=400,
                            detail="Invalid parameters")
    
    predictService = PredictService(serial=serial)
    try:
        prediction = await predictService.predict()
        return {"prediction": prediction}
    except errors.RecordNotFoundError:
        raise HTTPException(status_code=404,
                            detail="Airplane not found")
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=str(e))