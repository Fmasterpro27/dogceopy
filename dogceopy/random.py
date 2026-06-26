from __future__ import annotations

from .client import DogCEOClient


class Random:
    """
    Global random image endpoints.
    """

    def __init__(
        self,
        client: DogCEOClient,
    ) -> None:
        self._client = client

    def image(self) -> str:
        """
        Get a random dog image.

        Returns
        -------
        str
            Image URL.
        """
        return self._client.get(
            "/breeds/image/random"
        )

    def images(
        self,
        count: int,
    ) -> list[str]:
        """
        Get multiple random dog images.

        Parameters
        ----------
        count : int
            Number of images.

        Returns
        -------
        list[str]
            List of image URLs.
        """
        return self._client.get(
            f"/breeds/image/random/{count}"
        )