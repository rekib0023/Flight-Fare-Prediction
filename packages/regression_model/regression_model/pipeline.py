# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:02:04 2020

@author: rkbra
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from sklearn.ensemble import RandomForestRegressor


from regression_model.processing import preprocessors as pp
from regression_model.processing import features
from regression_model.config import config


pipeline = Pipeline(
   [
     ('duration_transformer', features.DurationTransformer()),
     ('journey_data_transformer', features.JourneyDateTransformer()),
     ('departure_time_transformer', features.DepartureTimeTransformer()),
     ('arival_time_transformer', features.ArrivalTimeTransformer()),
     ('total_stop_transformer', pp.TotalStopTransformer()),
     ('rare_label_encoder', pp.RareLabelCategoricalEncoder(tol=0.0015, variables=config.FEATURE_WITH_RARE_LABELS)),
     ('encoder', pp.Encoder(variables=config.CATEGORICAL_FEATURES)),
     ('scaler', MinMaxScaler()),
     ('model', RandomForestRegressor(n_estimators=500))
   ]
)