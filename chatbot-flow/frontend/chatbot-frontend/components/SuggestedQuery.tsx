import { ListItem } from '@mui/material';

interface SuggestedQueryProps {
  text: string;
  onClick: () => void;
}

export default function SuggestedQuery({ text, onClick }: SuggestedQueryProps) {
  return <ListItem onClick={onClick} sx={{ cursor: 'pointer' }}>{text}</ListItem>;
}