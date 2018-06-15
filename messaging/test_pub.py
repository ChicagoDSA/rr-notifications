from settings import get_client
from datetime import datetime
import json
import sys

if __name__ == '__main__':
    channel = sys.argv[1]
    amount = int(sys.argv[2])
    number = sys.argv[3]
    r = get_client('0.0.0.0')

    #test normal message
    for i in range(0, amount):
        message = {
            "message": "message#: " + str(i) + ". Message sent at " + str(datetime.now()),
            "number": number
        }
        r.publish(channel, json.dumps(message))
