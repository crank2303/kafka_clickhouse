import asyncio
import datetime
import uuid

import aiohttp
import jwt
import pytest
from aiohttp.client import ClientSession


@pytest.fixture(scope='session')
async def aio_client() -> ClientSession:
    client = aiohttp.ClientSession()
    yield client
    await client.close()


@pytest.fixture(scope='session')
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def make_post_request(aio_client: ClientSession):
    async def inner(url, headers, body):
        resp_dict = dict()
        async with aio_client.post(url, headers=headers, json=body) as response:
            resp_dict['body'] = await response.json()
            resp_dict['headers'] = response.headers
            resp_dict['status'] = response.status
        return resp_dict
    return inner


@pytest.fixture
def create_token():
    token = jwt.encode(dict(
        user_id=str(uuid.uuid4()),
        exp=datetime.datetime.now() + datetime.timedelta(minutes=5),
        iat=datetime.datetime.now(),
    ),
        f'qwerty',
    )
    return token.decode('utf-8')
