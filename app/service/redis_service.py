import json
from ..config import redis


def write_to_redis(key, value):
    redis.set(key, json.dumps(value))


def read_from_redis(key):
    return json.loads(redis.get(key))


def check_user_in_redis(username):
    return redis.exists(username)
