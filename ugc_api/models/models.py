import datetime
import uuid

import orjson
from pydantic import BaseModel


def orjson_dumps(val, *, default):
    return orjson.dumps(val, default=default).decode()


class MyBaseModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps

 
class FilmTimeStamp(MyBaseModel):
    jwt: str
    film_id: uuid.UUID
    film_timestamp: datetime.datetime
    event_time: datetime.datetime


class KafkaFilmTimeStamp(MyBaseModel):
    user_id: uuid.UUID
    film_id: uuid.UUID
    film_timestamp: datetime.datetime
    event_time: datetime.datetime
    