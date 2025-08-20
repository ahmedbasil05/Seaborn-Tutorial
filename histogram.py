# Histogram - visualizes frequency distribution by category
# sns.histplot(data,x,bins)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Histogram Plot
sns.histplot(data=titanic, x='age', bins=20)
plt.show()