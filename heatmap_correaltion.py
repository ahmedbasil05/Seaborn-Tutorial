import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
titanic = sns.load_dataset('titanic')

# Compute correlation only for numeric columns
corr = titanic.select_dtypes(include=['number']).corr()

# Plot heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap - Titanic Dataset")
plt.show()
