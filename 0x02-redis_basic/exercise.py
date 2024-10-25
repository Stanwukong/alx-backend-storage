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
        self._redis.flushdb()

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """
        Store data in Redis with randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
