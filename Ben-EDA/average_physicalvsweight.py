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
    
    # Filter relevant columns
    relevant_columns = ['NObeyesdad', 'FAF', "BMI"]
    filtered_data = data[relevant_columns]
    
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
    
    # Perform t-test for each pair of categories
    '''for i in range(len(order)):
        for j in range(i + 1, len(order)):
            category1 = order[i]
            category2 = order[j]
            group1 = filtered_data[filtered_data['NObeyesdad'] == category1]['FAF']
            group2 = filtered_data[filtered_data['NObeyesdad'] == category2]['FAF']
            t_statistic, p_value = ttest_ind(group1, group2)
        
            print(f"T-test between {category1} and {category2}:")
            print(f"  p-value = {p_value}")
        
            if p_value < 0.05:  # Adjust the significance level as needed
                print("  The difference in mean is statistically significant.")
            else:
                print("  The difference in mean is not statistically significant.")
    '''
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
    

if __name__ == "__main__":
    PAFvsweight()