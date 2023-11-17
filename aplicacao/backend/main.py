import uvicorn
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from user.routes import router as UserRouter
from admin.routes import router as AdminRouter
from auth.routes import router as AuthRouter
from dash.routes import router as DashRouter
# from predict.routes import router as PredictionRouter
# from sklearn.preprocessing import MinMaxScaler
from fastapi.responses import FileResponse

app = FastAPI()

origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter)
app.include_router(AdminRouter)
app.include_router(AuthRouter)
app.include_router(DashRouter)
# app.include_router(PredictionRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3001)