from fastapi import FastAPI

# Send request from the from end to backend
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

