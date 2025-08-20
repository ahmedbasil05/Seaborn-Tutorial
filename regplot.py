#regression plot - shows linear rekatonship between two numeric variables
# sns.regplot(data,x,y)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Regplot
sns.regplot(data= titanic, x= 'age', y= 'fare')
plt.show()