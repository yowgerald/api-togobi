from fastapi import FastAPI
from routers.v1 import profile_router
from routers.v1 import signer_router

app = FastAPI()

PREFIX_V1 = "/api/v1"

app.include_router(profile_router.router, prefix=PREFIX_V1 + "/profile")
app.include_router(signer_router.router, prefix=PREFIX_V1)

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.app_port)
