# -*- coding: utf-8 -*-

import logging as lg

import flask

from ollama_python_api import OllamaAPI

lg.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create a Flask app
app = flask.Flask(__name__)

# Load the system prompt from a file
with open("system_prompt.txt", "r") as f:
    system_prompt = f.read()

# Initialize the OllamaAPI object
api = OllamaAPI(system_prompt=system_prompt, debug=True)


@app.route("/chat", methods=["POST"])
def chat():
    data = flask.request.json
    try:
        session_id = data["session_id"]
        text = data["message"]
    except KeyError:
        return flask.jsonify({"error": "Invalid request format"})

    response = api.chat(session_id, text)

    return flask.jsonify(response)


@app.route("/new_session_id", methods=["GET"])
def new_session_id():
    session_id = api.generate_session_id()
    return flask.jsonify({"session_id": session_id})
