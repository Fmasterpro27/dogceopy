from __future__ import annotations

from .client import DogCEOClient


class Breeds:

    def __init__(
        self,
        client: DogCEOClient,
    ) -> None:
        self._client = client

    def list(self) -> list[str]:
        """
        Get a list of all dog breeds.

        Returns
        -------
        list[str]
            List of breed names.
        """
        return self._client.get("/breeds/list")

    def list_all(self) -> dict[str, list[str]]:
        """
        Get all dog breeds and their sub-breeds.

        Returns
        -------
        dict[str, list[str]]
            Dictionary mapping breeds to sub-breeds.
        """
        return self._client.get("/breeds/list/all")

    def sub_breeds(
        self,
        breed: str,
    ) -> list[str]:
        """
        Get all sub-breeds for a breed.

        Parameters
        ----------
        breed : str
            Breed name.

        Returns
        -------
        list[str]
            List of sub-breeds.
        """
        return self._client.get(
            f"/breed/{breed.lower()}/list"
        )

    def has_sub_breeds(
        self,
        breed: str,
    ) -> bool:
        """
        Check whether a breed has sub-breeds.

        Parameters
        ----------
        breed : str

        Returns
        -------
        bool
        """
        return len(self.sub_breeds(breed)) > 0

    def exists(
        self,
        breed: str,
    ) -> bool:
        """
        Check whether a breed exists.

        Parameters
        ----------
        breed : str

        Returns
        -------
        bool
        """
        breeds = self.list()
        return breed.lower() in breeds