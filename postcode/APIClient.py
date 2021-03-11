from .BaseClient import BaseClient
from .PostCodes import PostCodes

class APIClient:

    def __init__(self):
        self.__baseClient = BaseClient()
        self.__PostCodes = PostCodes(self.__baseClient)

    @property
    def PostCodes(self):
        """
        :return: A client for interacting with PostCodes
        """
        return self.__PostCodes