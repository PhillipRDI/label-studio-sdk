# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ApiWebhooksUpdateRequestActionsItem(str, enum.Enum):
    PROJECT_CREATED = "PROJECT_CREATED"
    PROJECT_UPDATED = "PROJECT_UPDATED"
    PROJECT_DELETED = "PROJECT_DELETED"
    TASKS_CREATED = "TASKS_CREATED"
    TASKS_DELETED = "TASKS_DELETED"
    ANNOTATION_CREATED = "ANNOTATION_CREATED"
    ANNOTATIONS_CREATED = "ANNOTATIONS_CREATED"
    ANNOTATION_UPDATED = "ANNOTATION_UPDATED"
    ANNOTATIONS_DELETED = "ANNOTATIONS_DELETED"
    LABEL_LINK_CREATED = "LABEL_LINK_CREATED"
    LABEL_LINK_UPDATED = "LABEL_LINK_UPDATED"
    LABEL_LINK_DELETED = "LABEL_LINK_DELETED"

    def visit(
        self,
        project_created: typing.Callable[[], T_Result],
        project_updated: typing.Callable[[], T_Result],
        project_deleted: typing.Callable[[], T_Result],
        tasks_created: typing.Callable[[], T_Result],
        tasks_deleted: typing.Callable[[], T_Result],
        annotation_created: typing.Callable[[], T_Result],
        annotations_created: typing.Callable[[], T_Result],
        annotation_updated: typing.Callable[[], T_Result],
        annotations_deleted: typing.Callable[[], T_Result],
        label_link_created: typing.Callable[[], T_Result],
        label_link_updated: typing.Callable[[], T_Result],
        label_link_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApiWebhooksUpdateRequestActionsItem.PROJECT_CREATED:
            return project_created()
        if self is ApiWebhooksUpdateRequestActionsItem.PROJECT_UPDATED:
            return project_updated()
        if self is ApiWebhooksUpdateRequestActionsItem.PROJECT_DELETED:
            return project_deleted()
        if self is ApiWebhooksUpdateRequestActionsItem.TASKS_CREATED:
            return tasks_created()
        if self is ApiWebhooksUpdateRequestActionsItem.TASKS_DELETED:
            return tasks_deleted()
        if self is ApiWebhooksUpdateRequestActionsItem.ANNOTATION_CREATED:
            return annotation_created()
        if self is ApiWebhooksUpdateRequestActionsItem.ANNOTATIONS_CREATED:
            return annotations_created()
        if self is ApiWebhooksUpdateRequestActionsItem.ANNOTATION_UPDATED:
            return annotation_updated()
        if self is ApiWebhooksUpdateRequestActionsItem.ANNOTATIONS_DELETED:
            return annotations_deleted()
        if self is ApiWebhooksUpdateRequestActionsItem.LABEL_LINK_CREATED:
            return label_link_created()
        if self is ApiWebhooksUpdateRequestActionsItem.LABEL_LINK_UPDATED:
            return label_link_updated()
        if self is ApiWebhooksUpdateRequestActionsItem.LABEL_LINK_DELETED:
            return label_link_deleted()
