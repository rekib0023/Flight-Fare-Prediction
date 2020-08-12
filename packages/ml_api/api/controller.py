# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:15:23 2020

@author: rkbra
"""

from flask import Blueprint, request


prediction_app = Blueprint('prediction.app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'okayyy!!!'