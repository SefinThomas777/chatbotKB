from fastapi import FastAPI
from routes.chat import router as chat_router
from routes.meeting import router as meeting_router
from services.supabase_client import init_db
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

app.include_router(chat_router)
app.include_router(meeting_router)

@app.on_event("startup")
async def startup_event():
    init_db()