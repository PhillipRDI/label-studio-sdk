# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...types.prediction import Prediction

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PredictionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def api_predictions_list(
        self,
        *,
        task: typing.Optional[str] = None,
        task_project: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
    ) -> typing.List[Prediction]:
        """
        List all predictions and their IDs.

        Parameters:
            - task: typing.Optional[str]. Filter the returned list by task

            - task_project: typing.Optional[str]. Filter the returned list by task\_\_project

            - project: typing.Optional[str]. Filter the returned list by project
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.predictions.api_predictions_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/predictions/"),
            params=remove_none_from_dict({"task": task, "task__project": task_project, "project": project}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Prediction], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_predictions_create(self, *, request: Prediction) -> Prediction:
        """
        Create a prediction for a specific task.

        Parameters:
            - request: Prediction.
        ---
        from label-studio import Prediction
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.predictions.api_predictions_create(request=Prediction(task=1, ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/predictions/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_predictions_read(self, id: int) -> Prediction:
        """
        Get details about a specific prediction by its ID.

        Parameters:
            - id: int. Prediction ID
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.predictions.api_predictions_read(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_predictions_update(self, id: int, *, request: Prediction) -> Prediction:
        """
        Overwrite prediction data by prediction ID.

        Parameters:
            - id: int. Prediction ID

            - request: Prediction.
        ---
        from label-studio import Prediction
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.predictions.api_predictions_update(id=1, request=Prediction(task=1, ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_predictions_delete(self, id: int) -> None:
        """
        Delete a prediction by prediction ID.

        Parameters:
            - id: int. Prediction ID
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.predictions.api_predictions_delete(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
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

    def api_predictions_partial_update(self, id: int, *, request: Prediction) -> Prediction:
        """
        Update prediction data by prediction ID.

        Parameters:
            - id: int. Prediction ID

            - request: Prediction.
        ---
        from label-studio import Prediction
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.predictions.api_predictions_partial_update(id=1, request=Prediction(task=1, ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPredictionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def api_predictions_list(
        self,
        *,
        task: typing.Optional[str] = None,
        task_project: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
    ) -> typing.List[Prediction]:
        """
        List all predictions and their IDs.

        Parameters:
            - task: typing.Optional[str]. Filter the returned list by task

            - task_project: typing.Optional[str]. Filter the returned list by task\_\_project

            - project: typing.Optional[str]. Filter the returned list by project
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.predictions.api_predictions_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/predictions/"),
            params=remove_none_from_dict({"task": task, "task__project": task_project, "project": project}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Prediction], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_predictions_create(self, *, request: Prediction) -> Prediction:
        """
        Create a prediction for a specific task.

        Parameters:
            - request: Prediction.
        ---
        from label-studio import Prediction
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.predictions.api_predictions_create(request=Prediction(task=1, ), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/predictions/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_predictions_read(self, id: int) -> Prediction:
        """
        Get details about a specific prediction by its ID.

        Parameters:
            - id: int. Prediction ID
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.predictions.api_predictions_read(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_predictions_update(self, id: int, *, request: Prediction) -> Prediction:
        """
        Overwrite prediction data by prediction ID.

        Parameters:
            - id: int. Prediction ID

            - request: Prediction.
        ---
        from label-studio import Prediction
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.predictions.api_predictions_update(id=1, request=Prediction(task=1, ), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_predictions_delete(self, id: int) -> None:
        """
        Delete a prediction by prediction ID.

        Parameters:
            - id: int. Prediction ID
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.predictions.api_predictions_delete(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
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

    async def api_predictions_partial_update(self, id: int, *, request: Prediction) -> Prediction:
        """
        Update prediction data by prediction ID.

        Parameters:
            - id: int. Prediction ID

            - request: Prediction.
        ---
        from label-studio import Prediction
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.predictions.api_predictions_partial_update(id=1, request=Prediction(task=1, ), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/predictions/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Prediction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
