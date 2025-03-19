# Setup Guide
1. **Clone Repo**: `git clone <url>`
2. **Run Locally**:
   - Start services: `docker-compose up -d`
   - Frontend: `cd frontend/chatbot-frontend && npm install && npm run dev`
   - Backend: `cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && uvicorn main:app --reload`
3. **Populate DB**:
   - Generate vectors: Run the vector script (see README).
   - Load schema and data: `docker exec -i <supabase-container-id> psql -U postgres -d postgres < db/schema.sql` and `< db/sample_data.sql`
4. **Configure .env**:
   - Frontend: `NEXT_PUBLIC_API_URL`
   - Backend: `DATABASE_URL`, `REDIS_HOST`, `CALENDLY_API_TOKEN`
5. **Access**: Frontend at `http://localhost:3000`, Backend at `http://localhost:8000`
6. **Production**: `docker-compose -f docker-compose.prod.yml up -d`, configure Cloudflare.