import logging
from fastapi import status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from .schema.response import HTTPErrorResponse
from .schema.response.common.errors import InternalUnhandledErrorResponse


async def _handle_http_exception(request: Request, exc: HTTPException) -> JSONResponse:
    msg_warn = "HTTP exception occurred."
    logging.warning(msg_warn, exc_info=True)

    body = HTTPErrorResponse(message=exc.detail)

    return JSONResponse(status_code=exc.status_code, content=body.model_dump())


async def _handle_request_validation_error(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    msg_warn = "Request validation error."
    logging.warning(msg_warn, exc_info=True)

    body = HTTPErrorResponse(message=str(exc))

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=body.model_dump()
    )


async def _handle_unhandled_error(request: Request, exc: Exception) -> JSONResponse:
    msg_err = "Unhandled error occurred."
    logging.error(msg_err, exc_info=True)

    body = InternalUnhandledErrorResponse()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=body.model_dump(),
    )


ERROR_RESPONSES = {
    status.HTTP_404_NOT_FOUND: {"model": HTTPErrorResponse},
    status.HTTP_405_METHOD_NOT_ALLOWED: {"model": HTTPErrorResponse},
    status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": HTTPErrorResponse},
}


EXCEPTION_HANDLERS = {
    HTTPException: _handle_http_exception,
    RequestValidationError: _handle_request_validation_error,
    Exception: _handle_unhandled_error,
}
