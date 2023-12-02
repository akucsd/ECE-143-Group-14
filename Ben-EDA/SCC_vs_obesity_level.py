import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Obesity_with_Macros.csv')

df['NObeyesdad'] = df['NObeyesdad'].replace({
    'Overweight_Level_I': 'Overweight',
    'Overweight_Level_II': 'Overweight',
    'Obesity_Type_I': 'Obesity',
    'Obesity_Type_II': 'Obesity',
    'Obesity_Type_III': 'Obesity'
})

# First, filter the data for 'yes' under SCC
yes_data = df[df['SCC'] == 'yes']

# Group by 'obesity level' and count the occurrences
yes_obesity_counts = yes_data['NObeyesdad'].value_counts()

order = ['Insufficient_Weight', 'Normal_Weight', 'Overweight', 'Obesity']
# Plot the first pie chart
plt.figure(1)
plt.pie(yes_obesity_counts[order],
        labels=yes_obesity_counts[order].index,
        autopct='%1.2f%%',
        startangle=90,
        colors=sns.color_palette('Set2'),
        explode=[0, 0.1, 0, 0])
plt.title('People who Monitor their Daily Calories')

# Repeat the process for 'no' under SCC
no_data = df[df['SCC'] == 'no']
no_obesity_counts = no_data['NObeyesdad'].value_counts()

# Plot the second pie chart
plt.figure(2)
plt.pie(no_obesity_counts[order],
        labels=no_obesity_counts[order].index,
        autopct='%1.2f%%',
        startangle=90,
        colors=sns.color_palette('Set2'),
        explode=[0, 0.1, 0, 0])
plt.title('People who don\'t Monitor their Daily Calories')
plt.show()
