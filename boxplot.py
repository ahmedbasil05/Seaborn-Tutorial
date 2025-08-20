# Box Plot - distribution of numeric data over categories
#          - shows edians, quartiles, outliers
#           - useful for extreme values and variability
# sns.boxplot(data,x,y,hue)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Box Plot
sns.boxplot(data= titanic, x= 'age', y= 'fare', hue= 'sex')
plt.show()