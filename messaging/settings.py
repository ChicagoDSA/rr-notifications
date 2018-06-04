import redis

# TODO: The host and port need to be env variables that are passed via docker
config = {
    'host': '0.0.0.0',
    'port': 6379,
    'db': 0,
    "charset": "utf-8",
    "decode_responses": True
}

r = redis.StrictRedis(**config)
