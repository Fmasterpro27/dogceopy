from .breeds import Breeds
from .client import DogCEOClient
from .images import Images
from .random import Random
from .version import __version__


class DogCEO:


    def __init__(
        self,
        timeout: float = 30.0,
    ) -> None:
        client = DogCEOClient(timeout=timeout)

        self.breeds = Breeds(client)
        self.images = Images(client)
        self.random = Random(client)

    def close(self) -> None:
        self.breeds._client.close()

    def __enter__(self) -> "DogCEO":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()


__all__ = [
    "DogCEO",
    "DogCEOClient",
    "Breeds",
    "Images",
    "Random",
    "__version__"
]