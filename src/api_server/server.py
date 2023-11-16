import uvicorn
from fastapi import FastAPI


def start_api_server(application: FastAPI, host: str, port: int) -> None:
    uvicorn.run(app=application, host=host, port=port)
