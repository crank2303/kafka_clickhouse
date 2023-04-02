from http import HTTPStatus

import pytest


@pytest.mark.asyncio
async def test_films_list(make_post_request, create_token):
    headers = {'Authorization': f'Bearer {create_token}'}
    body = {
        'jwt': f'{create_token}',
        'film_id': '3fa85f64-5717-4562-b3fc-2c963f66afa0',
        'film_timestamp': '2023-04-01T10:58:07.196Z',
        'event_time': '2023-04-01T10:58:07.196Z'
    }
    response = await make_post_request(f'http://localhost:8000/api/v1/films/film-timestamp/', headers, body)
    assert response['status'] == HTTPStatus.OK
