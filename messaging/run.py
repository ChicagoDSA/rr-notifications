from settings import r
from datetime import datetime
from twilio.rest import Client
import sys
import json
import asyncio

#TODO: These needs to be an ENV variable passed via docker
channel = sys.argv[1]
secs_per_msg = int(sys.argv[2])
account_sid = sys.argv[3]
auth_token =  sys.argv[4]

client = Client(account_sid, auth_token)

pubsub = r.pubsub(ignore_subscribe_messages=True)
pubsub.subscribe(channel)

messages = asyncio.Queue()

print ('Listening to the channel')


async def producer():
    while True:
        data = pubsub.get_message()
        if data:
            if data['type'] == 'message':
                message = data['data']
                await messages.put(message)
        else:
            await asyncio.sleep(1)


async def consumer(io):
    last_at = datetime.now()
    while True:
        message = await messages.get()
        diff = secs_per_msg - (datetime.now() - last_at).seconds
        if diff > 0:
            await asyncio.sleep(diff)

        task = asyncio.ensure_future(io.run_in_executor(None, messager, message))
        await asyncio.wait([task])
        last_at = datetime.now()


def messager(info):
    info = json.loads(info)
    message = client.messages.create(
        body = info['message'],
        # TODO: Forgot what this was
        from_ = 'MG7a6f7258ae5f997a493ac29648309fb9',
        to = info['number']
    )
    print(message.sid)


loop = asyncio.get_event_loop()
loop.create_task(producer())
loop.create_task(consumer(loop))

loop.run_forever()
