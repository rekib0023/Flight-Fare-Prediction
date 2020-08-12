# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:22:22 2020

@author: rkbra
"""

from api.app import create_app
from api.config import DevelopmentConfig


application = create_app(
    config_object=DevelopmentConfig)


if __name__ == '__main__':
    application.run()
