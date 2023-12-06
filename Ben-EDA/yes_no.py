# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:29:02 2023

@author: ben's computer
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a CSV file named "Obesity_with_Macros.csv" in the current directory
csv_file = "Obesity_with_Macros.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Set the style for Seaborn
sns.set(style="whitegrid")

# Define the order for x-axis categories
order_yes_no = ["yes", "no"]

# Create subplots with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot the bar chart for "family_history_with_overweight"
sns.countplot(x="family_history_with_overweight", data=df, order=order_yes_no, ax=axs[0, 0])
axs[0, 0].set_title("Respondents with Family History of Overweightness")
axs[0, 0].set_xlabel("Family History of Overweightness")
axs[0, 0].set_ylabel("Count")

# Plot the bar chart for "FAVC"
sns.countplot(x="FAVC", data=df, order=order_yes_no, ax=axs[0, 1])
axs[0, 1].set_title("Respondents that Frequently Consume High Caloric Food (FAVC)")
axs[0, 1].set_xlabel("Frequently Consume High Caloric Food (FAVC)")
axs[0, 1].set_ylabel("Count")

# Plot the bar chart for "SMOKE"
sns.countplot(x="SMOKE", data=df, order=order_yes_no, ax=axs[1, 0])
axs[1, 0].set_title("Respondents that Smoke (SMOKE)")
axs[1, 0].set_xlabel("Smoking Status (SMOKE)")
axs[1, 0].set_ylabel("Count")

# Plot the bar chart for "SCC"
sns.countplot(x="SCC", data=df, order=order_yes_no, ax=axs[1, 1])
axs[1, 1].set_title("Respondents that Monitor Calorie Consumption (SCC)")
axs[1, 1].set_xlabel("Monitoring Calorie Consumption (SCC)")
axs[1, 1].set_ylabel("Count")

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()