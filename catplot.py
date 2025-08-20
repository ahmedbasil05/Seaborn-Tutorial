# catplot - grid of categorical plots
#         - combine multiple categories in a single plot
# sns.catplot(data,x,y,hue,kind,height,aspect)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Catplot
sns.catplot(data= titanic, x= 'age', y= 'fare', hue= 'sex', kind= 'bar')
plt.show()