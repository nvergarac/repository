# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:42:20 2022

@author: oligo

"""
from pathlib import Path
import os

def test():
    idx = 0
    idx2 = 0
    end = 6
    while idx < end:
        idx = idx + 1
        idx2 = idx2 + idx
    print (idx2)
    print("Current working directory:", os.getcwd())

