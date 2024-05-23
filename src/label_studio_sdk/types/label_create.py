# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class LabelCreate(pydantic_v1.BaseModel):
    id: typing.Optional[int] = None
    created_by: typing.Optional[int] = None
    organization: typing.Optional[int] = None
    project: int
    from_name: str
    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Time of label creation
    """

    updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Time of label modification
    """

    value: typing.Dict[str, typing.Any] = pydantic_v1.Field()
    """
    Label value
    """

    title: str = pydantic_v1.Field()
    """
    Label title
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Label description
    """

    approved: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Status of label
    """

    approved_by: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    User who approved this label
    """

    projects: typing.Optional[typing.List[int]] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
