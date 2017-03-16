#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
lesson1.py

Code for the first lesson for Python users. This is an end-to-end demonstration of the capabilities in pandas. Later lessons go into detail about specific aspects.

Created by Chandrasekhar Ramakrishnan on 2017-03-10.
Copyright (c) 2017 Chandrasekhar Ramakrishnan. All rights reserved.
"""

# Import the packages we will use
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Read some data into a frame
# A frame is like an table in a spreadsheet.
# It contains columns (which usually have names) and rows (which can be indexed by number,
# but may also have names)
df = pd.read_csv('https://raw.githubusercontent.com/rmcelreath/rethinking/master/data/Howell1.csv', sep=";")
df.head()

# Graph the data -- let's look at height vs. age
df.plot.scatter(x='age', y='height')

# Filter to adults, since height and age are correlated in children
adults_df = df[df['age'] >= 18]
# Look at height vs. age again
adults_df.plot.scatter(x='age', y='height')

# Print out how many rows are in each frame
len(df), len(adults_df)

# Let's look at how the data are distributed
adults_df['height'].plot.hist()

# Split data in to male and female
# -- first add in a sex column to make it less confusing
df['sex'] = df.apply(lambda row: 'Male' if row['male'] == 1 else 'Female', axis=1)
# -- re-apply the filter, since we modified the data
adults_df = df[df['age'] >= 18]
adults_df.head()

# Let's summarize the data
adults_df[['age', 'height', 'weight']].describe()

# Let's look at the data broken down by sex
adults_df[['age', 'height', 'weight', 'sex']].groupby('sex').describe()

# Let's focus on the means and std
summary_df = adults_df[['age', 'height', 'weight', 'sex']].groupby('sex').describe()
summary_df.loc[(slice(None),['mean', 'std']), :]

# Let's look at the data visually -- plot height broken down by sex
g = sns.FacetGrid(adults_df, hue='sex', size=6)
g.map(sns.distplot, "height")
g.add_legend()


# Actually, let's look at everything
# -- first, get rid of the male column, it's redundant and confusing
del adults_df['male']
adults_df.head()

# -- now flatten the data -- very confusing, it will be explained later
flat_df = adults_df.set_index('sex', append=True)
flat_df = flat_df.stack().reset_index([1, 2])
flat_df.columns = ['sex', 'measurement', 'value']
flat_df.head()

# Plot!
g = sns.FacetGrid(flat_df, col='measurement', hue='sex', size=6, sharex=False)
g.map(sns.distplot, "value")
g.add_legend()



# # Basic Manipulations
# * Subsetting

# * Accessing rows/columns/individual items
# * Indexing
# * Changing Column Headers
# * Changing Row Labels
# * Creating Calculated Values
# * using lambda functions (or functions in general) to manipulate the data
