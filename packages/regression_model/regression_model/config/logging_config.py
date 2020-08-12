# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:29:05 2020

@author: rkbra
"""


import logging
import sys


FORMATTER = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s -" "%(funcName)s:%(lineno)d - %(message)s"
    )


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler