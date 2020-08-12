# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:15:23 2020

@author: rkbra
"""

from flask import Blueprint, request

from api.config import get_logger

_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'
