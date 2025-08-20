# 🎨 Seaborn Mastery: Beginner to Advanced  

This repository contains my complete **Seaborn learning journey**, covering all major concepts step by step with code examples and visualizations.  

Seaborn is a Python data visualization library based on Matplotlib, providing a high-level interface for creating beautiful and informative statistical graphics.  

---

## 📂 Repository Structure  

- **01_Basics/** → Getting started with Seaborn (installation, datasets, styling)  
- **02_Distribution_Plots/** → histplot, kdeplot, distplot
- **03_Categorical_Plots/** → barplot, countplot, boxplot, violinplot 
- **04_Relationship_Plots/** → scatterplot, lineplot, relplot  
- **05_Matrix_Plots/** → heatmap, clustermap  
- **06_Multi-Variable_Plots/** → pairplot 
- **07_Customization/** → titles, labels, color palettes, styles, themes  
- **08_Advanced_Topics/** → FacetGrid, regression plots, annotations, combining plots  
- **09_Practice_Projects/** → Mini projects using Titanic, Tips, and custom datasets  

---

## 🚀 Topics Covered  

✔️ Introduction to Seaborn  
✔️ Built-in Datasets (tips, titanic, iris, etc.)  
✔️ Distribution plots (histogram, KDE, etc.)  
✔️ Categorical plots (bar, violin, box, swarm, strip)  
✔️ Relationship plots (scatter, line, relplot)  
✔️ Matrix plots (heatmap, clustermap)  
✔️ Multi-variable plots (pairplot, jointplot)  
✔️ Themes & Styles (darkgrid, whitegrid, ticks, etc.)  
✔️ Advanced customization (palette, annotations, subplots integration)  
✔️ Practical mini projects  

---

## 🎯 Purpose

- 📘 Learn Seaborn step by step (Beginner → Advanced)
- 🧑‍💻 Build a reference guide for future projects
 - 📊 Create professional, clean visualizations
- 🚀 Prepare for Data Analysis, Machine Learning, and AI projects

---

## 📊 Example Outputs  

Here are some example plots from the repository:  

- **Heatmap Example**  
```python
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
corr = titanic.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
