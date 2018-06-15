import redis

# TODO: The host and port need to be env variables that are passed via docker


def get_client(host):
    config = {
        'host': host,
        'port': 6379,
        'db': 0,
        "charset": "utf-8",
        "decode_responses": True
    }

    return redis.StrictRedis(**config)
