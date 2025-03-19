from fastapi import APIRouter
from models import Query
from services.calendly_client import CalendlyClient
from services.supabase_client import save_conversation, get_suggestions

router = APIRouter()
calendly_client = CalendlyClient()

@router.post("/appointment")
async def book_appointment(query: Query):
    if "appointment" in query.query.lower():
        link = calendly_client.get_booking_link()
        if link:
            answer = f"Book here: {link}"
        else:
            answer = "Error generating appointment link."
    else:
        answer = "No appointment detected."
    save_conversation(query.query, answer)
    suggestions = get_suggestions(query.query)
    return {"answer": answer, "suggestions": suggestions}