from fastapi import HTTPException
from clerk_backend_api import Clerk, AuthenticateRequestOptions
import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the program
load_dotenv()

# Create a Clerk client object using the secret key stored in the environment
# This object allows us to interact with Clerk for authentication
clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

# Define a function to authenticate a request and get user details
def authenticate_and_get_user_details(request):
    try:
        #   - authorized_parties: which frontend URLs are allowed to make requests
        #   - jwt_key: the public key to verify the token locally
        request_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=["http://localhost:5173", "http://localhost:5174"],
                jwt_key=os.getenv("JWT_KEY")
            )
        )

        if not request_state.is_signed_in:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = request_state.payload.get("sub")

        return {"user_id": user_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
