import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load Data
df = pd.read_csv('StudentPerformanceFactors.csv')

# 2. Basic Preprocessing
# Drop missing values to ensure accurate plotting
df_clean = df.dropna()

# Set the visual style for the plots
sns.set_style("whitegrid")

# --- Distribution of Exam Scores ---
# Analyze the target variable (Exam_Score)
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Exam_Score'], kde=True, bins=30, color='teal')
plt.title('Distribution of Exam Scores')
plt.xlabel('Exam Score')
plt.show()
