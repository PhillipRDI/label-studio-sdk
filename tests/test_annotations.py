# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "result": [
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        "created_username": "created_username",
        "created_ago": "created_ago",
        "completed_by": {"completed_by": {"key": "value"}},
        "unique_id": "unique_id",
        "was_cancelled": False,
        "ground_truth": False,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "draft_created_at": "2024-01-15T09:30:00Z",
        "lead_time": 10,
        "import_id": 1,
        "last_action": "prediction",
        "task": 1,
        "project": 1,
        "updated_by": 1,
        "parent_prediction": 1,
        "parent_annotation": 1,
        "last_created_by": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "result": (
            "list",
            {
                0: (
                    "dict",
                    {
                        0: (None, None),
                        1: (None, None),
                        2: (None, None),
                        3: (None, None),
                        4: (None, None),
                        5: (None, None),
                        6: (None, None),
                    },
                )
            },
        ),
        "created_username": None,
        "created_ago": None,
        "completed_by": ("dict", {0: (None, None)}),
        "unique_id": None,
        "was_cancelled": None,
        "ground_truth": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "draft_created_at": "datetime",
        "lead_time": None,
        "import_id": "integer",
        "last_action": None,
        "task": "integer",
        "project": "integer",
        "updated_by": "integer",
        "parent_prediction": "integer",
        "parent_annotation": "integer",
        "last_created_by": "integer",
    }
    response = client.annotations.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.annotations.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.annotations.delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.annotations.delete(id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "result": [
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        "created_username": "created_username",
        "created_ago": "created_ago",
        "completed_by": {"completed_by": {"key": "value"}},
        "unique_id": "unique_id",
        "was_cancelled": False,
        "ground_truth": False,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "draft_created_at": "2024-01-15T09:30:00Z",
        "lead_time": 10,
        "import_id": 1,
        "last_action": "prediction",
        "task": 1,
        "project": 1,
        "updated_by": 1,
        "parent_prediction": 1,
        "parent_annotation": 1,
        "last_created_by": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "result": (
            "list",
            {
                0: (
                    "dict",
                    {
                        0: (None, None),
                        1: (None, None),
                        2: (None, None),
                        3: (None, None),
                        4: (None, None),
                        5: (None, None),
                        6: (None, None),
                    },
                )
            },
        ),
        "created_username": None,
        "created_ago": None,
        "completed_by": ("dict", {0: (None, None)}),
        "unique_id": None,
        "was_cancelled": None,
        "ground_truth": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "draft_created_at": "datetime",
        "lead_time": None,
        "import_id": "integer",
        "last_action": None,
        "task": "integer",
        "project": "integer",
        "updated_by": "integer",
        "parent_prediction": "integer",
        "parent_annotation": "integer",
        "last_created_by": "integer",
    }
    response = client.annotations.update(
        id=1,
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        was_cancelled=False,
        ground_truth=True,
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.annotations.update(
        id=1,
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        was_cancelled=False,
        ground_truth=True,
    )
    validate_response(async_response, expected_response, expected_types)


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "id": 1,
            "result": [
                {
                    "original_width": 1920,
                    "original_height": 1080,
                    "image_rotation": 0,
                    "from_name": "bboxes",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "x": 20,
                        "y": 30,
                        "width": 50,
                        "height": 60,
                        "rotation": 0,
                        "values": {"rectanglelabels": {"0": "Person"}},
                    },
                }
            ],
            "created_username": "created_username",
            "created_ago": "created_ago",
            "completed_by": {"completed_by": {"key": "value"}},
            "unique_id": "unique_id",
            "was_cancelled": False,
            "ground_truth": False,
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-15T09:30:00Z",
            "draft_created_at": "2024-01-15T09:30:00Z",
            "lead_time": 10,
            "import_id": 1,
            "last_action": "prediction",
            "task": 1,
            "project": 1,
            "updated_by": 1,
            "parent_prediction": 1,
            "parent_annotation": 1,
            "last_created_by": 1,
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "id": "integer",
                "result": (
                    "list",
                    {
                        0: (
                            "dict",
                            {
                                0: (None, None),
                                1: (None, None),
                                2: (None, None),
                                3: (None, None),
                                4: (None, None),
                                5: (None, None),
                                6: (None, None),
                            },
                        )
                    },
                ),
                "created_username": None,
                "created_ago": None,
                "completed_by": ("dict", {0: (None, None)}),
                "unique_id": None,
                "was_cancelled": None,
                "ground_truth": None,
                "created_at": "datetime",
                "updated_at": "datetime",
                "draft_created_at": "datetime",
                "lead_time": None,
                "import_id": "integer",
                "last_action": None,
                "task": "integer",
                "project": "integer",
                "updated_by": "integer",
                "parent_prediction": "integer",
                "parent_annotation": "integer",
                "last_created_by": "integer",
            }
        },
    )
    response = client.annotations.list(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.annotations.list(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "result": [
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        "created_username": "created_username",
        "created_ago": "created_ago",
        "completed_by": {"completed_by": {"key": "value"}},
        "unique_id": "unique_id",
        "was_cancelled": False,
        "ground_truth": False,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "draft_created_at": "2024-01-15T09:30:00Z",
        "lead_time": 10,
        "import_id": 1,
        "last_action": "prediction",
        "task": 1,
        "project": 1,
        "updated_by": 1,
        "parent_prediction": 1,
        "parent_annotation": 1,
        "last_created_by": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "result": (
            "list",
            {
                0: (
                    "dict",
                    {
                        0: (None, None),
                        1: (None, None),
                        2: (None, None),
                        3: (None, None),
                        4: (None, None),
                        5: (None, None),
                        6: (None, None),
                    },
                )
            },
        ),
        "created_username": None,
        "created_ago": None,
        "completed_by": ("dict", {0: (None, None)}),
        "unique_id": None,
        "was_cancelled": None,
        "ground_truth": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "draft_created_at": "datetime",
        "lead_time": None,
        "import_id": "integer",
        "last_action": None,
        "task": "integer",
        "project": "integer",
        "updated_by": "integer",
        "parent_prediction": "integer",
        "parent_annotation": "integer",
        "last_created_by": "integer",
    }
    response = client.annotations.create(
        id=1,
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        was_cancelled=False,
        ground_truth=True,
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.annotations.create(
        id=1,
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": {"0": "Person"}},
                },
            }
        ],
        was_cancelled=False,
        ground_truth=True,
    )
    validate_response(async_response, expected_response, expected_types)
