""" The `from` statements are importing various modules and classes """
from fastapi import Request
from fastapi.responses import JSONResponse
from firebase_admin import auth, credentials
import firebase_admin
from config import app_settings

cred = credentials.Certificate(app_settings.firebase_credentials)
firebase_admin.initialize_app(cred)


class AuthMiddleware:
    """
    The AuthMiddleware class is used for handling authentication in a Python web application.
    """

    async def __call__(self, request: Request, call_next):
        try:
            auth_token = request.headers.get("AuthToken")

            if not auth_token:
                # Return a JSON response with an error message if AuthToken header is missing
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Authorization token not provided."},
                )

            auth.verify_id_token(auth_token)

            # process the request and get the response
            response = await call_next(request)

            return response
        except ValueError as error:
            # Handle authentication-related errors
            return JSONResponse(
                status_code=401,
                content={"detail": "Authentication error: " + str(error)},
            )
        except Exception as error:
            # Handle other unexpected errors
            return JSONResponse(
                status_code=500,
                content={"detail": "An error occurred: " + str(error)},
            )
