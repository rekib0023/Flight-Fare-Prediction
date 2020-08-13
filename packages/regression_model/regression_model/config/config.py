# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:35:26 2020

@author: rkbra
"""

import pathlib

import regression_model


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"


PIPELINE_NAME = "randomforest_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"


# data
TESTING_DATA_FILE = "test.xlsx"
TRAINING_DATA_FILE = "train.xlsx"
TARGET = "Price"


FEATURES = ['Airline', 
            'Date_of_Journey', 
            'Source', 
            'Destination', 
            'Route',
            'Dep_Time', 
            'Arrival_Time', 
            'Duration', 
            'Total_Stops',
            'Additional_Info']

CATEGORICAL_FEATURES = ['Airline', 
                        'Source', 
                        'Destination', 
                        'Route', 
                        'Additional_Info']


FEATURE_WITH_RARE_LABELS = ['Airline', 'Additional_Info']