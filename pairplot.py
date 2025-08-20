# Pair Plot - used for multi-variable exploration
#           -> grid of plots (scatterplot + histograms)
#           - helps see contributions, correlations
# sns.pairplot(data,hue,vars)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#pairplot
sns.pairplot(titanic, hue='sex', vars=['age','fare'])
plt.show()