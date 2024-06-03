# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk import Label, LabelCreate
from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "count": 1,
        "next": "next",
        "previous": "previous",
        "results": [
            {
                "id": 1,
                "links": [1],
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-15T09:30:00Z",
                "value": {},
                "title": "title",
                "description": "description",
                "approved": True,
                "created_by": 1,
                "approved_by": 1,
                "organization": 1,
                "projects": [1],
            }
        ],
    }
    expected_types: typing.Any = {
        "count": "integer",
        "next": None,
        "previous": None,
        "results": (
            "list",
            {
                0: {
                    "id": "integer",
                    "links": ("list", {0: "integer"}),
                    "created_at": "datetime",
                    "updated_at": "datetime",
                    "value": ("dict", {}),
                    "title": None,
                    "description": None,
                    "approved": None,
                    "created_by": "integer",
                    "approved_by": "integer",
                    "organization": "integer",
                    "projects": ("list", {0: "integer"}),
                }
            },
        ),
    }
    response = client.labels.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.labels.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = [
        {
            "id": 1,
            "created_by": 1,
            "organization": 1,
            "project": 1,
            "from_name": "from_name",
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-15T09:30:00Z",
            "value": {"value": {"key": "value"}},
            "title": "title",
            "description": "description",
            "approved": True,
            "approved_by": 1,
            "projects": [1],
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "id": "integer",
                "created_by": "integer",
                "organization": "integer",
                "project": "integer",
                "from_name": None,
                "created_at": "datetime",
                "updated_at": "datetime",
                "value": ("dict", {0: (None, None)}),
                "title": None,
                "description": None,
                "approved": None,
                "approved_by": "integer",
                "projects": ("list", {0: "integer"}),
            }
        },
    )
    response = client.labels.create(request=[LabelCreate(project=1, from_name="from_name", value={}, title="title")])
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.labels.create(
        request=[LabelCreate(project=1, from_name="from_name", value={}, title="title")]
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "links": [1],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "value": {"value": {"key": "value"}},
        "title": "title",
        "description": "description",
        "approved": True,
        "created_by": 1,
        "approved_by": 1,
        "organization": 1,
        "projects": [1],
    }
    expected_types: typing.Any = {
        "id": "integer",
        "links": ("list", {0: "integer"}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "value": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "approved": None,
        "created_by": "integer",
        "approved_by": "integer",
        "organization": "integer",
        "projects": ("list", {0: "integer"}),
    }
    response = client.labels.get(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.labels.get(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.labels.delete(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.labels.delete(id="id") is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "links": [1],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "value": {"value": {"key": "value"}},
        "title": "title",
        "description": "description",
        "approved": True,
        "created_by": 1,
        "approved_by": 1,
        "organization": 1,
        "projects": [1],
    }
    expected_types: typing.Any = {
        "id": "integer",
        "links": ("list", {0: "integer"}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "value": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "approved": None,
        "created_by": "integer",
        "approved_by": "integer",
        "organization": "integer",
        "projects": ("list", {0: "integer"}),
    }
    response = client.labels.update(id="id", request=Label(value={}, title="title", created_by=1, organization=1))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.labels.update(
        id="id", request=Label(value={}, title="title", created_by=1, organization=1)
    )
    validate_response(async_response, expected_response, expected_types)