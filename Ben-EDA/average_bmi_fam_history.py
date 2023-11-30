# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 02:55:57 2023

@author: ben's computer
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def avgbmifam():
    # Load your CSV file into a pandas DataFrame
    df = pd.read_csv('Obesity_with_Macros.csv')
    
    # Set custom colors for the boxplot
    colors = {'yes': 'lightblue', 'no': 'lightcoral'}
   
    # Create a boxplot to visualize the distribution of BMI for each group
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='family_history_with_overweight', y='BMI', data=df, palette=colors)
    plt.title('Distribution of BMI for Respondents with and without Family History of Overweight')
    plt.xlabel('Family History of Overweight')
    plt.ylabel('BMI')
    plt.show()
        
    
    # Separate data into two groups: with and without a family history of overweight
    with_history = df[df['family_history_with_overweight'] == 'yes']
    without_history = df[df['family_history_with_overweight'] == 'no']
    
       # Calculate the average BMI for each group
    average_bmi_with_history = with_history['BMI'].mean()
    average_bmi_without_history = without_history['BMI'].mean()
        
    # Perform a t-test to determine if the difference in means is statistically significant
    t_stat, p_value = stats.ttest_ind(with_history['BMI'], without_history['BMI'], equal_var=False)
        
    # Display the results
    print(f"Average BMI with family history: {average_bmi_with_history:.2f}")
    print(f"Average BMI without family history: {average_bmi_without_history:.2f}")
    print("\nT-test results:")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")

    # Check if the difference is statistically significant
    #alpha is the significance level, usually =.05
    alpha = 0.05
    if p_value < alpha:
        print("The difference in average BMI is statistically significant.")
    else:
        print("There is no statistically significant difference in average BMI.")
        
    
    # Perform a correlation test between BMI and family history
    correlation, p_value_corr = stats.pearsonr(df['BMI'], df['family_history_with_overweight'].map({'yes': 1, 'no': 0}))
   
    # Display the results for the correlation test
    print("\nCorrelation results:")
    print(f"Pearson correlation coefficient: {correlation:.4f}")
    if correlation > 0.9 or correlation < -0.9:
        print( "Perfect correlation")
    elif 0.5 <= abs(correlation) <= 0.9:
        print( "High degree of correlation")
    elif 0.3 <= abs(correlation) <= 0.49:
        print( "Moderate degree of correlation")
    elif abs(correlation) < 0.3:
        print( "Low degree of correlation")
    else:
        print( "No correlation")
        
if __name__ == "__main__":
    avgbmifam()