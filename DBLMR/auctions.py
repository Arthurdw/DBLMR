import requests
import json
from DBLMR import error


def fetch(url, token):
    """Internal auctions fetch function!"""
    r = requests.get("https://dbl.marcorennmaus.de" + url, headers={'Authorization': token})
    if r.status_code != 404:
        return json.loads(r.text)
    elif r.status_code == 429:
        raise error.TooManyRequestsError("Request limit has been breached.")
    else:
        raise error.NotFoundError("Unable to fetch auction!")


class Auctions:
    def __init__(self, token):
        self.token = token

    @property
    def stats(self):
        """:returns a statistics object about the auctions.
        :rtype object"""
        return Stats(self.token)

    @property
    def bidders(self):
        """:returns an array of bidder objects.
        :rtype list[object]"""
        return [Bidder(user) for user in fetch("/api/auctions/bidders/", self.token)["bidders"]]


class Stats:
    def __init__(self, token):
        self.selected = fetch("/api/auctions/stats/", token)

    @property
    def value(self):
        """:returns sum of all bids (including bids that got outbid) made since recording began.
        :rtype int"""
        return int(self.selected["moneytotal"])

    @property
    def bids(self):
        """:returns count of all bids (including bids that got outbid) since recording.
        :rtype int"""
        return int(self.selected["bidtotal"])

    @property
    def current(self):
        """:returns sum of all active bids this week if there were bids, else it returns `None`.
        :rtype int or None"""
        if self.selected["currentvalue"] is None:
            return None
        return int(self.selected["currentvalue"])


class Bidder:
    def __init__(self, bidder):
        self.selected = bidder

    @property
    def id(self):
        """:returns the bidder their ID.
        :rtype int"""
        return int(self.selected["userid"])

    @property
    def name(self):
        """:returns the bidder their username.
        :rtype str"""
        return str(self.selected["username"])

    @property
    def bet(self):
        """:returns the bet that the bidder place.
        :rtype int"""
        return int(self.selected["amount"])
