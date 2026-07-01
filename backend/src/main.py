from fastapi import FastAPI
from routers import leads, activities

app = FastAPI(title="LeadFlow API", description="API for managing leads and activities", version="1.0.0")

app.include_router(leads.router, prefix="/api/leads", tags=["Leads"])
app.include_router(activities.router, prefix="/api/activities", tags=["Activities"])


@app.get("/")
def home():
    """
    Root endpoint that returns a simple greeting message.
    """
    return {"message": "Hello, World!"}

