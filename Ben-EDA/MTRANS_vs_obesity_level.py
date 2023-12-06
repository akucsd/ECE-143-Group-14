import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

df['NObeyesdad'] = df['NObeyesdad'].replace({
    'Overweight_Level_I': 'Overweight/Obesity',
    'Overweight_Level_II': 'Overweight/Obesity',
    'Obesity_Type_I': 'Overweight/Obesity',
    'Obesity_Type_II': 'Overweight/Obesity',
    'Obesity_Type_III': 'Overweight/Obesity'
})

df['NObeyesdad'] = df['NObeyesdad'].replace({
    'Normal_Weight': 'Not Overweight',
    'Insufficient_Weight': 'Not Overweight'
})

# Set display order
order = ['Automobile', 'Public_Transportation', 'Motorbike', 'Bike', 'Walking']
df['MTRANS'] = pd.Categorical(df['MTRANS'], categories=order, ordered=True)

# Group by 'mtrans' and 'obesity', and count occurrences
grouped = df.groupby(['MTRANS', 'NObeyesdad']).size().unstack()

# Normalize the counts to get percentages
grouped_percent = grouped.div(grouped.sum(axis=1), axis=0) * 100

# Plotting
fig, ax = plt.subplots()

grouped_percent.plot(kind='barh', stacked=True, ax=ax)

# Adding labels and title
ax.set_xlabel('Percentage')
ax.set_title('Overweight vs. Not Overweight')

# Display the plot
plt.show()
