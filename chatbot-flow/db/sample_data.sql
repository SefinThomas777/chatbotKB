INSERT INTO knowledge_base (query, answer, vector) VALUES
('What is this chatbot?', 'I’m a helpful chatbot!', '<paste-vector-hex-here>'),
('How do I use it?', 'Just type your question!', '<paste-vector-hex-here>');

INSERT INTO suggested_queries (query, related_query) VALUES
('Tell me more', 'What is this chatbot?'),
('How does it work?', 'How do I use it?'),
('Schedule a call', 'appointment');