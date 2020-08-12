# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:43:23 2020

@author: rkbra
"""


import pytest


from api.app import create_app
from api.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
