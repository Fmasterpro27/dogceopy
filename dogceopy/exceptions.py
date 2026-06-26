class DogCEOError(Exception):
    """Base exception for DogCEOPy."""


class APIError(DogCEOError):
    """Raised when the Dog CEO API returns an error."""