import requests
import json
from DBLMR import error


class User:
    def __init__(self, token):
        self.selected = requests.get("https://dbl.marcorennmaus.de/api/quota/", headers={'Authorization': token})

    @property
    def id(self):
        """":returns the ID of the user that this token belongs to.
        :rtype int"""
        return int(json.loads(self.selected.text)['userid'])

    @property
    def requests(self):
        """":returns the used quota of the current minute!
        :rtype int"""
        return json.loads(self.selected.text)['requests']

    @property
    def limit(self):
        """":returns the quota limit of this user!
        :rtype int"""
        return json.loads(self.selected.text)['ratelimit']
