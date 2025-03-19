import redis
from dotenv import load_dotenv
import os

load_dotenv()

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0
        )

    def get(self, key: str) -> str | None:
        value = self.client.get(key)
        return value.decode() if value else None

    def set(self, key: str, value: str):
        self.client.set(key, value)