# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:59:03 2020

@author: rkbra
"""

from api.config import PACKAGE_ROOT

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()
