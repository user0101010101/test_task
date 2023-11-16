from pydantic import BaseModel


class ResponseBody(BaseModel):
    result: BaseModel


class HTTPErrorResponse(BaseModel):
    message: str


class ErrorResult(BaseModel):
    message: str
    code: int


class ErrorResponse(BaseModel):
    error: ErrorResult
