import { ListItem } from '@mui/material';

interface MessageProps {
  text: string;
}

export default function Message({ text }: MessageProps) {
  return <ListItem>{text}</ListItem>;
}