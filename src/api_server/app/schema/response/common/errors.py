from ..base import ErrorResponse, ErrorResult


class InternalUnhandledError(ErrorResult):
    code: int = 1
    message: str = "Got internal error. Investigation is recommended."


class InternalUnhandledErrorResponse(ErrorResponse):
    error: InternalUnhandledError = InternalUnhandledError()
