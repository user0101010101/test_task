import abc


class ConfigurationObtainer(abc.ABC):
    @abc.abstractmethod
    def get_repo_host(self) -> str:
        pass

    @abc.abstractmethod
    def get_repo_port(self) -> int:
        pass

    @abc.abstractmethod
    def get_repo_user(self) -> str:
        pass

    @abc.abstractmethod
    def get_repo_password(self) -> str:
        pass

    @abc.abstractmethod
    def get_repo_database(self) -> str:
        pass

    @abc.abstractmethod
    def get_repo_collection(self) -> str:
        pass
