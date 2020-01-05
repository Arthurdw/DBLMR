# Marco Rennmaus DBL API wrapper errors.


class DBLMRError(Exception):
    """"Base exception class for the Marco Rennmaus DBL API wrapper"""
    pass


class UnauthorizedError(DBLMRError):
    """"Occurs when no header or an invalid token has been given!"""
    pass


class TooManyRequestsError(DBLMRError):
    """Occurs when a ratelimit has been breached.
    Default ratelimit is 20 quota points."""
    pass


class NotFoundError(DBLMRError):
    """Occurs when Marco Rennmaus DBL API wrapper couldn't fetch the data."""
    pass
