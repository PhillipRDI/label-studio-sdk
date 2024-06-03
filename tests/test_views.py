# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = [
        {
            "id": 1,
            "filter_group": {
                "id": 1,
                "filters": [{"column": "column", "type": "type", "operator": "operator"}],
                "conjunction": "conjunction",
            },
            "data": {"data": {"key": "value"}},
            "ordering": {"ordering": {"key": "value"}},
            "selected_items": {"selected_items": {"key": "value"}},
            "user": 1,
            "project": 1,
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "id": "integer",
                "filter_group": {
                    "id": "integer",
                    "filters": ("list", {0: {"column": None, "type": None, "operator": None}}),
                    "conjunction": None,
                },
                "data": ("dict", {0: (None, None)}),
                "ordering": ("dict", {0: (None, None)}),
                "selected_items": ("dict", {0: (None, None)}),
                "user": "integer",
                "project": "integer",
            }
        },
    )
    response = client.views.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.views.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "filter_group": {
            "id": 1,
            "filters": [{"column": "column", "type": "type", "operator": "operator"}],
            "conjunction": "conjunction",
        },
        "data": {"data": {"key": "value"}},
        "ordering": {"ordering": {"key": "value"}},
        "selected_items": {"selected_items": {"key": "value"}},
        "user": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "filter_group": {
            "id": "integer",
            "filters": ("list", {0: {"column": None, "type": None, "operator": None}}),
            "conjunction": None,
        },
        "data": ("dict", {0: (None, None)}),
        "ordering": ("dict", {0: (None, None)}),
        "selected_items": ("dict", {0: (None, None)}),
        "user": "integer",
        "project": "integer",
    }
    response = client.views.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.views.create()
    validate_response(async_response, expected_response, expected_types)


async def test_delete_all(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.views.delete_all(project=1) is None  # type: ignore[func-returns-value]

    assert await async_client.views.delete_all(project=1) is None  # type: ignore[func-returns-value]


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "filter_group": {
            "id": 1,
            "filters": [{"column": "column", "type": "type", "operator": "operator"}],
            "conjunction": "conjunction",
        },
        "data": {"data": {"key": "value"}},
        "ordering": {"ordering": {"key": "value"}},
        "selected_items": {"selected_items": {"key": "value"}},
        "user": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "filter_group": {
            "id": "integer",
            "filters": ("list", {0: {"column": None, "type": None, "operator": None}}),
            "conjunction": None,
        },
        "data": ("dict", {0: (None, None)}),
        "ordering": ("dict", {0: (None, None)}),
        "selected_items": ("dict", {0: (None, None)}),
        "user": "integer",
        "project": "integer",
    }
    response = client.views.get(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.views.get(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.views.delete(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.views.delete(id="id") is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "filter_group": {
            "id": 1,
            "filters": [{"column": "column", "type": "type", "operator": "operator"}],
            "conjunction": "conjunction",
        },
        "data": {"data": {"key": "value"}},
        "ordering": {"ordering": {"key": "value"}},
        "selected_items": {"selected_items": {"key": "value"}},
        "user": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "filter_group": {
            "id": "integer",
            "filters": ("list", {0: {"column": None, "type": None, "operator": None}}),
            "conjunction": None,
        },
        "data": ("dict", {0: (None, None)}),
        "ordering": ("dict", {0: (None, None)}),
        "selected_items": ("dict", {0: (None, None)}),
        "user": "integer",
        "project": "integer",
    }
    response = client.views.update(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.views.update(id="id")
    validate_response(async_response, expected_response, expected_types)