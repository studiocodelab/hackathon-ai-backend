# -*- coding: utf-8 -*-
"""
Ollama API

This module provides a simple API for interacting with the Ollama chatbot.
"""

import logging as lg
import time
import uuid

from typing import Any

# import flask
import ollama

lg.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class OllamaAPI:
    """
    OllamaAPI

    This class provides a simple API for interacting with the Ollama chatbot.
    """

    def __init__(
        self, model: str = "llama3.1", system_prompt: str = "", debug: bool = False
    ) -> None:
        """
        Initialize the OllamaAPI object.

        Args:
            model (str): The model to use for the chatbot.
            system_prompt (str): The system prompt to use for the chatbot.
            debug (bool): Whether to enable debug logging.
        """
        self.logger = lg.getLogger(f"{__name__}.{self.__class__.__name__}")
        if debug:
            self.logger.setLevel(lg.DEBUG)
        else:
            self.logger.setLevel(lg.INFO)

        self.model = model
        self.session_ids: dict[str, int] = {}

        self.system_prompt: dict[str, str] = {
            "role": "system",
            "content": system_prompt,
        }
        self.history: dict[str, list[dict[str, str]]] = {}
        self.logger.info(f"Initialized OllamaAPI with model {model}")

    def _update_history(self, session_id: str, message: dict[str, str]) -> None:
        """
        Update the chat history with the latest message.

        Args:
            session_id (str): The session ID.
            message (dict): The message to add to the history.
        """
        self.history[session_id].append(message)

    def generate_session_id(self) -> str:
        """
        Generate a new session ID.

        Returns:
            str: The generated session ID.
        """
        self.logger.debug("Generating new session ID...")
        _uuid = str(uuid.uuid4())
        self.history[_uuid] = []
        self.session_ids[_uuid] = time.time()
        self.logger.debug(f"Generated session ID: {_uuid}")
        return _uuid

    def cleanup(self) -> None:
        """
        Cleanup old session IDs.
        """
        timeout = 60 * 60  # 1 hour
        self.logger.debug(f"Cleaning up session IDs older than {timeout} seconds...")
        for session_id, timestamp in list(self.session_ids.items()).copy():
            if time.time() - timestamp > timeout:
                self.logger.info(f"Cleaning up session ID: {session_id}")
                del self.session_ids[session_id]
                del self.history[session_id]

    def chat(self, session_id: str, text: str, context: str) -> str:
        """
        Chat with the Ollama chatbot.

        Args:
            session_id (str): The session ID.
            text (str): The user input text.
            target_lang (str): The target language for the response.
            context (str): The context for the response, CSV string.

        Example `context`:
        "
        meeting_name;meeting_purpose;datetime;location
        team meeting;discuss project progress;2022-12-31 12:00:00;conference room 1
        h&s training;compliance training;2023-01-01 09:00:00;training room 2
        "
        """
        self.logger.debug("Cleaning up old session IDs...")
        self.cleanup()
        self.logger.info(f"User input (id: {session_id}): {text}")
        self._update_history(session_id, {"role": "user", "content": text})
        self.session_ids[session_id] = time.time()

        context_system_prompt: dict[str, str] = {
            "role": "system",
            "content": "<<DATA>>\n" + context,
        }

        messages = (
            [self.system_prompt, context_system_prompt] + self.history[session_id] + [{"role": "user", "content": text}]  # fmt: skip
        )
        self.logger.debug(f"History: {self.history}")
        response = ollama.chat(self.model, messages)

        self._update_history(session_id, response["message"])
        return response


def pretty_print(response: dict[str, str]) -> None:
    """
    Pretty print the chat response.

    Args:
        response (dict): The chat response.
    """
    print(f"{response['message']['role']}: {response['message']['content']}")


if __name__ == "__main__":  # test the API
    # Create an instance of the OllamaAPI
    api = OllamaAPI(debug=False)
    session_id = api.generate_session_id()
    pretty_print(api.chat(session_id, "Hello, my name's Jane!"))
    pretty_print(api.chat(session_id, "What's my name?"))

    pretty_print(api.chat(session_id, "Tell me how a nuclear reactor works."))
    pretty_print(api.chat(session_id, "shorter explanation"))

    other_session_id = api.generate_session_id()
    pretty_print(api.chat(other_session_id, "Hello, what's my name?"))

    pretty_print(api.chat(session_id, "What's my name?"))
