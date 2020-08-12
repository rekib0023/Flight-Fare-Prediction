# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:01:11 2020

@author: rkbra
"""


import numpy as np
import pandas as pd

from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import LabelEncoder

            
    
class TotalStopTransformer(BaseEstimator, TransformerMixin):
    """Encoding Total Stops to numerical"""
    
    def __init__(self, variables='Total_Stops'):
        self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X[self.variables].replace(['1 stop', 'non-stop', '2 stops', '3 stops', '4 stops'], [1, 0, 2, 3, 4], inplace=True)
        
        return X
    
    
    
class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """Rare label categorical encoder"""

    def __init__(self, tol=0.05, variables=None):
        self.tol = tol
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # persist frequent labels in dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            # the encoder will learn the most frequent categories
            t = pd.Series(X[var].value_counts() / np.float(len(X)))
            # frequent labels:
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(
                X[feature].isin(self.encoder_dict_[feature]), X[feature], "Rare"
            )

        return X
            

class Encoder(BaseEstimator, TransformerMixin):
    """Categorical Encoder"""
    
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X[self.variables] = X[self.variables].apply(LabelEncoder().fit_transform)
        
        return X