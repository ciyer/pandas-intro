#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
lesson1.py

Code for the first lesson for Python users.

Created by Chandrasekhar Ramakrishnan on 2017-03-10.
Copyright (c) 2017 Chandrasekhar Ramakrishnan. All rights reserved.
"""

# Import the packages we will use
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Read in some data
df = pd.read_csv('https://raw.githubusercontent.com/rmcelreath/rethinking/master/data/Howell1.csv', sep=";")
df.head()

# Look at one of the columns. What do you see? Columns are names and typed.
print(df['height'].head())
