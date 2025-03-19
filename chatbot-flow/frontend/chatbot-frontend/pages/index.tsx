import { useState } from 'react';
import ChatInterface from '../components/ChatInterface';

export default function Home() {
  const [messages, setMessages] = useState<string[]>([]);
  return <ChatInterface messages={messages} setMessages={setMessages} />;
}