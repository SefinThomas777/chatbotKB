import { useState } from 'react';
import { TextField, Button, List, Typography, Box } from '@mui/material';
import Message from './Message';
import SuggestedQuery from './SuggestedQuery';
import { sendQuery } from '../services/api';

interface ChatInterfaceProps {
  messages: string[];
  setMessages: (messages: string[]) => void;
}

export default function ChatInterface({ messages, setMessages }: ChatInterfaceProps) {
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState<string[]>([]);

  const handleSend = async () => {
    try {
      const endpoint = query.toLowerCase().includes('appointment') ? '/appointment' : '/query';
      const response = await sendQuery(query, endpoint);
      setMessages([...messages, `User: ${query}`, `Bot: ${response.answer}`]);
      setSuggestions(response.suggestions || []);
      setQuery('');
    } catch (error) {
      setMessages([...messages, `User: ${query}`, `Bot: Error occurred.`]);
    }
  };

  return (
    <Box sx={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <Typography variant="h4" gutterBottom>Chatbot</Typography>
      <List>
        {messages.map((msg, idx) => (
          <Message key={idx} text={msg} />
        ))}
      </List>
      <TextField
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        fullWidth
        label="Type your query"
        variant="outlined"
        sx={{ marginBottom: '10px' }}
      />
      <Button onClick={handleSend} variant="contained" color="primary">
        Send
      </Button>
      <Typography variant="h6" sx={{ marginTop: '20px' }}>Suggestions:</Typography>
      <List>
        {suggestions.map((sug, idx) => (
          <SuggestedQuery key={idx} text={sug} onClick={() => { setQuery(sug); handleSend(); }} />
        ))}
      </List>
    </Box>
  );
}