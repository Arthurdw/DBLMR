import requests
import json
from DBLMR import error, rank


class Bot:
    def __init__(self, token, bot_id):
        self.selected = None
        r = requests.get("https://dbl.marcorennmaus.de/api/bot/" + str(bot_id), headers={'Authorization': token})
        if r.status_code != 404:
            self.selected = r
        elif r.status_code == 429:
            raise error.TooManyRequestsError("Request limit has been breached.")
        else:
            raise error.NotFoundError("Unable to fetch bot!")

    def check(self):
        if self.selected is None:
            raise ValueError("No (correct) ID value got given!")
        else:
            return True

    @property
    def id(self):
        """":returns the selected bot its ID
        :rtype int"""
        if self.check():
            return int(json.loads(self.selected.text)["botid"])

    @property
    def name(self):
        """:returns the selected bot its name.
        :rtype str"""
        if self.check():
            return str(json.loads(self.selected.text)["botname"])

    @property
    def points(self):
        """:returns the all-time earned points.
        :rtype int"""
        if self.check():
            return int(json.loads(self.selected.text)["points"])

    @property
    def monthly(self):
        """:returns the points the bot earned this month.
        :rtype int"""
        if self.check():
            return int(json.loads(self.selected.text)["monthlyPoints"])

    @property
    def daily(self):
        """:returns the points the bot earned today.
        :rtype int"""
        if self.check():
            return int(json.loads(self.selected.text)["dailyPoints"])

    @property
    def servers(self):
        """:returns the amount of guilds the bot is in.
        :rtype int"""
        if self.check():
            return int(json.loads(self.selected.text)["dailyPoints"])

    @property
    def shards(self):
        """:returns the amount of shards the bot has.
        :rtype int"""
        if self.check():
            return int(json.loads(self.selected.text)["shards"])

    @property
    def owners(self):
        """:returns the list of owner(s).
        :rtype list"""
        if self.check():
            return json.loads(self.selected.text)["owners"]

    @property
    def deleted(self):
        """:returns if the bot got removed/deleted from DBL or if it still exists.
        :rtype bool"""
        if self.check():
            removed = False
            if int(json.loads(self.selected.text)["deleted"]) == 1:
                removed = True
            return removed

    @property
    def notice(self):
        """":returns the bot notice. If there is no notice it will return `None`
        :rtype str or None"""
        if self.check():
            return json.loads(self.selected.text)["notice"]

    @property
    def rank(self):
        """:returns the list of owner(s).
        :rtype list"""
        if self.check():
            return rank.Rank(json.loads(self.selected.text)["ranks"])
