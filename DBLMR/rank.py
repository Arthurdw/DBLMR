class Rank:
    def __init__(self, rank):
        self.rank = rank

    @property
    def daily(self):
        """:returns the bot its rank position ordered by amount of points gained in the last 24 rolling hours.
        :rtype int"""
        return self.rank["dailyPoints"]

    @property
    def monthly(self):
        """:returns the bot its rank position ordered by the amount of points gained in the last month
        :rtype int"""
        return self.rank["monthlyPoints"]

    @property
    def all(self):
        """:returns the bot its rank position ordered by All-Time Points
        :rtype int"""
        return self.rank["allTimePoints"]

    @property
    def servers(self):
        """:returns the bot its rank position ordered by amount of servers
        :rtype int"""
        return self.rank["serverCount"]

    @property
    def shards(self):
        """:returns the bot its rank position ordered by amount of shards
        :rtype int"""
        return self.rank["shardCount"]
