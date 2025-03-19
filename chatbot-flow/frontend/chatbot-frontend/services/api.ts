import axios from 'axios';

export async function sendQuery(query: string, endpoint: string) {
  const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}${endpoint}`, { query });
  return response.data;
}