from __init__ import db
from prisma import Prisma
from contextlib import asynccontextmanager
import pickle


model_filename1 = 'predict/classification_model.pkl'

with open(model_filename1, 'rb') as file:
    model1 = pickle.load(file)

class PredictService:
    def __init__(self, serial):
        self.serial = serial
        
    @asynccontextmanager
    async def database_connection(self):
        self.db = db
        await self.db.connect()
        try:
            yield
        finally:
            await self.db.disconnect()
    
    async def class_predict(self):
        async with self.database_connection():
            airplane_id = (await self.db.airplane.find_first(
                where = {
                    "aircraftSerNum_1": self.serial
                }
            )).id
            
            last_flight_id = (await self.db.flight.find_first(
                where = {
                    "airplaneId": airplane_id
                },
                order = {"createdAt": "desc"}
            )).id
            
            data = await self.db.transformed.find_first(
                where = {
                    "flightId": last_flight_id
                }
            )
            
            prediction = model1.predict(data)
            print(prediction)
            
            return {
                "prediction": prediction
            }