from __future__ import annotations

from .client import DogCEOClient


class Images:
    """
    Image-related endpoints.
    """

    def __init__(
        self,
        client: DogCEOClient,
    ) -> None:
        self._client = client

    def all(
        self,
        breed: str,
    ) -> list[str]:
        """
        Get all images for a breed.

        Parameters
        ----------
        breed : str
            Breed name.

        Returns
        -------
        list[str]
            List of image URLs.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/images"
        )

    def random(
        self,
        breed: str,
    ) -> str:
        """
        Get a random image for a breed.

        Parameters
        ----------
        breed : str
            Breed name.

        Returns
        -------
        str
            Image URL.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/images/random"
        )

    def random_many(
        self,
        breed: str,
        count: int,
    ) -> list[str]:
        """
        Get multiple random images for a breed.

        Parameters
        ----------
        breed : str
            Breed name.

        count : int
            Number of images.

        Returns
        -------
        list[str]
            List of image URLs.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/images/random/{count}"
        )

    def sub_all(
        self,
        breed: str,
        sub_breed: str,
    ) -> list[str]:
        """
        Get all images for a sub-breed.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/{sub_breed.lower()}/images"
        )

    def sub_random(
        self,
        breed: str,
        sub_breed: str,
    ) -> str:
        """
        Get a random image for a sub-breed.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/{sub_breed.lower()}/images/random"
        )

    def sub_random_many(
        self,
        breed: str,
        sub_breed: str,
        count: int,
    ) -> list[str]:
        """
        Get multiple random images for a sub-breed.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/{sub_breed.lower()}/images/random/{count}"
        )