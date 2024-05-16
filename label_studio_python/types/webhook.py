# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .webhook_actions_item import WebhookActionsItem
from .webhook_headers import WebhookHeaders

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Webhook(pydantic.BaseModel):
    id: typing.Optional[int]
    organization: typing.Optional[int]
    project: typing.Optional[int]
    url: str = pydantic.Field(description="URL of webhook")
    send_payload: typing.Optional[bool] = pydantic.Field(description="If value is False send only action")
    send_for_all_actions: typing.Optional[bool] = pydantic.Field(
        description="If value is False - used only for actions from WebhookAction"
    )
    headers: typing.Optional[WebhookHeaders] = pydantic.Field(description="Key Value Json of headers")
    is_active: typing.Optional[bool] = pydantic.Field(description="If value is False the webhook is disabled")
    actions: typing.Optional[typing.List[WebhookActionsItem]]
    created_at: typing.Optional[dt.datetime] = pydantic.Field(description="Creation time")
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(description="Last update time")

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
