from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
queries = ["What is this chatbot?", "How do I use it?"]
vectors = [model.encode(q).tobytes().hex() for q in queries]
for q, v in zip(queries, vectors):
    print(f"('{q}', 'I’m HSJB chatbot!' or 'Just type your question!', '{v}'),")
