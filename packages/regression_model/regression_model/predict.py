# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:54:31 2020

@author: rkbra
"""

import numpy as np
import pandas as pd

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)


pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
pipeline = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""
    
    data = pd.read_json(input_data)
    prediction = pipeline.predict(data[config.FEATURES])
    
    results = {"predictions": prediction, "version": _version}
    
    _logger.info(
            f"Making predictions with model version: (_version)"
            f"Inputs: {data}"
            f"Predictions: {results}"
        )
    
    return results