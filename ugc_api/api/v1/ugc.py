from http import HTTPStatus

from fastapi import APIRouter, Depends

from models.models import FilmTimeStamp
from svc.event_sendler import KafkaEventSendler, get_kafka_event_sendler
from auth.auth_bearer import JWTBearer

router = APIRouter()


@router.post("/film-timestamp/", dependencies=[Depends(JWTBearer())])
async def film_timestamp(film_timestamp: FilmTimeStamp,
                         kafka_event_sendler: KafkaEventSendler = Depends(get_kafka_event_sendler)) -> HTTPStatus.OK:
    await kafka_event_sendler.post_event(topic="film_timestamp", event_obj=film_timestamp)
    return HTTPStatus.OK
