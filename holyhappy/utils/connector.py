import redis
import os
from django.conf import settings


class RedisConnector:
    def __init__(self):
        self.redisCache = {'host': os.environ.get('REDIS_HOST', settings.REDIS_HOST),
                           'port': os.environ.get('REDIS_PORT', settings.REDIS_PORT)}

    def get_redis_cache(self):
        client = redis.Redis(host=self.redisCache['host'], port=self.redisCache['port'])
        return client