# Count plot - counts the deatils of specific column/entry in dataset
#            - frequency of categories
#  sns.countplot(data,x)   --> x = category column

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Countplot
sns.countplot(data= titanic, x= 'class', hue= 'sex')
plt.show()