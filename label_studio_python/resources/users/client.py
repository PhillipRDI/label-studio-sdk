# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...types.base_user import BaseUser
from .types.api_current_user_reset_token_create_response import ApiCurrentUserResetTokenCreateResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def api_current_user_reset_token_create(self) -> ApiCurrentUserResetTokenCreateResponse:
        """
        Reset the user token for the current user.

        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_current_user_reset_token_create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/current-user/reset-token/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ApiCurrentUserResetTokenCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_current_user_token_list(self) -> None:
        """
        Get a user token to authenticate to the API as the current user.

        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_current_user_token_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/current-user/token"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_current_user_whoami_read(self) -> BaseUser:
        """
        Retrieve details of the account that you are using to access the API.

        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_current_user_whoami_read()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/current-user/whoami"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_users_list(self) -> typing.List[BaseUser]:
        """
        List the users that exist on the Label Studio server.

        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_users_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/users/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[BaseUser], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_users_create(self, *, request: BaseUser) -> BaseUser:
        """
        Create a user in Label Studio.

        Parameters:
            - request: BaseUser.
        ---
        from label-studio import BaseUser
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_users_create(request=BaseUser(username="username", ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/users/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_users_read(self, id: int) -> BaseUser:
        """
        Get info about a specific Label Studio user, based on the user ID.

        Parameters:
            - id: int. User ID
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_users_read(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/users/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_users_delete(self, id: int) -> None:
        """
        Delete a specific Label Studio user.

        Parameters:
            - id: int. User ID
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_users_delete(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/users/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_users_partial_update(self, id: int, *, request: BaseUser) -> BaseUser:
        """
        Update details for a specific user, such as their name or contact information, in Label Studio.

        Parameters:
            - id: int. User ID

            - request: BaseUser.
        ---
        from label-studio import BaseUser
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.users.api_users_partial_update(id=1, request=BaseUser(username="username", ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/users/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def api_current_user_reset_token_create(self) -> ApiCurrentUserResetTokenCreateResponse:
        """
        Reset the user token for the current user.

        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_current_user_reset_token_create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/current-user/reset-token/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ApiCurrentUserResetTokenCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_current_user_token_list(self) -> None:
        """
        Get a user token to authenticate to the API as the current user.

        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_current_user_token_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/current-user/token"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_current_user_whoami_read(self) -> BaseUser:
        """
        Retrieve details of the account that you are using to access the API.

        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_current_user_whoami_read()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/current-user/whoami"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_users_list(self) -> typing.List[BaseUser]:
        """
        List the users that exist on the Label Studio server.

        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_users_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/users/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[BaseUser], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_users_create(self, *, request: BaseUser) -> BaseUser:
        """
        Create a user in Label Studio.

        Parameters:
            - request: BaseUser.
        ---
        from label-studio import BaseUser
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_users_create(request=BaseUser(username="username", ), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/users/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_users_read(self, id: int) -> BaseUser:
        """
        Get info about a specific Label Studio user, based on the user ID.

        Parameters:
            - id: int. User ID
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_users_read(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/users/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_users_delete(self, id: int) -> None:
        """
        Delete a specific Label Studio user.

        Parameters:
            - id: int. User ID
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_users_delete(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/users/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_users_partial_update(self, id: int, *, request: BaseUser) -> BaseUser:
        """
        Update details for a specific user, such as their name or contact information, in Label Studio.

        Parameters:
            - id: int. User ID

            - request: BaseUser.
        ---
        from label-studio import BaseUser
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.users.api_users_partial_update(id=1, request=BaseUser(username="username", ), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/users/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
