from celery import shared_task

from api.utils import RedisContextManager
from data_analysis_soccer.lambda_function import lambda_handler


@shared_task
def cache_matches() -> None:
    matches_json = lambda_handler()["body"]
    with RedisContextManager() as redis_connection:
        redis_connection.lpop("cached_matches")
        redis_connection.lpush("cached_matches", matches_json)

