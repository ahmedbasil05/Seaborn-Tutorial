# FacetGrid - multi-plot layout by category
# sns.FacetGrid(data,col,row,margin_titles = True)
# .map(kind, col = '')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading titanic dataset
titanic = sns.load_dataset('titanic')

#FacetGrid 
g = sns.FacetGrid(titanic, col='sex', row='class', margin_titles=True)
g.map(sns.histplot, 'age')
plt.show()
