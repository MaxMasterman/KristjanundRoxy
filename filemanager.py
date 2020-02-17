#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 17 01:16:44 2020

@author: kristjan
"""

import yaml

def yaml_dump(filename, data):
    with open(filename, 'w') as file:
        yaml.dump(data, file)
        
def yaml_load(filename):
    with open(filename, 'r') as file:
        return yaml.load(file)
