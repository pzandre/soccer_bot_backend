import aioredis
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis_context_manager import RedisContextManager
from starlette.requests import Request
from starlette.responses import Response

from data_analysis_soccer import lambda_function

app = FastAPI()


@cache()
async def get_cache():
    return 1


@app.get("/")
# @cache(expire=180)
async def index(request: Request, response: Response):
    with RedisContextManager() as redis_connection:
        cached_results = redis_connection.lrange("cached_results", 0, -1)
    return cached_results


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://127.0.0.1:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


def cache_response() -> None:
    response = lambda_function.lambda_handler("event", "handler")
    with RedisContextManager() as redis_connection:
        redis_connection.lpop("cached_results")
        redis_connection.lpush("cached_results", response)


@app.on_event("startup")
@repeat_every(seconds=60 * 3)  # 3 minutes
def cache_response_task() -> None:
    cache_response()
