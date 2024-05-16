# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MlBackendState(str, enum.Enum):
    CO = "CO"
    DI = "DI"
    ER = "ER"
    TR = "TR"
    PR = "PR"

    def visit(
        self,
        co: typing.Callable[[], T_Result],
        di: typing.Callable[[], T_Result],
        er: typing.Callable[[], T_Result],
        tr: typing.Callable[[], T_Result],
        pr: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MlBackendState.CO:
            return co()
        if self is MlBackendState.DI:
            return di()
        if self is MlBackendState.ER:
            return er()
        if self is MlBackendState.TR:
            return tr()
        if self is MlBackendState.PR:
            return pr()
