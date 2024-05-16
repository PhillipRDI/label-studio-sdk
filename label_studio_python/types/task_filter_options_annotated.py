# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskFilterOptionsAnnotated(str, enum.Enum):
    """
    `only` - include all tasks with at least one not skipped annotation<br>`exclude` - exclude all tasks with at least one not skipped annotation
    """

    ONLY = "only"
    EXCLUDE = "exclude"

    def visit(self, only: typing.Callable[[], T_Result], exclude: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaskFilterOptionsAnnotated.ONLY:
            return only()
        if self is TaskFilterOptionsAnnotated.EXCLUDE:
            return exclude()
