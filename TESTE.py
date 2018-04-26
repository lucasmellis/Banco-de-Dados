# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:22:10 2018

@author: Lucas
"""

import json
with open ('teste.txt', 'r') as arquivo:
    Estoque = json.loads(arquivo.read())