# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:15:23 2020

@author: rkbra
"""

from flask import Blueprint, request, jsonify, render_template
from regression_model.predict import make_prediction
from regression_model import __version__ as _version

from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})


@prediction_app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@prediction_app.route('/predict', methods=['POST', 'GET'])
def predictForUser():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = {
            'Airline': str(request.form['Airline']),
            'Date_of_Journey': str(request.form['Date_of_Journey']),
            'Source': str(request.form['Source']),
            'Destination': str(request.form['Destination']),
            'Dep_Time': str(request.form['Dep_Time']),
            'Arrival_Time': str(request.form['Arrival_Time']),
            'Duration': str(request.form['Duration']),
            'Total_Stops': str(request.form['Total_Stops']),
            'Additional_Info': str(request.form['Additional_Info']),
        }
        
        _logger.debug(f'Inputs: {json_data}')
        
        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data, many=False)
        

        # Step 3: Model prediction
        result = make_prediction(input_data=input_data, form_input=True)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})   
    

@prediction_app.route('/v1/predict/regression', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data)

        # Step 3: Model prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})