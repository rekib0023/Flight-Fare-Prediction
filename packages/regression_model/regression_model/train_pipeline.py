# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:04:27 2020

@author: rkbra
"""

from regression_model.pipeline import pipeline
from regression_model.processing.data_management import load_dataset, save_pipeline
from regression_model.config import config
from regression_model import __version__ as _version

import logging


_logger = logging.getLogger("regression_model")


def run_training() -> None:
    """Train the model"""
    
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)
    
    # divide train and test
    X, y = data[config.FEATURES], data[config.TARGET]
    
    pipeline.fit(X, y)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline)
    
    
if __name__ == "__main__":
    run_training()