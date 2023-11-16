import os

from .configuration_obtainer import ConfigurationObtainer


class EnvConfigurationObtainer(ConfigurationObtainer):
    def __init__(self):
        self._repo_host = os.environ["host"]
        self._repo_port = os.environ["port"]
        self._repo_user = os.environ["user"]
        self._repo_password = os.environ["password"]
        self._repo_database_title = os.environ["database"]
        self._repo_collection_title = os.environ["collection"]

    def get_repo_host(self) -> str:
        return self._repo_host

    def get_repo_port(self) -> int:
        return int(self._repo_port)

    def get_repo_user(self) -> str:
        return self._repo_user

    def get_repo_password(self) -> str:
        return self._repo_password

    def get_repo_database(self) -> str:
        return self._repo_database_title

    def get_repo_collection(self) -> str:
        return self._repo_collection_title
