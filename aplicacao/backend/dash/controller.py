from .service import DashService
from fastapi import HTTPException
from prisma import errors


async def controller_get_dashboard(serial: str) -> dict:
    if serial == "":
        raise HTTPException(status_code=400, detail="Invalid parameters")
    
    dashService = DashService(aircraftSerNum_1=serial)
    try: 
        dashboard_data = await dashService.dashboard()
        return dashboard_data
    except errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail="Some data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def controller_get_airplane_by_serial(serial: str) -> dict:
    if serial == "":
        raise HTTPException(status_code=400, detail="Invalid Parameters")

    dashService = DashService(aircraftSerNum_1=serial)
    try:
        airplane = await dashService.get_airplane_by_serial()
        return {"airplane": airplane}
    except errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail="Airplane not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def controller_get_flights_by_serial(serial: str):
    if serial == "":
        raise HTTPException(status_code=400, detail="Invalid Parameters")
    
    dashService = DashService(aircraftSerNum_1=serial)
    
    try:
        flights = await dashService.get_transformed_by_serial()
        return {
            "aircraftSerNum_1": serial,
            "flights": flights
        }
    except errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail=f"Not found flights for airplane {serial}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def controller_get_predictions(serial: str):
    if serial == "":
        raise HTTPException(status_code=400, detail="Invalid Parameters")
    
    dashService = DashService(aircraftSerNum_1=serial)
    try:
        predictions = await dashService.get_predictions_by_serial()
        return {"predictions": predictions}
    except errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail="Predictions not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def controller_insert_into_transformed(
    amscHprsovDrivF_1a: float,
    amscHprsovDrivF_1b: float,
    amscHprsovDrivF_2b: float,
    amscPrsovDrivF_1a: float,
    amscPrsovDrivF_1b: float,
    amscPrsovDrivF_2b: float,
    basBleedLowPressF_1a: float,
    basBleedLowPressF_2b: float,
    basBleedLowTempF_1a: float,
    basBleedLowTempF_2b: float,
    basBleedOverPressF_1a: float,
    basBleedOverPressF_2b: float,
    basBleedOverTempF_1a: float,
    basBleedOverTempF_2b: float,
    bleedFavTmCmd_1a: float,
    bleedFavTmCmd_1b: float,
    bleedFavTmCmd_2a: float,
    bleedFavTmCmd_2b: float,
    bleedFavTmFbk_1a: float,
    bleedFavTmFbk_1b: float,
    bleedFavTmFbk_2b: float,
    bleedHprsovCmdStatus_1a: float,
    bleedHprsovCmdStatus_1b: float,
    bleedHprsovCmdStatus_2a: float,
    bleedHprsovCmdStatus_2b: float,
    bleedHprsovOpPosStatus_1a: float,
    bleedHprsovOpPosStatus_1b: float,
    bleedHprsovOpPosStatus_2a: float,
    bleedHprsovOpPosStatus_2b: float,
    bleedMonPress_1a: float,
    bleedMonPress_1b: float,
    bleedMonPress_2a: float,
    bleedMonPress_2b: float,
    bleedOnStatus_1a: float,
    bleedOnStatus_1b: float,
    bleedOnStatus_2b: float,
    bleedOverpressCas_2a: float,
    bleedOverpressCas_2b: float,
    bleedPrecoolDiffPress_1a: float,
    bleedPrecoolDiffPress_1b: float,
    bleedPrecoolDiffPress_2a: float,
    bleedPrecoolDiffPress_2b: float,
    bleedPrsovClPosStatus_1a: float,
    bleedPrsovClPosStatus_2a: float,
    bleedPrsovFbk_1a: float,
    bleedPrsovFbk_1b: float,
    bleedPrsovFbk_2b: float,
    flightMinutes: float,
    message0418DAA_1: float,
    message0422DAA_1: float,
    aircraftSerNum_1: str):
    dash = DashService( amscHprsovDrivF_1a=amscHprsovDrivF_1a,
                        amscHprsovDrivF_1b=amscHprsovDrivF_1b,
                        amscHprsovDrivF_2b=amscHprsovDrivF_2b,
                        amscPrsovDrivF_1a=amscPrsovDrivF_1a,
                        amscPrsovDrivF_1b=amscPrsovDrivF_1b,
                        amscPrsovDrivF_2b=amscPrsovDrivF_2b,
                        basBleedLowPressF_1a=basBleedLowPressF_1a,
                        basBleedLowPressF_2b=basBleedLowPressF_2b,
                        basBleedLowTempF_1a=basBleedLowTempF_1a,
                        basBleedLowTempF_2b=basBleedLowTempF_2b,
                        basBleedOverPressF_1a=basBleedOverPressF_1a,
                        basBleedOverPressF_2b=basBleedOverPressF_2b,
                        basBleedOverTempF_1a=basBleedOverTempF_1a,
                        basBleedOverTempF_2b=basBleedOverTempF_2b,
                        bleedFavTmCmd_1a=bleedFavTmCmd_1a,
                        bleedFavTmCmd_1b=bleedFavTmCmd_1b,
                        bleedFavTmCmd_2a=bleedFavTmCmd_2a,
                        bleedFavTmCmd_2b=bleedFavTmCmd_2b,
                        bleedFavTmFbk_1a=bleedFavTmFbk_1a,
                        bleedFavTmFbk_1b=bleedFavTmFbk_1b,
                        bleedFavTmFbk_2b=bleedFavTmFbk_2b,
                        bleedHprsovCmdStatus_1a=bleedHprsovCmdStatus_1a,
                        bleedHprsovCmdStatus_1b=bleedHprsovCmdStatus_1b,
                        bleedHprsovCmdStatus_2a=bleedHprsovCmdStatus_2a,
                        bleedHprsovCmdStatus_2b=bleedHprsovCmdStatus_2b,
                        bleedHprsovOpPosStatus_1a=bleedHprsovOpPosStatus_1a,
                        bleedHprsovOpPosStatus_1b=bleedHprsovOpPosStatus_1b,
                        bleedHprsovOpPosStatus_2a=bleedHprsovOpPosStatus_2a,
                        bleedHprsovOpPosStatus_2b=bleedHprsovOpPosStatus_2b,
                        bleedMonPress_1a=bleedMonPress_1a,
                        bleedMonPress_1b=bleedMonPress_1b,
                        bleedMonPress_2a=bleedMonPress_2a,
                        bleedMonPress_2b=bleedMonPress_2b,
                        bleedOnStatus_1a=bleedOnStatus_1a,
                        bleedOnStatus_1b=bleedOnStatus_1b,
                        bleedOnStatus_2b=bleedOnStatus_2b,
                        bleedOverpressCas_2a=bleedOverpressCas_2a,
                        bleedOverpressCas_2b=bleedOverpressCas_2b,
                        bleedPrecoolDiffPress_1a=bleedPrecoolDiffPress_1a,
                        bleedPrecoolDiffPress_1b=bleedPrecoolDiffPress_1b,
                        bleedPrecoolDiffPress_2a=bleedPrecoolDiffPress_2a,
                        bleedPrecoolDiffPress_2b=bleedPrecoolDiffPress_2b,
                        bleedPrsovClPosStatus_1a=bleedPrsovClPosStatus_1a,
                        bleedPrsovClPosStatus_2a=bleedPrsovClPosStatus_2a,
                        bleedPrsovFbk_1a=bleedPrsovFbk_1a,
                        bleedPrsovFbk_1b=bleedPrsovFbk_1b,
                        bleedPrsovFbk_2b=bleedPrsovFbk_2b,
                        flightMinutes=flightMinutes,
                        message0418DAA_1=message0418DAA_1,
                        message0422DAA_1=message0422DAA_1,
                        aircraftSerNum_1=aircraftSerNum_1)
    try:
        new_flight = await dash.insert_into_transformed()
        print(new_flight)
        return {"message": "Flight created successfully"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))


async def controller_get_airplanes():
    dashService = DashService()
    try:
        airplanes = await dashService.get_airplanes()
        return {"airplanes": airplanes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
