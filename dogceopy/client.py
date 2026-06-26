from __future__ import annotations

from typing import Any

import requests

from .constants import BASE_URL, USER_AGENT
from .exceptions import APIError


class DogCEOClient:
    """
    Base client for interacting with the Dog CEO API.
    """

    def __init__(
        self,
        timeout: float = 30.0,
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = BASE_URL
        self.timeout = timeout
        self.session = session or requests.Session()

        self.session.headers.update(
            {
                "User-Agent": USER_AGENT,
                "Accept": "application/json",
            }
        )

    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> Any:
        """
        Send an HTTP request to the Dog CEO API.

        Parameters
        ----------
        method : str
            HTTP method (GET, POST, etc.).

        endpoint : str
            API endpoint beginning with '/'.

        Returns
        -------
        Any
            The value of the 'message' field from the API response.

        Raises
        ------
        APIError
            If the request fails or the API returns an error.
        """

        try:
            response = self.session.request(
                method=method,
                url=f"{self.base_url}{endpoint}",
                timeout=self.timeout,
                **kwargs,
            )

            response.raise_for_status()

        except requests.RequestException as exc:
            raise APIError(str(exc)) from exc

        try:
            data = response.json()

        except ValueError as exc:
            raise APIError(
                "The API returned an invalid JSON response."
            ) from exc

        if not isinstance(data, dict):
            raise APIError(
                "Invalid response received from the API."
            )

        if "status" not in data or "message" not in data:
            raise APIError(
                "Malformed API response."
            )

        if data["status"] != "success":
            raise APIError(data["message"])

        return data["message"]

    def get(
        self,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """
        Perform a GET request.

        Parameters
        ----------
        endpoint : str
            API endpoint.

        params : dict[str, Any] | None
            Optional query parameters.

        Returns
        -------
        Any
            API response message.
        """

        return self.request(
            "GET",
            endpoint,
            params=params,
        )

    def close(self) -> None:
        """
        Close the HTTP session.
        """
        self.session.close()

    def __enter__(self) -> "DogCEOClient":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        self.close()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"base_url={self.base_url!r}, "
            f"timeout={self.timeout})"
        )