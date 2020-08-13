# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:46:16 2020

@author: rkbra
"""

import json

from regression_model.config import config
from regression_model.processing.data_management import load_dataset


def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the regression_model package.
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    post_json = test_data.to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/regression',
                                      json=json.loads(post_json))
    

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    
    
    if response_json.get('errors') == None:
        errors_len = 0
    else:
        errors_len = len(response_json.get('errors'))

    # Check correct number of errors removed
    assert len(response_json.get('predictions')) + errors_len == len(test_data)
