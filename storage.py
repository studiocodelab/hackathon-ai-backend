# -*- coding: utf-8 -*-
"""File storage using base64 encoding."""

import base64
from typing import Any
import logging as lg
import os


class Storage:
    """File storage using base64 encoding."""

    def __init__(self):
        """Initialize the storage."""
        self.storage_dir = "stored_files/"
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)
        self.logger = lg.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.info("Storage initialized.")

    def _add_file(self, filename: str, data: Any):
        """Add a file to the storage."""
        self.logger.info(f"Adding {filename}")
        with open(self.storage_dir + filename, "wb") as f:
            f.write(data)

    def _get_file(self, filename: str):
        """Get a file from the storage."""
        self.logger.info(f"Getting {filename}")
        with open(self.storage_dir + filename, "rb") as f:
            return f.read()

    def store(self, filename: str, data: Any):
        """Store the data in the file."""
        self.logger.info(f"Storing {filename}")
        self._add_file(filename, base64.b64encode(data.encode()))

    def retrieve(self, filename: str):
        """Retrieve the data from the file."""
        self.logger.info(f"Retrieving {filename}")
        return base64.b64decode(self._get_file(filename))

    def delete(self, filename: str):
        """Delete the file."""
        self.logger.info(f"Deleting {filename}")
        os.remove(self.storage_dir + filename)

    def list(self):
        """List the files."""
        self.logger.info("Listing files")
        return os.listdir(self.storage_dir)
