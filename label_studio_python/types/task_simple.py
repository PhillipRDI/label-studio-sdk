# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .annotation import Annotation
from .prediction import Prediction
from .task_simple_data import TaskSimpleData
from .task_simple_meta import TaskSimpleMeta

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TaskSimple(pydantic.BaseModel):
    id: typing.Optional[int]
    data: TaskSimpleData = pydantic.Field(
        description="User imported or uploaded data for a task. Data is formatted according to the project label config. You can find examples of data for your project on the Import page in the Label Studio Data Manager UI."
    )
    meta: typing.Optional[TaskSimpleMeta] = pydantic.Field(
        description="Meta is user imported (uploaded) data and can be useful as input for an ML Backend for embeddings, advanced vectors, and other info. It is passed to ML during training/predicting steps."
    )
    created_at: typing.Optional[dt.datetime] = pydantic.Field(description="Time a task was created")
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(description="Last time a task was updated")
    is_labeled: typing.Optional[bool] = pydantic.Field(
        description="True if the number of annotations for this task is greater than or equal to the number of maximum_completions for the project"
    )
    overlap: typing.Optional[int] = pydantic.Field(
        description="Number of distinct annotators that processed the current task"
    )
    inner_id: typing.Optional[int] = pydantic.Field(description="Internal task ID in the project, starts with 1")
    total_annotations: typing.Optional[int] = pydantic.Field(
        description="Number of total annotations for the current task except cancelled annotations"
    )
    cancelled_annotations: typing.Optional[int] = pydantic.Field(
        description="Number of total cancelled annotations for the current task"
    )
    total_predictions: typing.Optional[int] = pydantic.Field(
        description="Number of total predictions for the current task"
    )
    comment_count: typing.Optional[int] = pydantic.Field(
        description="Number of comments in the task including all annotations"
    )
    unresolved_comment_count: typing.Optional[int] = pydantic.Field(
        description="Number of unresolved comments in the task including all annotations"
    )
    last_comment_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the last comment was updated"
    )
    project: typing.Optional[int] = pydantic.Field(description="Project ID for this task")
    updated_by: typing.Optional[int] = pydantic.Field(description="Last annotator or reviewer who updated this task")
    file_upload: typing.Optional[int] = pydantic.Field(description="Uploaded file used as data source for this task")
    comment_authors: typing.Optional[typing.List[int]] = pydantic.Field(description="Users who wrote comments")
    annotations: typing.Optional[typing.List[Annotation]]
    predictions: typing.Optional[typing.List[Prediction]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
