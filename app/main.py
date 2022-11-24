""" Main Module """

import datetime
import uvicorn
from uuid import uuid4
from fastapi import (
    FastAPI,
    Depends,
)

app = FastAPI()

# from .dependencies import get_query_token, get_token_header
from routers import devices, users

# app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(devices.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)