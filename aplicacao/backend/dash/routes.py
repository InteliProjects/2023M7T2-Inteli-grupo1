from fastapi import APIRouter, Depends
from .controller import (
    controller_get_airplanes,
    controller_get_airplane_by_serial,
    controller_insert_into_transformed,
    controller_get_predictions,
    controller_get_flights_by_serial,
    controller_get_dashboard
)
from auth.dependencies import get_jwt_payload
from fastapi import HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/dash", tags=["dashboard"])

class CreateFlightRequest(BaseModel):
    amscHprsovDrivF_1a: float | None = None
    amscHprsovDrivF_1b: float | None = None
    amscHprsovDrivF_2b: float | None = None
    amscPrsovDrivF_1a: float | None = None
    amscPrsovDrivF_1b: float | None = None
    amscPrsovDrivF_2b: float | None = None
    basBleedLowPressF_1a: float | None = None
    basBleedLowPressF_2b: float | None = None
    basBleedLowTempF_1a: float | None = None
    basBleedLowTempF_2b: float | None = None
    basBleedOverPressF_1a: float | None = None
    basBleedOverPressF_2b: float | None = None
    basBleedOverTempF_1a: float | None = None
    basBleedOverTempF_2b: float | None = None
    bleedFavTmCmd_1a: float | None = None
    bleedFavTmCmd_1b: float | None = None
    bleedFavTmCmd_2a: float | None = None
    bleedFavTmCmd_2b: float | None = None
    bleedFavTmFbk_1a: float | None = None
    bleedFavTmFbk_1b: float | None = None
    bleedFavTmFbk_2b: float | None = None
    bleedHprsovCmdStatus_1a: float | None = None
    bleedHprsovCmdStatus_1b: float | None = None
    bleedHprsovCmdStatus_2a: float | None = None
    bleedHprsovCmdStatus_2b: float | None = None
    bleedHprsovOpPosStatus_1a: float | None = None
    bleedHprsovOpPosStatus_1b: float | None = None
    bleedHprsovOpPosStatus_2a: float | None = None
    bleedHprsovOpPosStatus_2b: float | None = None
    bleedMonPress_1a: float | None = None
    bleedMonPress_1b: float | None = None
    bleedMonPress_2a: float | None = None
    bleedMonPress_2b: float | None = None
    bleedOnStatus_1a: float | None = None
    bleedOnStatus_1b: float | None = None
    bleedOnStatus_2b: float | None = None
    bleedOverpressCas_2a: float | None = None
    bleedOverpressCas_2b: float | None = None
    bleedPrecoolDiffPress_1a: float | None = None
    bleedPrecoolDiffPress_1b: float | None = None
    bleedPrecoolDiffPress_2a: float | None = None
    bleedPrecoolDiffPress_2b: float | None = None
    bleedPrsovClPosStatus_1a: float | None = None
    bleedPrsovClPosStatus_2a: float | None = None
    bleedPrsovFbk_1a: float | None = None
    bleedPrsovFbk_1b: float | None = None
    bleedPrsovFbk_2b: float | None = None
    flightMinutes: float | None = None
    message0418DAA_1: float | None = None
    message0422DAA_1: float | None = None
    aircraftSerNum_1: str | None = None


@router.get("/airplanes")
async def get_airplanes():
    return await controller_get_airplanes()


@router.post("/flight")
async def post_flight(data: CreateFlightRequest):
    return await controller_insert_into_transformed(
    amscHprsovDrivF_1a=         data.amscHprsovDrivF_1a           , 
    amscHprsovDrivF_1b=         data.amscHprsovDrivF_1b            ,
    amscHprsovDrivF_2b=         data.amscHprsovDrivF_2b            ,
    amscPrsovDrivF_1a=          data.amscPrsovDrivF_1a             ,
    amscPrsovDrivF_1b=          data.amscPrsovDrivF_1b             ,
    amscPrsovDrivF_2b=          data.amscPrsovDrivF_2b             ,
    basBleedLowPressF_1a=       data.basBleedLowPressF_1a              ,
    basBleedLowPressF_2b=       data.basBleedLowPressF_2b              ,
    basBleedLowTempF_1a=        data.basBleedLowTempF_1a               ,
    basBleedLowTempF_2b=        data.basBleedLowTempF_2b               ,
    basBleedOverPressF_1a=      data.basBleedOverPressF_1a             ,
    basBleedOverPressF_2b=      data.basBleedOverPressF_2b             ,
    basBleedOverTempF_1a=       data.basBleedOverTempF_1a              ,
    basBleedOverTempF_2b=       data.basBleedOverTempF_2b              ,
    bleedFavTmCmd_1a=           data.bleedFavTmCmd_1a              ,
    bleedFavTmCmd_1b=           data.bleedFavTmCmd_1b              ,
    bleedFavTmCmd_2a=           data.bleedFavTmCmd_2a              ,
    bleedFavTmCmd_2b=           data.bleedFavTmCmd_2b              ,
    bleedFavTmFbk_1a=           data.bleedFavTmFbk_1a              ,
    bleedFavTmFbk_1b=           data.bleedFavTmFbk_1b              ,
    bleedFavTmFbk_2b=           data.bleedFavTmFbk_2b              ,
    bleedHprsovCmdStatus_1a=    data.bleedHprsovCmdStatus_1a               ,
    bleedHprsovCmdStatus_1b=    data.bleedHprsovCmdStatus_1b               ,
    bleedHprsovCmdStatus_2a=    data.bleedHprsovCmdStatus_2a               ,
    bleedHprsovCmdStatus_2b=    data.bleedHprsovCmdStatus_2b               ,
    bleedHprsovOpPosStatus_1a=  data.bleedHprsovOpPosStatus_1a             ,
    bleedHprsovOpPosStatus_1b=  data.bleedHprsovOpPosStatus_1b             ,
    bleedHprsovOpPosStatus_2a=  data.bleedHprsovOpPosStatus_2a             ,
    bleedHprsovOpPosStatus_2b=  data.bleedHprsovOpPosStatus_2b             ,
    bleedMonPress_1a=           data.bleedMonPress_1a              ,
    bleedMonPress_1b=           data.bleedMonPress_1b              ,
    bleedMonPress_2a=           data.bleedMonPress_2a              ,
    bleedMonPress_2b=           data.bleedMonPress_2b              ,
    bleedOnStatus_1a=           data.bleedOnStatus_1a              ,
    bleedOnStatus_1b=           data.bleedOnStatus_1b              ,
    bleedOnStatus_2b=           data.bleedOnStatus_2b              ,
    bleedOverpressCas_2a=       data.bleedOverpressCas_2a              ,
    bleedOverpressCas_2b=       data.bleedOverpressCas_2b              ,
    bleedPrecoolDiffPress_1a=   data.bleedPrecoolDiffPress_1a              ,
    bleedPrecoolDiffPress_1b=   data.bleedPrecoolDiffPress_1b              ,
    bleedPrecoolDiffPress_2a=   data.bleedPrecoolDiffPress_2a              ,
    bleedPrecoolDiffPress_2b=   data.bleedPrecoolDiffPress_2b              ,
    bleedPrsovClPosStatus_1a=   data.bleedPrsovClPosStatus_1a              ,
    bleedPrsovClPosStatus_2a=   data.bleedPrsovClPosStatus_2a              ,
    bleedPrsovFbk_1a=           data.bleedPrsovFbk_1a              ,
    bleedPrsovFbk_1b=           data.bleedPrsovFbk_1b              ,
    bleedPrsovFbk_2b=           data.bleedPrsovFbk_2b              ,
    flightMinutes=              data.flightMinutes             ,
    message0418DAA_1=           data.message0418DAA_1              ,
    message0422DAA_1=           data.message0422DAA_1              ,
    aircraftSerNum_1=           data.aircraftSerNum_1     )         

@router.get("/dashboard")
async def get_dashboard(payload: dict):
    if payload["serial"]:
        return await controller_get_dashboard(serial=payload["serial"])
    else:
        raise HTTPException(status_code=400, detail="Invalid parameters, try 'serial' like the aircraftSerialNumber")

@router.get("/airplane")
async def get_airplane(payload: dict):
    if payload["serial"]:
        return await controller_get_airplane_by_serial(serial=payload["serial"])
    else:
        raise HTTPException(
            status_code=400, detail="Invalid Parameters, try 'serial' like the aircraftSerialNumber"
        )

@router.get("/flights")
async def get_flights_by_serial(payload: dict):
    if payload["serial"]:
        return await controller_get_flights_by_serial(serial=payload["serial"])
    else:
        raise HTTPException(status_code=400, detail="Invalid Parameters, try 'serial' like the aircraftSerialNumber")
        
        
@router.get("/predictions")
async def get_predictions(payload: dict):
    if payload["serial"]:
        return await controller_get_predictions(serial=payload["serial"])
    else:
        raise HTTPException(status_code=400, detail="Invalid Parameters, try 'serial' like the aircraftSerialNumber")
