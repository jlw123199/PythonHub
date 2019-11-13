
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
# import statistics
import numpy as np
import scipy
from scipy import stats
import seaborn

tripData = pd.read_csv('trip.csv')
print tripData.head(5)
print len(tripData)



# After looking at the feature classification in Table 1-4 Eric noticed that Nancy had
# correctly identified the data types and thus it seemed to be an easy job for him to explain
# what variable types mean. As Eric recalled to have explained the following:
# In normal everyday interaction with data we usually represent numbers
# as integers, text as strings, True/False as Boolean, etc. These are what
# we refer to as data types. But the lingo in machine learning is a bit more
# granular, as it splits the data types we knew earlier into variable types.
# Understanding these variable types is crucial in deciding upon the type
# of charts while doing exploratory data analysis or while deciding upon a
# suitable machine learning algorithm to be applied on our data.
# Continuous/Quantitative Variables
# A continuous variable can have an infinite number of values within a given range. Unlike
# discrete variables, they are not countable. Before exploring the types of continuous
# variables, let’s understand what is meant by a true zero point.
