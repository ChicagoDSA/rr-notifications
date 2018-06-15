from settings import get_client
from datetime import datetime
from twilio.rest import Client
import json
import asyncio
import os
import time

#TODO use the config parser class for this
channel = os.environ['REDIS_CHANNEL']
secs_per_msg = int(os.environ['SECS_PER_MSG'])
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
from_account = os.environ['FROM_ACCOUNT']
redis_server = os.environ['REDIS_SERVER']

client = Client(account_sid, auth_token)
pubsub = get_client(redis_server).pubsub(ignore_subscribe_messages=True)
pubsub.subscribe(channel)

messages = asyncio.Queue()

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
    # TODO: add error handling if parsing or sending a message fails
    info = json.loads(info)
    message = client.messages.create(
        body = info['message'],
        from_ = from_account,
        to = info['number']
    )


loop = asyncio.get_event_loop()
loop.create_task(producer())
loop.create_task(consumer(loop))

loop.run_forever()
