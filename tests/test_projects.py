# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk import Project, ProjectLabelConfig
from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "title": "title",
        "description": "description",
        "label_config": "label_config",
        "expert_instruction": "expert_instruction",
        "show_instruction": True,
        "show_skip_button": True,
        "enable_empty_annotation": True,
        "show_annotation_history": True,
        "reveal_preannotations_interactively": True,
        "show_collab_predictions": True,
        "maximum_annotations": 1,
        "color": "color",
        "control_weights": {"control_weights": {"key": "value"}},
    }
    expected_types: typing.Any = {
        "title": None,
        "description": None,
        "label_config": None,
        "expert_instruction": None,
        "show_instruction": None,
        "show_skip_button": None,
        "enable_empty_annotation": None,
        "show_annotation_history": None,
        "reveal_preannotations_interactively": None,
        "show_collab_predictions": None,
        "maximum_annotations": "integer",
        "color": None,
        "control_weights": ("dict", {0: (None, None)}),
    }
    response = client.projects.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.create()
    validate_response(async_response, expected_response, expected_types)


async def test_api_projects_validate_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.projects.api_projects_validate_create(request=ProjectLabelConfig(label_config="label_config")) is None  # type: ignore[func-returns-value]

    assert await async_client.projects.api_projects_validate_create(request=ProjectLabelConfig(label_config="label_config")) is None  # type: ignore[func-returns-value]


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "title": "My project",
        "description": "My first project",
        "label_config": "<View>[...]</View>",
        "expert_instruction": "Label all cats",
        "show_instruction": True,
        "show_skip_button": True,
        "enable_empty_annotation": True,
        "show_annotation_history": True,
        "organization": 1,
        "color": "#FF0000",
        "maximum_annotations": 1,
        "is_published": True,
        "model_version": "1.0.0",
        "is_draft": False,
        "created_by": {
            "id": 1,
            "first_name": "Jo",
            "last_name": "Doe",
            "email": "manager@humansignal.com",
            "avatar": "avatar",
        },
        "created_at": "2023-08-24T14:15:22Z",
        "min_annotations_to_start_training": 0,
        "start_training_on_annotation_update": "start_training_on_annotation_update",
        "show_collab_predictions": True,
        "num_tasks_with_annotations": 10,
        "task_number": 100,
        "useful_annotation_number": 10,
        "ground_truth_number": 5,
        "skipped_annotations_number": 0,
        "total_annotations_number": 10,
        "total_predictions_number": 0,
        "sampling": "Sequential sampling",
        "show_ground_truth_first": True,
        "show_overlap_first": True,
        "overlap_cohort_percentage": 100,
        "task_data_login": "user",
        "task_data_password": "secret",
        "control_weights": {"control_weights": {"key": "value"}},
        "parsed_label_config": {"parsed_label_config": {"key": "value"}},
        "evaluate_predictions_automatically": False,
        "config_has_control_tags": "config_has_control_tags",
        "skip_queue": "REQUEUE_FOR_ME",
        "reveal_preannotations_interactively": True,
        "pinned_at": "2023-08-24T14:15:22Z",
        "finished_task_number": 10,
        "queue_total": "queue_total",
        "queue_done": "queue_done",
    }
    expected_types: typing.Any = {
        "id": "integer",
        "title": None,
        "description": None,
        "label_config": None,
        "expert_instruction": None,
        "show_instruction": None,
        "show_skip_button": None,
        "enable_empty_annotation": None,
        "show_annotation_history": None,
        "organization": "integer",
        "color": None,
        "maximum_annotations": "integer",
        "is_published": None,
        "model_version": None,
        "is_draft": None,
        "created_by": {"id": "integer", "first_name": None, "last_name": None, "email": None, "avatar": None},
        "created_at": "datetime",
        "min_annotations_to_start_training": "integer",
        "start_training_on_annotation_update": None,
        "show_collab_predictions": None,
        "num_tasks_with_annotations": "integer",
        "task_number": "integer",
        "useful_annotation_number": "integer",
        "ground_truth_number": "integer",
        "skipped_annotations_number": "integer",
        "total_annotations_number": "integer",
        "total_predictions_number": "integer",
        "sampling": None,
        "show_ground_truth_first": None,
        "show_overlap_first": None,
        "overlap_cohort_percentage": "integer",
        "task_data_login": None,
        "task_data_password": None,
        "control_weights": ("dict", {0: (None, None)}),
        "parsed_label_config": ("dict", {0: (None, None)}),
        "evaluate_predictions_automatically": None,
        "config_has_control_tags": None,
        "skip_queue": None,
        "reveal_preannotations_interactively": None,
        "pinned_at": "datetime",
        "finished_task_number": "integer",
        "queue_total": None,
        "queue_done": None,
    }
    response = client.projects.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.projects.delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.projects.delete(id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "title": "title",
        "description": "description",
        "label_config": "label_config",
        "expert_instruction": "expert_instruction",
        "show_instruction": True,
        "show_skip_button": True,
        "enable_empty_annotation": True,
        "show_annotation_history": True,
        "organization": 1,
        "color": "color",
        "maximum_annotations": 1,
        "is_published": True,
        "model_version": "model_version",
        "is_draft": True,
        "created_by": {
            "id": 1,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "avatar": "avatar",
        },
        "created_at": "2024-01-15T09:30:00Z",
        "min_annotations_to_start_training": 1,
        "start_training_on_annotation_update": "start_training_on_annotation_update",
        "show_collab_predictions": True,
        "num_tasks_with_annotations": 1,
        "task_number": 1,
        "useful_annotation_number": 1,
        "ground_truth_number": 1,
        "skipped_annotations_number": 1,
        "total_annotations_number": 1,
        "total_predictions_number": 1,
        "sampling": "Sequential sampling",
        "show_ground_truth_first": True,
        "show_overlap_first": True,
        "overlap_cohort_percentage": 1,
        "task_data_login": "task_data_login",
        "task_data_password": "task_data_password",
        "control_weights": {"control_weights": {"key": "value"}},
        "parsed_label_config": {"parsed_label_config": {"key": "value"}},
        "evaluate_predictions_automatically": True,
        "config_has_control_tags": "config_has_control_tags",
        "skip_queue": "REQUEUE_FOR_ME",
        "reveal_preannotations_interactively": True,
        "pinned_at": "2024-01-15T09:30:00Z",
        "finished_task_number": 1,
        "queue_total": "queue_total",
        "queue_done": "queue_done",
    }
    expected_types: typing.Any = {
        "id": "integer",
        "title": None,
        "description": None,
        "label_config": None,
        "expert_instruction": None,
        "show_instruction": None,
        "show_skip_button": None,
        "enable_empty_annotation": None,
        "show_annotation_history": None,
        "organization": "integer",
        "color": None,
        "maximum_annotations": "integer",
        "is_published": None,
        "model_version": None,
        "is_draft": None,
        "created_by": {"id": "integer", "first_name": None, "last_name": None, "email": None, "avatar": None},
        "created_at": "datetime",
        "min_annotations_to_start_training": "integer",
        "start_training_on_annotation_update": None,
        "show_collab_predictions": None,
        "num_tasks_with_annotations": "integer",
        "task_number": "integer",
        "useful_annotation_number": "integer",
        "ground_truth_number": "integer",
        "skipped_annotations_number": "integer",
        "total_annotations_number": "integer",
        "total_predictions_number": "integer",
        "sampling": None,
        "show_ground_truth_first": None,
        "show_overlap_first": None,
        "overlap_cohort_percentage": "integer",
        "task_data_login": None,
        "task_data_password": None,
        "control_weights": ("dict", {0: (None, None)}),
        "parsed_label_config": ("dict", {0: (None, None)}),
        "evaluate_predictions_automatically": None,
        "config_has_control_tags": None,
        "skip_queue": None,
        "reveal_preannotations_interactively": None,
        "pinned_at": "datetime",
        "finished_task_number": "integer",
        "queue_total": None,
        "queue_done": None,
    }
    response = client.projects.update(id=1, request=Project())
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.update(id=1, request=Project())
    validate_response(async_response, expected_response, expected_types)


async def test_api_projects_reimports_read(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "status": "created",
        "error": "error",
        "task_count": 1,
        "annotation_count": 1,
        "prediction_count": 1,
        "duration": 1,
        "file_upload_ids": {"file_upload_ids": {"key": "value"}},
        "files_as_tasks_list": True,
        "found_formats": {"found_formats": {"key": "value"}},
        "data_columns": {"data_columns": {"key": "value"}},
        "traceback": "traceback",
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "status": None,
        "error": None,
        "task_count": "integer",
        "annotation_count": "integer",
        "prediction_count": "integer",
        "duration": "integer",
        "file_upload_ids": ("dict", {0: (None, None)}),
        "files_as_tasks_list": None,
        "found_formats": ("dict", {0: (None, None)}),
        "data_columns": ("dict", {0: (None, None)}),
        "traceback": None,
        "project": "integer",
    }
    response = client.projects.api_projects_reimports_read(id=1, reimport_pk="reimport_pk")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.api_projects_reimports_read(id=1, reimport_pk="reimport_pk")
    validate_response(async_response, expected_response, expected_types)


async def test_api_projects_tasks_list(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.projects.api_projects_tasks_list(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.projects.api_projects_tasks_list(id=1) is None  # type: ignore[func-returns-value]


async def test_api_projects_tasks_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.projects.api_projects_tasks_delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.projects.api_projects_tasks_delete(id=1) is None  # type: ignore[func-returns-value]


async def test_validate_config(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {"label_config": "label_config"}
    expected_types: typing.Any = {"label_config": None}
    response = client.projects.validate_config(id=1, request=ProjectLabelConfig(label_config="label_config"))
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.projects.validate_config(
        id=1, request=ProjectLabelConfig(label_config="label_config")
    )
    validate_response(async_response, expected_response, expected_types)