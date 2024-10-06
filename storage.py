# -*- coding: utf-8 -*-
"""File storage using base64 encoding."""

import base64
from typing import Any
import logging as lg


class Storage:
    """File storage using base64 encoding."""

    def __init__(self):
        """Initialize the storage."""
        self.logger = lg.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._files: dict[str, Any] = {}
        self.logger.info("Storage initialized.")

    def store(self, filename: str, data: Any):
        """Store the data in the file."""
        self.logger.info(f"Storing {filename}")
        self._files[filename] = base64.b64encode(data.encode())

    def retrieve(self, filename: str):
        """Retrieve the data from the file."""
        self.logger.info(f"Retrieving {filename}")
        return base64.b64decode(self._files[filename])

    def delete(self, filename: str):
        """Delete the file."""
        self.logger.info(f"Deleting {filename}")
        del self._files[filename]

    def list(self):
        """List the files."""
        self.logger.info("Listing files")
        return self._files.keys()
