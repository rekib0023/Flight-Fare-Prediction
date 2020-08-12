# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:00:01 2020

@author: rkbra
"""

import numpy as np
import pandas as pd

from sklearn.base import TransformerMixin, BaseEstimator


class DurationTransformer(BaseEstimator, TransformerMixin):
    """Converts duration hours in min."""
    
    def __init__(self, variables='Duration'):
        self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X[self.variables] = X[self.variables].str.replace("h", '*60').str.replace(" ", '+').str.replace("m", '*1').apply(eval)
        
        return X
    
    
class JourneyDateTransformer(BaseEstimator, TransformerMixin):
    """Converts Journey Date to respective Day and Month"""
    
    def __init__(self, variables='Date_of_Journey'):
        self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X["Journey_day"] = X[self.variables].str.split('/').str[0].astype(int)
        X["Journey_month"] = X[self.variables].str.split('/').str[1].astype(int)
        X.drop([self.variables], axis = 1, inplace = True)
        
        return X
            
    
    
class DepartureTimeTransformer(BaseEstimator, TransformerMixin):
    """Converts Departure Time to respective Hiur and Minute"""
    
    def __init__(self, variables='Dep_Time'):
        self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X["Dep_hour"] = pd.to_datetime(X[self.variables]).dt.hour
        X["Dep_min"] = pd.to_datetime(X[self.variables]).dt.minute
        X.drop([self.variables], axis = 1, inplace = True)
        
        return X
    
    
class ArrivalTimeTransformer(BaseEstimator, TransformerMixin):
    """Converts Arrival Time to respective Hiur and Minute"""
    
    def __init__(self, variables='Arrival_Time'):
        self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X["Arrival_hour"] = pd.to_datetime(X[self.variables]).dt.hour
        X["Arrival_min"] = pd.to_datetime(X[self.variables]).dt.minute
        X.drop([self.variables], axis = 1, inplace = True)
        
        return X