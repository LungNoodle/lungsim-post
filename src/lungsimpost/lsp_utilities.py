#!/usr/bin/env python
import numpy as np

def is_float(str):
    try:
        num = float(str)
    except ValueError:
        return False
    return True
