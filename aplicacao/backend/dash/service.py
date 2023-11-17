from __init__ import db
from prisma import Prisma, errors
from contextlib import asynccontextmanager
from datetime import datetime, timedelta

class DashService:
    def __init__(self, id="", aircraftSerNum_1=""):
        # self.id = id
        self.id = aircraftSerNum_1
        
    @asynccontextmanager
    async def database_connection(self):
        self.db = db
        await self.db.connect()
        try:
            yield
        finally:
            await self.db.disconnect()
        
    
    async def dashboard(self):
        async with self.database_connection():
            errors = []
            try:
                my_airplane = await self.db.airplane.find_first(where={"id": self.id})
                dashboard_data = {
                "serial_number": str(my_airplane.aircraftSerNum_1),
                }
            except Exception as e:
                print("Erro em encontrar o avião: ", str(e))
                errors.append(str(e))
            
            try:
                all_flights = await self.db.flight.find_many(
                where = {"airplaneId": self.id}
                )
                dashboard_data["all_flights_count"] = len(all_flights)
            except Exception as e:
                print("Erro em encontrar os voos do aviao em questão: ", str(e))
                errors.append(str(e))
            

            try: 
                flights = await self.db.transformed.find_many(where = {"aircraftSerNum_1": self.id})
            
            
                total_flight_time = sum(flight["flightMinutes"] for flight in flights)
                
                
                today = datetime.now()
                first_day_of_current_month = today.replace(day=1)
                last_month_start = (first_day_of_current_month - timedelta(days=1)).replace(day=1)
                last_month_end = first_day_of_current_month - timedelta(days=1)
                
                flight_time_current_month = sum(
                    flight["flightMinutes"] 
                    for flight in flights 
                    if last_month_start <= flight["createdAt"] <= last_month_end
                    )
                
                flight_time_last_month = sum(
                    flight["flightMinutes"]
                    for flight in flights
                    if (last_month_start - timedelta(days=1)) <= flight["createdAt"] <= last_month_end
                )
                
                dashboard_data["flight_time"] = {
                    "all": total_flight_time,
                    "last_month": flight_time_last_month,
                    "current_month": flight_time_current_month
                }
            except Exception as e:
                print("Erro em pegar os voos do avião: ", str(e))
                errors.append(str(e))
            
            try:
                failures = await self.db.failure.find_many(where = {"aircraftSerNum_1": self.id})
                
                total_failure_count = len(failures)

                failure_count_current_month = len(
                    [failure 
                    for failure in failures
                    if (last_month_start <= failure.Flight["createdAt"] <= last_month_end)])
                
                failure_count_last_month = len(
                    [failure
                    for failure in failures
                    if (last_month_start - timedelta(days=1)) <= failure.Flight["createdAt"] <= last_month_end]
                )
                
                dashboard_data["flight_failures"] = {
                    "all": total_failure_count,
                    "last_month": failure_count_last_month,
                    "current_month": failure_count_current_month
                }
            except Exception as e:
                print("Erro em pegar os erros da aeronave: ", str(e))
                errors.append(str(e))
            
            try:
                other_airplanes = await self.db.airplane.find_many()
                dashboard_data["airplanes"] = {}
                for airplane in other_airplanes:
                    dashboard_data["airplanes"][str(airplane.aircraftSerNum_1)] = {}
                    airplane_id = airplane.id
                    dashboard_data["airplanes"][str(airplane.aircraftSerNum_1)]["serial_number"] = airplane.aircraftSerNum_1
                    dashboard_data["airplanes"][str(airplane.aircraftSerNum_1)]["description"] = airplane.description
                    
                    
                    last_flight = (await self.db.flight.find_many(
                        where= {"airplaneId": airplane_id},
                        order = {"createdAt": "desc"}
                    ))[0]
                    dashboard_data["airplanes"][str(airplane.aircraftSerNum_1)]["last_flight"] = last_flight
                    
                    flights = await self.db.transformed.find_many(
                        where = {"aircraftSerNum_1" : airplane.aircraftSerNum_1},
                    )
                    flight_minutes = sum(flight.flightMinutes for flight in flights)
                    dashboard_data["airplanes"][str(airplane.aircraftSerNum_1)]["flight_minutes"] = flight_minutes
                    
                    failures = len(await self.db.failure.find_many(
                        where = {"aircraftSerNum_1": airplane_id}
                    ))
                    dashboard_data["airplanes"][str(airplane.aircraftSerNum_1)]["failures"] = failures
            except Exception as e:
                print("Erro em pegar os dados de outras aeronaves: ", str(e))
                errors.append(str(e))
            
            dashboard_data["errors"] = errors
            return dashboard_data
    
    async def get_airplanes(self):
        async with self.database_connection():
            airplanes = await self.db.airplane.find_many()
            return airplanes
    
    async def get_transformed_by_serial(self):
        async with self.database_connection():
            airplane_flights = await self.db.transformed.find_many(
                where={
                        "aircraftSerNum_1": self.aircraftSerNum_1
                        },
                        include={"Predicted": True}
            )
            return airplane_flights
        
    async def get_airplane_by_serial(self):
        async with self.database_connection():
            airplane = await self.db.transformed.find_first(
                where={
                    "aircraftSerNum_1": self.id
                }
            )
                        
            return airplane
        
    async def get_predictions_by_serial(self):
        async with self.database_connection():
            predictions = await self.db.predicted.find_many(
                where={
                    "aircraftSerNum_1": self.id
                }
            )
            return predictions
    
    async def insert_into_transformed(self):
        async with self.database_connection():
            try:
                flyght = await self.db.transformed.find_unique_or_raise(
                    where={
                        "id": self.id
                    },
                )
                
                raise NameError("Data already exists")
            except errors.RecordNotFoundError:
                flyght = await self.db.transformed.create(data={
                "amscHprsovDrivF_1a": self.amscHprsovDrivF_1a,
                "amscHprsovDrivF_1b": self.amscHprsovDrivF_1b,
                "amscHprsovDrivF_2b": self.amscHprsovDrivF_2b,
                "amscPrsovDrivF_1a": self.amscPrsovDrivF_1a,
                "amscPrsovDrivF_1b": self.amscPrsovDrivF_1b,
                "amscPrsovDrivF_2b": self.amscPrsovDrivF_2b,
                "basBleedLowPressF_1a": self.basBleedLowPressF_1a,
                "basBleedLowPressF_2b": self.basBleedLowPressF_2b,
                "basBleedLowTempF_1a": self.basBleedLowTempF_1a,
                "basBleedLowTempF_2b": self.basBleedLowTempF_2b,
                "basBleedOverPressF_1a": self.basBleedOverPressF_1a,
                "basBleedOverPressF_2b": self.basBleedOverPressF_2b,
                "basBleedOverTempF_1a": self.basBleedOverTempF_1a,
                "basBleedOverTempF_2b": self.basBleedOverTempF_2b,
                "bleedFavTmCmd_1a": self.bleedFavTmCmd_1a,
                "bleedFavTmCmd_1b": self.bleedFavTmCmd_1b,
                "bleedFavTmCmd_2a": self.bleedFavTmCmd_2a,
                "bleedFavTmCmd_2b": self.bleedFavTmCmd_2b,
                "bleedFavTmFbk_1a": self.bleedFavTmFbk_1a,
                "bleedFavTmFbk_1b": self.bleedFavTmFbk_1b,
                "bleedFavTmFbk_2b": self.bleedFavTmFbk_2b,
                "bleedHprsovCmdStatus_1a": self.bleedHprsovCmdStatus_1a,
                "bleedHprsovCmdStatus_1b": self.bleedHprsovCmdStatus_1b,
                "bleedHprsovCmdStatus_2a": self.bleedHprsovCmdStatus_2a,
                "bleedHprsovCmdStatus_2b": self.bleedHprsovCmdStatus_2b,
                "bleedHprsovOpPosStatus_1a":self.bleedHprsovOpPosStatus_1a,
                "bleedHprsovOpPosStatus_1b":self.bleedHprsovOpPosStatus_1b,
                "bleedHprsovOpPosStatus_2a":self.bleedHprsovOpPosStatus_2a,
                "bleedHprsovOpPosStatus_2b":self.bleedHprsovOpPosStatus_2b,
                "bleedMonPress_1a": self.bleedMonPress_1a,
                "bleedMonPress_1b": self.bleedMonPress_1b,
                "bleedMonPress_2a": self.bleedMonPress_2a,
                "bleedMonPress_2b": self.bleedMonPress_2b,
                "bleedOnStatus_1a": self.bleedOnStatus_1a,
                "bleedOnStatus_1b": self.bleedOnStatus_1b,
                "bleedOnStatus_2b": self.bleedOnStatus_2b,
                "bleedOverpressCas_2a": self.bleedOverpressCas_2a,
                "bleedOverpressCas_2b": self.bleedOverpressCas_2b,
                "bleedPrecoolDiffPress_1a": self.bleedPrecoolDiffPress_1a,
                "bleedPrecoolDiffPress_1b": self.bleedPrecoolDiffPress_1b,
                "bleedPrecoolDiffPress_2a": self.bleedPrecoolDiffPress_2a,
                "bleedPrecoolDiffPress_2b": self.bleedPrecoolDiffPress_2b,
                "bleedPrsovClPosStatus_1a": self.bleedPrsovClPosStatus_1a,
                "bleedPrsovClPosStatus_2a": self.bleedPrsovClPosStatus_2a,
                "bleedPrsovFbk_1a": self.bleedPrsovFbk_1a,
                "bleedPrsovFbk_1b": self.bleedPrsovFbk_1b,
                "bleedPrsovFbk_2b": self.bleedPrsovFbk_2b,
                "flightMinutes": self.flightMinutes,
                "message0418DAA_1": self.message0418DAA_1,
                "message0422DAA_1": self.message0422DAA_1,
                "aircraftSerNum_1": self.id              
                })
                return flyght