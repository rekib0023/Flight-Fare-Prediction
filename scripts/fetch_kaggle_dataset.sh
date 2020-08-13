#!/usr/bin/env bash

kaggle datasets download -d nikhilmittal/flight-fare-prediction-mh -p packages/regression_model/regression_model/datasets/


unzip packages/regression_model/regression_model/datasets/flight-fare-prediction-mh.zip -d packages/regression_model/regression_model/datasets

mv packages/regression_model/regression_model/datasets/Data_Train.xlsx packages/regression_model/regression_model/datasets/train.xlsx

mv packages/regression_model/regression_model/datasets/Test_set.xlsx packages/regression_model/regression_model/datasets/test.xlsx

rm packages/regression_model/regression_model/datasets/flight-fare-prediction-mh.zip

rm packages/regression_model/regression_model/datasets/Sample_submission.xlsx