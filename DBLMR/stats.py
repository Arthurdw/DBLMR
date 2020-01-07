import requests
import json
from DBLMR import error


class Stats:
    def __init__(self, token):
        self.token = token
        self.selected = None
        r = requests.get("https://dbl.marcorennmaus.de/api/totals/", headers={'Authorization': token})
        if r.status_code != 404:
            self.selected = json.loads(r.text)
        elif r.status_code == 429:
            raise error.TooManyRequestsError("Request limit has been breached.")
        else:
            raise error.NotFoundError("Unable to fetch statistics!")

    @property
    def bots(self):
        """:returns the count of all bots listed on DBL
        :rtype int"""
        return int(self.selected["totalbot"])

    @property
    def servers(self):
        """:returns the sum of all server counts submitted on DBL
        :rtype int"""
        return int(self.selected["totalserver"])

    @property
    def points(self):
        """:returns the All-Time Points received on DBL
        :rtype int"""
        return int(self.selected["totalpoints"])
