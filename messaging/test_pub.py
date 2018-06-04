from settings import r
import json
import sys

if __name__ == '__main__':
    channel = sys.argv[1]
    message = {
        "message": "hello",
        "number": "+17733176723"
    }
    r.publish(channel, json.dumps(message))
