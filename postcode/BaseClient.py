import json
import requests
import time

from .ApiError import ApiError

class BaseClient(object):
    """Handles communication with API"""
    def __init__(self, url='http://api.postcodes.io'):
        self.__url = url

    @property
    def uri(self):
        return self.__url

    def checkResponse(self, response, main_message):
        if response.status_code < 200 or response.status_code >= 300:
            status = response.status_code
            reason = response.text
            url = response.url
            error = f"      status {status}:{reason}        URL:{url}"
            response.close()
            message = main_message + error
            raise ApiError(message)

    def request(self, method, url, params=None, data=None, headers=None, **kwargs):
        return requests.request(method, url, params=params, data=None, headers=headers, **kwargs)


        