""" The code is importing the necessary modules and routers for the FastAPI application. """
from fastapi import FastAPI
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from firebase_admin import credentials
import firebase_admin

from config import app_settings
from middlewares.auth_middleware import AuthMiddleware
from routers.v1 import file_router
from routers.v1 import signer_router
from routers.v1 import gpt_router
from routers.v1 import ai21_router

app = FastAPI()

# initialize firebase
cred = credentials.Certificate(app_settings.firebase_credentials)
firebase_admin.initialize_app(cred)

# add middleware
if app_settings.app_env != "local":
    auth_middleware = AuthMiddleware()
    app.add_middleware(BaseHTTPMiddleware, dispatch=auth_middleware)

PREFIX_V1 = "/api/v1"

PREFIX_AI21 = "/ai21"

app.include_router(file_router.router, prefix=PREFIX_V1)
app.include_router(signer_router.router, prefix=PREFIX_V1)
app.include_router(gpt_router.router, prefix=PREFIX_V1)
app.include_router(ai21_router.router, prefix=PREFIX_V1 + PREFIX_AI21)

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=app_settings.app_port)
