""" The code is importing the necessary modules and routers for the FastAPI application. """
from fastapi import FastAPI
import uvicorn
from config import app_settings
from routers.v1 import file_router
from routers.v1 import signer_router

app = FastAPI()

PREFIX_V1 = "/api/v1"

app.include_router(file_router.router, prefix=PREFIX_V1)
app.include_router(signer_router.router, prefix=PREFIX_V1)

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=app_settings.app_port)
