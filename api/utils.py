import redis
from django.conf import settings


class RedisContextManager:
    def __init__(self):
        pool = redis.ConnectionPool(
            host=settings.REDIS_HOSTNAME, port=settings.REDIS_PORT, db=settings.REDIS_CACHE_DB, decode_responses=True
        )
        self.r = redis.Redis(connection_pool=pool)

    def __enter__(self):
        return self.r

    def __exit__(self, exc_type, exc_value, traceback):
        self.r.close()

