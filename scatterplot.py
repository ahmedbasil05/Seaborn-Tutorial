# Scatter plot - realtionship between two numerical variables
#              - shows trends over time
# sns.scatterplot(data,x,y,hue)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Scatter Plot
sns.scatterplot(data=titanic, x='age', y='fare', hue='sex')
plt.show()
