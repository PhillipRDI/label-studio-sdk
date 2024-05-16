# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...types.annotation import Annotation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AnnotationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_annotation(self, id: int) -> Annotation:
        """
        Retrieve a specific annotation for a task using the annotation result ID.

        Parameters:
            - id: int. A unique integer value identifying this annotation.
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.annotations.retrieve_annotation(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/annotations/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Annotation, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_annotations_delete(self, id: int) -> None:
        """
        Delete an annotation. This action can't be undone!

        Parameters:
            - id: int. A unique integer value identifying this annotation.
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.annotations.api_annotations_delete(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/annotations/{id}/"),
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

    def api_annotations_partial_update(self, id: int, *, request: Annotation) -> Annotation:
        """
        Update existing attributes on an annotation.

        Parameters:
            - id: int. A unique integer value identifying this annotation.

            - request: Annotation.
        ---
        from label-studio import Annotation
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.annotations.api_annotations_partial_update(id=1, request=Annotation(), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/annotations/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Annotation, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_tasks_annotations_list(self, id: int) -> typing.List[Annotation]:
        """
        List all annotations for a task.

        Parameters:
            - id: int. Task ID
        ---
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.annotations.api_tasks_annotations_list(id=1, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/{id}/annotations/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Annotation], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_tasks_annotations_create(self, id: int, *, request: Annotation) -> Annotation:
        """
        Add annotations to a task like an annotator does. The content of the result field depends on your
        labeling configuration. For example, send the following data as part of your POST
        request to send an empty annotation with the ID of the user who completed the task:

        ```json
        {
        "result": {},
        "was_cancelled": true,
        "ground_truth": true,
        "lead_time": 0,
        "task": 0
        "completed_by": 123
        }
        ```

        Parameters:
            - id: int. Task ID

            - request: Annotation.
        ---
        from label-studio import Annotation
        from label-studio.client import LabelStudioApi

        client = LabelStudioApi(api_key="YOUR_API_KEY", )
        client.annotations.api_tasks_annotations_create(id=1, request=Annotation(), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/{id}/annotations/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Annotation, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAnnotationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_annotation(self, id: int) -> Annotation:
        """
        Retrieve a specific annotation for a task using the annotation result ID.

        Parameters:
            - id: int. A unique integer value identifying this annotation.
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.annotations.retrieve_annotation(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/annotations/{id}/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Annotation, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_annotations_delete(self, id: int) -> None:
        """
        Delete an annotation. This action can't be undone!

        Parameters:
            - id: int. A unique integer value identifying this annotation.
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.annotations.api_annotations_delete(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/annotations/{id}/"),
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

    async def api_annotations_partial_update(self, id: int, *, request: Annotation) -> Annotation:
        """
        Update existing attributes on an annotation.

        Parameters:
            - id: int. A unique integer value identifying this annotation.

            - request: Annotation.
        ---
        from label-studio import Annotation
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.annotations.api_annotations_partial_update(id=1, request=Annotation(), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/annotations/{id}/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Annotation, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_tasks_annotations_list(self, id: int) -> typing.List[Annotation]:
        """
        List all annotations for a task.

        Parameters:
            - id: int. Task ID
        ---
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.annotations.api_tasks_annotations_list(id=1, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/{id}/annotations/"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Annotation], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_tasks_annotations_create(self, id: int, *, request: Annotation) -> Annotation:
        """
        Add annotations to a task like an annotator does. The content of the result field depends on your
        labeling configuration. For example, send the following data as part of your POST
        request to send an empty annotation with the ID of the user who completed the task:

        ```json
        {
        "result": {},
        "was_cancelled": true,
        "ground_truth": true,
        "lead_time": 0,
        "task": 0
        "completed_by": 123
        }
        ```

        Parameters:
            - id: int. Task ID

            - request: Annotation.
        ---
        from label-studio import Annotation
        from label-studio.client import AsyncLabelStudioApi

        client = AsyncLabelStudioApi(api_key="YOUR_API_KEY", )
        await client.annotations.api_tasks_annotations_create(id=1, request=Annotation(), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/{id}/annotations/"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Annotation, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
