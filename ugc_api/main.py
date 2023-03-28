import socket

from aiokafka import AIOKafkaProducer
from api.v1 import ugc
from core.config import settings
from db import kafka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from svc import event_producer, event_sendler

from kafka import KafkaAdminClient

app = FastAPI(
    title=settings.project_name,
    docs_url="/api/docs",
    openapi_url="/api/docs.json",
    default_response_class=ORJSONResponse,
    debug=settings.debug,
)


@app.on_event("startup")
async def startup():
    kafka.kafka_admin = KafkaAdminClient(
        bootstrap_servers=f"{settings.kafka_host}:{settings.kafka_port}", client_id=socket.gethostname()
    )
    kafka.kafka_producer = AIOKafkaProducer(
        bootstrap_servers=[f"{settings.kafka_host}:{settings.kafka_port}"], client_id=socket.gethostname()
    )
    await kafka.kafka_producer.start()
    event_producer.kafka_event_producer = event_producer.KafkaEventProducer(
        event_producer=kafka.kafka_producer,
        kafka_admin=kafka.kafka_admin,
        topics=set(
            "film_timestamp",
        ),
    )
    event_sendler.kafka_event_sendler = event_sendler.KafkaEventSendler(
        event_producer=event_producer.kafka_event_producer
    )


@app.on_event("shutdown")
async def shutdown():
    await kafka.kafka_producer.stop()
    kafka.kafka_admin.close()


app.include_router(ugc.router, prefix=f"/api/{settings.api_version}/films", tags=["ugc"])
