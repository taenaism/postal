import json

from .BaseClient import BaseClient


class PostCodes(object):
    """
    Client for interacting with PostCodes
    """
    def __init__(self, client: BaseClient):
        self.__baseClient = client
        self.__uri_API = client.uri
        self.__setPathTemplates()

    def getPostCode(self, POSTCODE):
        if POSTCODE is None:
            raise TypeError

        response = self.__baseClient.request("get",self.__postcode.format(POSTCODE=POSTCODE))

        self.__baseClient.checkResponse(response, f"Failed to get PostCode, {POSTCODE}.")

        jobject = json.loads(response.content)
        result = {'country':jobject['result']['country'],'region':jobject['result']['region']}
        response.close()
        return result

    def validate(self, POSTCODE):
        if POSTCODE is None:
            raise TypeError

        response = self.__baseClient.request("get",self.__validate.format(POSTCODE=POSTCODE))

        self.__baseClient.checkResponse(response, f"Failed to get PostCode, {POSTCODE}.")

        jobject = json.loads(response.content)
        result = jobject['result']
        response.close()
        return result

    def nearest(self, POSTCODE):
        if POSTCODE is None:
            raise TypeError

        response = self.__baseClient.request("get",self.__nearest.format(POSTCODE=POSTCODE))

        self.__baseClient.checkResponse(response, f"Failed to get PostCode, {POSTCODE}.")

        jobject = json.loads(response.content)
        items = jobject['result']
        response.close()
        
        result = []
        for x in items:
            result.append({'postcode':x['postcode'],'country':x['country'],'region':x['region']})
        return result

    # private methods

    def __setPathTemplates(self):
        self.__basePath = self.__uri_API
        self.__validate = self.__basePath + "/postcodes/{POSTCODE}/validate"
        self.__nearest = self.__basePath + "/postcodes/{POSTCODE}/nearest"
        self.__postcode = self.__basePath + "/postcodes/{POSTCODE}"