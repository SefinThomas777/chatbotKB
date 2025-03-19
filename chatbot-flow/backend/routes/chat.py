from fastapi import APIRouter
from models import Query
from services.redis_client import RedisClient
from services.supabase_client import save_conversation, get_knowledge_base, get_suggestions
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

router = APIRouter()
redis_client = RedisClient()
model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)

faq = {
    "hello": "Hi there! How can I assist you?",
    "help": "I’m here to help. What do you need?"
}

def load_faiss_index():
    kb_entries = get_knowledge_base()
    if kb_entries:
        vectors = np.array([np.fromstring(entry.vector, dtype=np.float32) for entry in kb_entries])
        index.add(vectors)

load_faiss_index()

@router.post("/query")
async def process_query(query: Query):
    cached_response = redis_client.get(query.query)
    if cached_response:
        return {"answer": cached_response, "suggestions": get_suggestions(query.query)}

    if query.query.lower() in faq:
        answer = faq[query.query.lower()]
    else:
        query_vector = model.encode(query.query).reshape(1, -1).astype('float32')
        D, I = index.search(query_vector, 1)
        if I[0][0] != -1 and D[0][0] < 1.0:
            kb_entries = get_knowledge_base()
            answer = kb_entries[I[0][0]].answer
        else:
            answer = "Sorry, I don’t have an answer for that."

    redis_client.set(query.query, answer)
    save_conversation(query.query, answer)
    suggestions = get_suggestions(query.query)
    return {"answer": answer, "suggestions": suggestions}