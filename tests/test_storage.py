# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio


async def test_api_storages_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.storage.api_storages_list() is None  # type: ignore[func-returns-value]

    assert await async_client.storage.api_storages_list() is None  # type: ignore[func-returns-value]


async def test_api_storages_export_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.storage.api_storages_export_list() is None  # type: ignore[func-returns-value]

    assert await async_client.storage.api_storages_export_list() is None  # type: ignore[func-returns-value]


async def test_api_storages_export_types_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.storage.api_storages_export_types_list() is None  # type: ignore[func-returns-value]

    assert await async_client.storage.api_storages_export_types_list() is None  # type: ignore[func-returns-value]


async def test_api_storages_types_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.storage.api_storages_types_list() is None  # type: ignore[func-returns-value]

    assert await async_client.storage.api_storages_types_list() is None  # type: ignore[func-returns-value]
