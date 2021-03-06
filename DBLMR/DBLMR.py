from requests import get
from DBLMR import error, bot, user, auctions, stats


class Client:
    def __init__(self, token):
        self.token = token
        if get("https://dbl.marcorennmaus.de/api/quota/", headers={'Authorization': token}).status_code == 401:
            raise error.UnauthorizedError("An invalid token was given on setup!")

    @property
    def user(self):
        """":returns a user object!
        :rtype object"""
        return user.User(self.token)

    @property
    def auctions(self):
        """:returns a auction object!
        :rtype object"""
        return auctions.Auctions(self.token)

    @property
    def stats(self):
        """:returns a stats object.
        :rtype object"""
        return stats.Stats(self.token)

    def bot(self, bot_id: int):
        """:returns a bot object!
        :rtype object"""
        return bot.Bot(self.token, bot_id)
