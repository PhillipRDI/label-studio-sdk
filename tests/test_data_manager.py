# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_api_dm_columns_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.data_manager.api_dm_columns_list() is None  # type: ignore[func-returns-value]

    assert await async_client.data_manager.api_dm_columns_list() is None  # type: ignore[func-returns-value]


async def test_api_dm_project_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.data_manager.api_dm_project_list() is None  # type: ignore[func-returns-value]

    assert await async_client.data_manager.api_dm_project_list() is None  # type: ignore[func-returns-value]


async def test_api_dm_views_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {"data": {"filters": {"conjunction": "and", "items": [{}]}, "ordering": [{}]}, "project": 1}
    expected_types: typing.Any = {
        "data": {"filters": {"conjunction": None, "items": ("list", {0: {}})}, "ordering": ("list", {0: {}})},
        "project": "integer",
    }
    response = client.data_manager.api_dm_views_update(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.data_manager.api_dm_views_update(id="id")
    validate_response(async_response, expected_response, expected_types)