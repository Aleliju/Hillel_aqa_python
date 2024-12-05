import logging

import pytest

from .auth import APISession
from .base_url import BASE_URL, USERNAME, PASSWORD, CARS_ENDPOINT

@pytest.fixture(scope='session')
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
    file_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


@pytest.fixture(scope='class')
def authenticated_session():
    with APISession(BASE_URL, USERNAME, PASSWORD) as api_session:
        yield api_session

@pytest.mark.parametrize("params, expected_keys, expected_count", [
    ({"sort_by": "brand", "limit": 5}, ["brand"], 5),
    ({"sort_by": "price", "limit": 3}, ["price"], 3),
    ({"sort_by": "non_existent_field", "limit": 2}, [], 2),
    ({"sort_by": None, "limit": None}, ["brand"], 25),
    ({"sort_by": "year", "limit": 0}, ["year"], 0),
    ({"sort_by": "price", "limit": 50}, ["price"], 25),
])

def test_get_request(authenticated_session, params, expected_keys, expected_count, logger):
    logger.info(f"Starting test with params: {params}")
    response = authenticated_session.get(CARS_ENDPOINT, params=params)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    logger.info(f"Response data length: {len(data)}")

    assert len(data) == expected_count
    logger.info("Count check passed.")

    sort_by = params.get("sort_by")
    if sort_by and sort_by in expected_keys:
        assert data == sorted(data, key=lambda x: x[sort_by])
        logger.info(f"Sorting check passed for field: {sort_by}")

    limit = params.get("limit")
    if isinstance(limit, int) and limit >= 0:
        assert len(data) <= limit
        logger.info("Limit check passed.")

