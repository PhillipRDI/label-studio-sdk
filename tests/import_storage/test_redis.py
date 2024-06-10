# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = [
        {
            "id": 1,
            "type": "type",
            "synchronizable": True,
            "path": "path",
            "host": "host",
            "port": "port",
            "password": "password",
            "regex_filter": "regex_filter",
            "use_blob_urls": True,
            "last_sync": "2024-01-15T09:30:00Z",
            "last_sync_count": 1,
            "last_sync_job": "last_sync_job",
            "status": "initialized",
            "traceback": "traceback",
            "meta": {"meta": {"key": "value"}},
            "title": "title",
            "description": "description",
            "created_at": "2024-01-15T09:30:00Z",
            "db": 1,
            "project": 1,
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "id": "integer",
                "type": None,
                "synchronizable": None,
                "path": None,
                "host": None,
                "port": None,
                "password": None,
                "regex_filter": None,
                "use_blob_urls": None,
                "last_sync": "datetime",
                "last_sync_count": "integer",
                "last_sync_job": None,
                "status": None,
                "traceback": None,
                "meta": ("dict", {0: (None, None)}),
                "title": None,
                "description": None,
                "created_at": "datetime",
                "db": "integer",
                "project": "integer",
            }
        },
    )
    response = client.import_storage.redis.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.redis.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "title": "title",
        "description": "description",
        "project": 1,
        "path": "path",
        "host": "host",
        "port": "port",
        "password": "password",
    }
    expected_types: typing.Any = {
        "regex_filter": None,
        "use_blob_urls": None,
        "title": None,
        "description": None,
        "project": "integer",
        "path": None,
        "host": None,
        "port": None,
        "password": None,
    }
    response = client.import_storage.redis.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.redis.create()
    validate_response(async_response, expected_response, expected_types)


async def test_validate(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.redis.validate() is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.redis.validate() is None  # type: ignore[func-returns-value]


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "host": "host",
        "port": "port",
        "password": "password",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "db": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "host": None,
        "port": None,
        "password": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "db": "integer",
        "project": "integer",
    }
    response = client.import_storage.redis.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.redis.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.redis.delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.redis.delete(id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "title": "title",
        "description": "description",
        "project": 1,
        "path": "path",
        "host": "host",
        "port": "port",
        "password": "password",
    }
    expected_types: typing.Any = {
        "regex_filter": None,
        "use_blob_urls": None,
        "title": None,
        "description": None,
        "project": "integer",
        "path": None,
        "host": None,
        "port": None,
        "password": None,
    }
    response = client.import_storage.redis.update(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.redis.update(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_sync(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "path": "path",
        "host": "host",
        "port": "port",
        "password": "password",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "db": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "path": None,
        "host": None,
        "port": None,
        "password": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "db": "integer",
        "project": "integer",
    }
    response = client.import_storage.redis.sync(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.redis.sync(id=1)
    validate_response(async_response, expected_response, expected_types)
