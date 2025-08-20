# Lineplot - shows trends over continuous data
#          - best fore time series and continuous data
#   sns.linplot(data,x,y)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Lineplot
sns.lineplot(data= titanic, x= 'age', y= 'fare')
plt.show()
