# -*- coding: utf-8 -*-

import logging as lg

import flask

from ollama_python_api import OllamaAPI
from storage import Storage

lg.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create a Flask app
app = flask.Flask(__name__, static_folder="stored_files")

# Load the system prompt from a file
with open("system_prompt.txt", "r") as f:
    system_prompt = f.read()

# Initialize the OllamaAPI object
api = OllamaAPI(system_prompt=system_prompt, debug=True)
storage = Storage()


@app.route("/chat", methods=["POST"])
def chat():
    """
    Chat endpoint for interacting with the chatbot.

    This endpoint accepts a POST request with a JSON body containing a session ID and a message.
    The chatbot will respond with a message.
    """
    data = flask.request.json
    if data["session_id"] not in api.history:
        return flask.jsonify(
            {
                "error": "Invalid session ID, please get a new session ID (/new_session_id)"
            }
        )

    try:
        session_id = data["session_id"]
        text = data["message"]
    except (KeyError, TypeError):
        return flask.jsonify({"error": "Invalid request format"})

    response = api.chat(session_id, text)
    return flask.jsonify(response)


@app.route("/new_session_id", methods=["POST"])
def new_session_id():
    """
    New session ID endpoint for generating a new session ID.

    This endpoint accepts a GET request and returns a new session ID.
    """
    data = flask.request.json

    try:
        _ = data["context"]
    except (KeyError, TypeError):
        return flask.jsonify({"error": "Invalid request format, please provide a context"})

    session_id = api.new_session(data["context"])
    return flask.jsonify({"session_id": session_id})


@app.route("/storage/push", methods=["POST"])
def store():
    """
    Store endpoint for storing data in the storage.

    This endpoint accepts a POST request with a JSON body containing a filename and data.
    """
    data = flask.request.json
    try:
        filename = data["filename"]
        data = data["data"]
    except (KeyError, TypeError):
        return flask.jsonify({"error": "Invalid request format"})

    storage.store(filename, data)
    return flask.jsonify({"message": "Data stored successfully"})


@app.route("/storage/pull", methods=["POST"])
def retrieve():
    """
    Retrieve endpoint for retrieving data from the storage.

    This endpoint accepts a POST request with a JSON body containing a filename.
    """
    data = flask.request.json
    try:
        filename = data["filename"]
    except (KeyError, TypeError):
        return flask.jsonify({"error": "Invalid request format"})

    try:
        data = storage.retrieve(filename)
        return flask.jsonify({"data": data.decode()})
    except KeyError:
        return flask.jsonify({"error": "File not found"})


@app.route("/storage/download/<filename>", methods=["GET"])
def download(filename):
    """
    Download endpoint for downloading data from the storage.

    This endpoint accepts a GET request with a filename in the URL.
    """
    try:
        data = storage.retrieve(filename)
        storage._add_file(f"dl_{filename}", data)
        flask.send_from_directory("stored_files/", f"dl_{filename}")
    except KeyError:
        return flask.jsonify({"error": "File not found"})
    return flask.jsonify({"message": "File downloading"})


@app.route("/storage/pop", methods=["POST"])
def delete():
    """
    Delete endpoint for deleting data from the storage.

    This endpoint accepts a POST request with a JSON body containing a filename.
    """
    data = flask.request.json
    try:
        filename = data["filename"]
    except (KeyError, TypeError):
        return flask.jsonify({"error": "Invalid request format"})

    try:
        storage.delete(filename)
        return flask.jsonify({"message": "File deleted successfully"})
    except KeyError:
        return flask.jsonify({"error": "File not found"})


@app.route("/storage/list", methods=["GET"])
def list_files():
    """
    List endpoint for listing files in the storage.

    This endpoint accepts a GET request and returns a list of filenames.
    """
    files = storage.list()
    return flask.jsonify({"files": list(files)})
