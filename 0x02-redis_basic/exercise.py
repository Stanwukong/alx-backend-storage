#!/usr/bin/env python3
"""
Writing strings to Redis with a cache class.
"""
import redis
import uuid
from typing import Union


class Cache:
    """A simple Cache class for interacting with Redis."""

    def __init__(self):
        """Initializes Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """
        Store data in Redis with randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

     def get(self, 
             key: str, 
             fn: Callable = None
             ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and apply a conversion
            function.
        """
        value = self._redis.get(key)
        if value is None:
            return None

        return fn(value) if fn else value

    def get_str(self, key) -> str:
        """Retrieve a string valie from Redis."""
        return self.get(key, lambda d: d:decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer values from Redis."""
        return self.get(key, lambda x: int(x))
