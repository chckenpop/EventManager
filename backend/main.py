from fastapi import FastAPI
from App.routes.auth import router as auth_router
# from App.routes.event_routes import router as event_router

app = FastAPI()

app.include_router(auth_router, prefix = "/auth")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}
