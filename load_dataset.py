# Seaborn - data visulaization library 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#checking dataset
print(titanic.head())  #preview first rows
print(titanic.info())  #check missing values and datatypes