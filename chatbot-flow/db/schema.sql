CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    query TEXT NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE knowledge_base (
    id SERIAL PRIMARY KEY,
    query TEXT NOT NULL,
    answer TEXT NOT NULL,
    vector TEXT NOT NULL
);

CREATE TABLE suggested_queries (
    id SERIAL PRIMARY KEY,
    query TEXT NOT NULL,
    related_query TEXT NOT NULL
);