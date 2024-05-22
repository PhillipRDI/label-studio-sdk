# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .ml_backend_auth_method import MlBackendAuthMethod
from .ml_backend_state import MlBackendState


class MlBackend(pydantic_v1.BaseModel):
    id: typing.Optional[int] = None
    state: typing.Optional[MlBackendState] = None
    readable_state: typing.Optional[str] = None
    is_interactive: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Used to interactively annotate tasks. If true, model returns one list with results
    """

    url: str = pydantic_v1.Field()
    """
    URL for the machine learning model server
    """

    error_message: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Error message in error state
    """

    title: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Name of the machine learning backend
    """

    auth_method: typing.Optional[MlBackendAuthMethod] = None
    basic_auth_user: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    HTTP Basic Auth user
    """

    basic_auth_pass: typing.Optional[str] = None
    basic_auth_pass_is_set: typing.Optional[str] = None
    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Description for the machine learning backend
    """

    extra_params: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Any extra parameters passed to the ML Backend during the setup
    """

    model_version: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Current model version associated with this machine learning backend
    """

    timeout: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Response model timeout
    """

    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    auto_update: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    If false, model version is set by the user, if true - getting latest version from backend.
    """

    project: int

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
