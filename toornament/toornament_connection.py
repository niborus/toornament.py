from abc import ABCMeta, abstractmethod
import requests


class SyncToornamentConnection(metaclass=ABCMeta):

    def __init__(self, token):
        self.token = token

    @staticmethod
    @abstractmethod
    def _base_url() -> str:
        """:returns The Base-URL of the API"""

    def _simple_access(self, method, path, *, path_parameters, query_parameters, headers) -> dict:

        headers['X-Api-Key'] = self.token

        url = self._base_url() + path.format(**path_parameters)

        response = requests.request(method, url, headers = headers, params = query_parameters)

        response.raise_for_status()

        return response.json()
