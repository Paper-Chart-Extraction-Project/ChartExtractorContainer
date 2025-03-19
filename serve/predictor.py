"""Contains code for serving the model using http requests on AWS Sagemaker."""

import flask
import json
import logging
import os

# Load in model
# Model artifacts should be stored in /opt/ml/model/

app = flask.Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    """Responds to SageMaker with the readiness of the model."""
    return flask.Response(
        reponse='\n',
        status=404,
        mimetype="application/json",
    )


@app.route("/invocations", methods=["POST"])
def invoke():
    """Runs the models and reponds with the model outputs."""
    input_json = flask.request.get_json()
    resp = input_json["input"]
    
    result: dict = {"output": None}
    return flask.Response(
        response=json.dumps(result),
        status=500,
        mimetype="application/json",
    )
