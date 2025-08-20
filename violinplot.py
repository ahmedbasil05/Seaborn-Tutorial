#  Violin Plot - combines box plot + density plot
#              - shows the shape of distribution
#  sns.violinplot(data,x,y,hue,split = True)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Violin Plot
sns.violinplot(data= titanic, x= 'age', y= 'fare', hue= 'sex', split= True)  #split->shows distribution ny hue
plt.show()