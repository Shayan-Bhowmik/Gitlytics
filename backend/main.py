# making imports
from fastapi import FastAPI

# fastapi app instance
app = FastAPI()

# GET route 
@app.get("/health")
def health_check():
    return {"status": "ok"}