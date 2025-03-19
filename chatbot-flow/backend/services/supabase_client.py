from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
Base = declarative_base()
engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    query = Column(String)
    answer = Column(Text)

class KnowledgeBase(Base):
    __tablename__ = 'knowledge_base'
    id = Column(Integer, primary_key=True)
    query = Column(String)
    answer = Column(Text)
    vector = Column(Text)

class SuggestedQuery(Base):
    __tablename__ = 'suggested_queries'
    id = Column(Integer, primary_key=True)
    query = Column(Text)
    related_query = Column(Text)

def init_db():
    Base.metadata.create_all(engine)

def save_conversation(query: str, answer: str):
    session = Session()
    convo = Conversation(query=query, answer=answer)
    session.add(convo)
    session.commit()
    session.close()

def get_knowledge_base():
    session = Session()
    results = session.query(KnowledgeBase).all()
    session.close()
    return results

def get_suggestions(query: str):
    session = Session()
    results = session.query(SuggestedQuery).filter(SuggestedQuery.related_query.ilike(f"%{query}%")).limit(3).all()
    session.close()
    return [r.query for r in results] or ["What’s your name?", "How can I help?", "Book an appointment"]