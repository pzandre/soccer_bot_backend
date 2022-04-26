import redis


class RedisContextManager:
    def __init__(self):
        pool = redis.ConnectionPool(
            host="127.0.0.1", port=6379, db="0", decode_responses=True
        )
        self.r = redis.Redis(connection_pool=pool)

    def __enter__(self):
        return self.r

    def __exit__(self, exc_type, exc_value, traceback):
        self.r.close()
