# Bar Plot - shows avg values numeric columns per category
#          - good for comparing averages
#  sns.barplot(data,x,y,hue)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Bar Plot
sns.barplot(data= titanic, x= 'age', y= 'fare')
plt.show()