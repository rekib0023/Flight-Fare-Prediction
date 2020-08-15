# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:01:11 2020

@author: rkbra
"""

import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # GIven
    test_data = load_dataset(file_name='test.xlsx')
    single_test_input = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_input)

    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)
    
    
def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.xlsx')
    original_data_length = len(test_data)
    multiple_test_input = test_data

    # When
    subject = make_prediction(input_data=multiple_test_input)

    # Then
    assert subject is not None
    assert len(subject.get('predictions')) == original_data_length

    