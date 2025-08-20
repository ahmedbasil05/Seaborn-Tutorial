# Displot - distribution plot
# sns.displot(data,x,hue,kind,height,aspect)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#Distribution Plot
sns.displot(data=titanic, x='age', hue='sex', kind='kde', height=5, aspect=1.5)
plt.show()