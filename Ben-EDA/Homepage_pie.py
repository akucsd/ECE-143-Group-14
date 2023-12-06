# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:20:51 2023

@author: ben's computer
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # Load the dataset
    file_path = "Obesity_with_Macros.csv"  # Replace with the actual file path
    df = pd.read_csv(file_path)
    
    # Set up Seaborn color palettes
    gender_palette = "pastel"
    obesity_palette = "Set3"
    age_palette = "Blues"
    weight_palette = "viridis"
    height_palette = "muted"
    
    # Plot 1: Pie plot of all genders
    sns.set_palette(gender_palette)
    gender_counts = df["Gender"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Distribution of Genders")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Adjust legend position
    plt.savefig("gender_distribution.png", bbox_inches="tight")
    plt.show()
    
    # Plot 2: Pie plot of all NObeyesdad (Obesity categories)
    sns.set_palette(obesity_palette)
    obesity_counts = df["NObeyesdad"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(obesity_counts, labels=obesity_counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Distribution of Obesity Categories")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Adjust legend position
    plt.savefig("obesity_distribution.png", bbox_inches="tight")
    plt.show()
    
    # Plot 3: Pie plot of age groups
    sns.set_palette(age_palette)
    age_bins = [14, 22, 30, 35, 45, 61]
    df["Age Group"] = pd.cut(df["Age"], bins=age_bins)
    age_group_counts = df["Age Group"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(age_group_counts, labels=age_group_counts.index, startangle=90)
    plt.title("Distribution of Age Groups")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Adjust legend position
    plt.savefig("age_distribution.png", bbox_inches="tight")
    plt.show()

    # Plot 4: Pie plot of height groups
    sns.set_palette(height_palette)
    height_bins = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    df["Height Group"] = pd.cut(df["Height"], bins=height_bins)
    height_group_counts = df["Height Group"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(height_group_counts, labels=height_group_counts.index, startangle=90)
    plt.title("Distribution of Height(meters) Groups")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Adjust legend position
    plt.savefig("height_distribution.png", bbox_inches="tight")
    plt.show()

    # Plot 5: Pie plot of weight groups
    sns.set_palette(weight_palette)
    weight_bins = list(range(35, 190, 25))
    df["Weight Group"] = pd.cut(df["Weight"], bins=weight_bins, labels=None)
    weight_group_counts = df["Weight Group"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(weight_group_counts, labels=weight_group_counts.index, startangle=90)
    plt.title("Distribution of Weight(kg) Groups")
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Adjust legend position
    plt.savefig("weight_distribution.png", bbox_inches="tight")
    plt.show()