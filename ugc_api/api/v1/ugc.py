from http import HTTPStatus

from fastapi import APIRouter, Depends
from models.models import FilmTimeStamp


router = APIRouter()


@router.post('/film-timestamp/')
async def film_timestamp(
    film_timestamp: FilmTimeStamp,
) -> HTTPStatus.OK:
    await kafka_event_sender.post_event(topic='film_timestamp', event_obj=film_timestamp)
    return HTTPStatus.OK