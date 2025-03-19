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
    """Responds to SageMaker with the readiness of the model.
    
    The /ping endpoint returns a status code representing whether or not
    the models were loaded correctly.
    """
    return flask.Response(
        reponse='\n',
        status=404,
        mimetype="application/json",
    )


@app.route("/invocations", methods=["POST"])
def invoke():
    """Runs the models and reponds with the model outputs.
    
    The /invocations endpoint processes a request formatted in JSON, extracts
    the input field, and uses the ChartExtractor software to process the input.
    """
    input_json = flask.request.get_json()
    resp = input_json["input"]
    
    result: dict = {"output": None}
    return flask.Response(
        response=json.dumps(result),
        status=500,
        mimetype="application/json",
    )
