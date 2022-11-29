from fastapi import APIRouter, Body, Depends, HTTPException, status
from database.model import Device
from routers.users import get_decoded_token
from database.setup import device_collection
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/devices/add", tags=["add_devices"], status_code=201)
async def add_device(device: Device = Body(default=None), token: str = Depends(get_decoded_token)):
    device_dict = {
        "owner": token['sub'],
        "name": device.name,
        "quantity": device.quantity,
        "description": device.description,
        "power_rated": device.power_rated,
    }
    device_collection.insert_one(device_dict)
    raise HTTPException(status_code=status.HTTP_201_CREATED, 
                            detail = f'{device.quantity} of device/devices added!')

@router.get("/devices/show", tags=["show_devices"], status_code=201)
async def show_devices(token: str = Depends(get_decoded_token)):
    username= token['sub']
    user = device_collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No Device found under this {username} username')
    else:
        return JSONResponse()