# import error
import requests
import json


class User:
    def __init__(self, token):
        self.token = token
        self.url = "https://dbl.marcorennmaus.de"
        self.quota = "/api/quota/"

    @property
    def get_token(self):
        """:returns the secret token!
        :rtype str"""
        return self.token

    @property
    def id(self):
        """":returns the ID of the user that this token belongs to.
        :rtype int"""
        r = requests.get(self.url + self.quota, headers={'Authorization': self.token}).text
        return int(json.loads(r)['userid'])

    @property
    def requests(self):
        """":returns the used quota of the current minute!
        :rtype int"""
        r = requests.get(self.url + self.quota, headers={'Authorization': self.token}).text
        return json.loads(r)['requests']

    @property
    def limit(self):
        """":returns the quota limit of this user!
        :rtype int"""
        r = requests.get(self.url + self.quota, headers={'Authorization': self.token}).text
        return json.loads(r)['ratelimit']
