# KDE Plot - A KDE plot stands for Kernel Density Estimate plot.
#          - It is a smoothed version of a histogram that shows the probability density function of a continuous variable.
#          - While a histogram divides data into bins and shows counts/frequencies,
#           - A KDE plot smooths the data using a kernel function (usually Gaussian) to estimate the probability distribution.

# sns.kdeplot(data=df['column].dropna(), shade = True)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#kdeplot
sns.kdeplot(data=titanic['age'].dropna(), shade = True)
plt.show()