# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 03:42:28 2023

@author: ben's computer
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, pearsonr

def PAFvsweight():
    # Load the CSV file into a pandas DataFrame
    # Load the CSV file into a DataFrame
    file_path = 'Obesity_with_Macros.csv'
    data = pd.read_csv(file_path)
    
    # Create a joint distribution plot for BMI vs FAF
    plt.figure(figsize=(8, 6))
    sns.jointplot(x='FAF', y='BMI', data=data, kind='scatter', marginal_kws=dict(bins=25, fill=False), color='skyblue')
    plt.suptitle('Joint Distribution of BMI and FAF', y=1.02)
    plt.show()
    
    
    # Filter relevant columns
    relevant_columns = ['NObeyesdad', 'FAF', "BMI"]
    filtered_data = data[relevant_columns]
    
    grouped_filtered_data = data[relevant_columns]
    
    
    # Define the desired order for the 'NObeyesdad' categories
    order = ['Insufficient_Weight', 'Normal_Weight', 'Overweight_Level_I', 'Overweight_Level_II',
         'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III']


    # Group by 'NObeyesdad' and calculate the average FAF for each group
    average_faf_per_group = filtered_data.groupby('NObeyesdad')['FAF'].mean().reset_index()
    
    # Print the average value for each unique 'NObeyesdad'
    print("Average FAF per NObeyesdad:")
    print(average_faf_per_group)

    # Plot the bar plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='NObeyesdad', y='FAF', data=average_faf_per_group, order=order, palette='viridis')
    plt.title('Average physical activity frequency per weight classification')
    plt.xlabel('Weight classification')
    plt.ylabel('physical activity frequency per week')
    plt.xticks(rotation=45, ha='right')
    

    # Perform correlation test between 'FAF' and 'BMI'
    correlation, p_value_corr = pearsonr(filtered_data['FAF'], filtered_data['BMI'])
    
    # Display the results for the correlation test
    print("\nCorrelation between FAF and BMI Result:")
    print(f"Pearson correlation coefficient: {correlation:.4f}")
    if correlation > 0.9 or correlation < -0.9:
        print( "Perfect correlation")
    elif 0.5 <= abs(correlation) <= 0.9:
        print( "High degree of correlation")
    elif 0.3 <= abs(correlation) <= 0.49:
        print( "Moderate degree of correlation")
    elif abs(correlation) < 0.3:
        print( "Low(close to NONE) degree of correlation")
    else:
        print( "No correlation")

    plt.show()
    
    
    
    grouped_filtered_data = data[relevant_columns].copy()
    # Combine 'Overweight_Level_I' and 'Overweight_Level_II' into 'Overweight'
    grouped_filtered_data['NObeyesdad'] = grouped_filtered_data['NObeyesdad'].replace({'Overweight_Level_I': 'Overweight','Overweight_Level_II': 'Overweight'})
   
    # Combine 'Obesity_Type_I', 'Obesity_Type_II', and 'Obesity_Type_III' into 'Obesity'
    grouped_filtered_data['NObeyesdad'] = grouped_filtered_data['NObeyesdad'].replace({'Obesity_Type_I': 'Obesity', 
                                                                      'Obesity_Type_II': 'Obesity',
                                                                      'Obesity_Type_III': 'Obesity'})
    grouped_order = ['Insufficient_Weight', 'Normal_Weight', 'Overweight', 'Obesity']

    # Group by 'NObeyesdad' and calculate the average FAF for each group
    grouped_average_faf_per_group = grouped_filtered_data.groupby('NObeyesdad')['FAF'].mean().reset_index()
    
    # Print the average value for each unique 'NObeyesdad'
    print("Average FAF per NObeyesdad:")
    print(grouped_average_faf_per_group)

    # Plot the bar plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='NObeyesdad', y='FAF', data=grouped_average_faf_per_group, order=grouped_order, palette='muted')
    plt.title('Average physical activity frequency per weight classification')
    plt.xlabel('Weight classification')
    plt.ylabel('physical activity frequency per week')
    plt.xticks(rotation=45, ha='right')
    
    #plt.show()
    
    
    
    
    more_grouped_filtered_data = data[relevant_columns].copy()
    # Combine 'Overweight_Level_I' and 'Overweight_Level_II' into 'Overweight'
    more_grouped_filtered_data['NObeyesdad'] = more_grouped_filtered_data['NObeyesdad'].replace({'Insufficient_Weight': 'Non-obese', 'Normal_Weight': 'Non-obese','Overweight_Level_I': 'Non-obese','Overweight_Level_II': 'Non-obese', 'Obesity_Type_I': 'Obese', 
                                                                      'Obesity_Type_II': 'Obese',
                                                                      'Obesity_Type_III': 'Obese'})
   
    more_grouped_order = ['Non-obese', 'Obese']

    # Group by 'NObeyesdad' and calculate the average FAF for each group
    more_grouped_average_faf_per_group = more_grouped_filtered_data.groupby('NObeyesdad')['FAF'].mean().reset_index()
    
    # Print the average value for each unique 'NObeyesdad'
    print("Average FAF per NObeyesdad:")
    print(more_grouped_average_faf_per_group)

    # Plot the bar plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='NObeyesdad', y='FAF', data=more_grouped_average_faf_per_group, order=more_grouped_order, palette='deep')
    plt.title('Average physical activity frequency per weight classification')
    plt.xlabel('Weight classification')
    plt.ylabel('physical activity frequency per week')
    plt.xticks(rotation=45, ha='right')
    
    plt.show()

if __name__ == "__main__":
    PAFvsweight()