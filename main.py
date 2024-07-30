from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router  # Import the router

app = FastAPI()

# Allow CORS for all origins for simplicity. Adjust this in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(router)

