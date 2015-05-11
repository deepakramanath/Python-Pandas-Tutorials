#!/usr/bin/python
# Deepak Ramanath

# Pandas tutorial with Pandas Series

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List of maximim temperature for a particular week
temp = [18, 24, 22, 17, 20, 27, 30]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Creating basic Pandas Series
seriesTemp = pd.Series(temp)
print seriesTemp

# Pandas core class
print type(seriesTemp)

# Pandas core values
print seriesTemp.values

# Pandas core values are nothing but Numpy ndarray
print type(seriesTemp.values)

# Creating a new Pandas Series. Here, we index with days
tempDays = pd.Series(temp, index = days)

# Specifing names to Pnadas Series
tempDays.name = 'Maximum Temperature'
tempDays.index.name = 'Weekday'
print tempDays

# Creating a dictionary using exisiting lists
dictTempDays = dict(zip(days, temp))
print dictTempDays

# We can create a Pnadas Series directly from a dictionary
tempDays2 = pd.Series(dictTempDays)
print tempDays2

# Numpy arrays are homogeneous. One float values, makes the entire series float
temp1 = [18, 24.2, 22, 17, 20, 27, 30]
tempDays3 = pd.Series(temp1, index=days)
print tempDays3

# Looping over the Series using enumerate
print "Looping using enumerate"
for i, v in enumerate(tempDays3):
	print "index: %s, value: %s" % (i, v)

# Lopping over the Series using iteritems
print "Looping using iteritems"
for j, k in tempDays3.iteritems():
	print "key: %s, value: %s" % (j, k)

#Some simple vectorised operations
print "Vector operation 1"
tempDays4 = tempDays3 * 2
print tempDays4

print "Vector operation 2"
tempDays5 =  tempDays3**2
print tempDays5
