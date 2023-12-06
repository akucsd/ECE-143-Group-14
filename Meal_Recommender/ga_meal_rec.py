import pandas as pd
import numpy as np
import runGA
from bs4 import BeautifulSoup
import requests


def ga_algo(csv_file,height,weight,gender,age,phy_activity,bmi_level):
    recipe_file=pd.read_csv(csv_file)
    chromosome_length=float(recipe_file.shape[0])
    ohe_meals=pd.get_dummies(recipe_file['Meal'])
    calories_csv=recipe_file['Calories']
    protein_csv=recipe_file['Protein']
    carbs_csv=recipe_file['Carbs']
    fat_csv=recipe_file['Fat']
    A=np.vstack((calories_csv,protein_csv,carbs_csv,fat_csv,ohe_meals['Breakfast'],ohe_meals['Entrée'],ohe_meals['Protein'],
                 ohe_meals['Side'],ohe_meals['Soup']))
    A=A.astype(float)
    cal,pro,carbs,fat=calculate_macros(height,weight,gender,age,phy_activity,bmi_level)
    b=[cal,pro,carbs,fat,2,2,2,2,2]
    b=np.array(b)
    b=b.astype(float)
    #ga
    gaAnalyzer = runGA.initialize()
    y=gaAnalyzer.runGA(chromosome_length,A,b)
    y=np.array(y)
    binary_array = (y >= 0.5).astype(int).T
    filtered_data=recipe_file[binary_array==1]
    drop_cols=['Servings','Cuisine','ProteinSource','Notes']
    dropped_df=filtered_data.drop(columns=drop_cols)
    drop_index=dropped_df.reset_index(drop=True)
    drop_index=drop_index.rename(columns={'URL':'Recipe Links'})
    calories=drop_index['Calories'].sum()
    protein=drop_index['Protein'].sum()
    fats=drop_index['Fat'].sum()
    carbz=drop_index['Carbs'].sum()
    return drop_index,calories,protein,carbz,fats


def calculate_macros(height, weight, gender, age, phy_activity,bmi_level):
    url = "https://www.calculator.net/macro-calculator.html"

    if gender=="Male":
        gender_par="m"
    else:
        gender_par="f"
    
    if phy_activity== 0:
        td= 1.2
    elif phy_activity==1:
        td= 1.375
    elif phy_activity==2:
        td= 1.465
    elif phy_activity==3:
        td==1.55
    elif phy_activity==4:
        td= 1.725
    else:
        td== 1

    if bmi_level=='Insufficient_Weight':
        cg='g1'
    elif bmi_level=='Overweight_Level_I' or bmi_level=='Overweight_Level_II':
        cg='l'
    elif bmi_level=='Obesity_Level_I':
        cg='l1'
    elif bmi_level=='Obesity_Level_II' or bmi_level=='Obesity_Level_III':
        cg='l2'
    else:
        cg='m'

    params = {
        "ctype": "metric",
        "cage": age,
        "csex": gender_par,
        "cheightmeter": height,
        "ckg": weight,
        "cactivity": td,
        "cgoal":cg,
        "printit": 0,
        "x": 121,
        "y": 28
    }

    response = requests.get(url, params=params)

    soup = BeautifulSoup(response.content, 'html.parser')

    macros = dict()

    labels = soup.find_all('td', {'class': 'arrow_box'})
    values = soup.find_all('td', {'class': 'result_box'})
    for label, value in zip(labels, values):
        temp_lab = label.div.text.strip()
        temp_val = value.text.replace('<', '').replace(':', '').strip().split(" ")
        macros[temp_lab+" ("+temp_val[1]+")"] = temp_val[0]

    carbs=int(macros['Carbs (grams/day)'])
    protein=int(macros['Protein (grams/day)'])
    fat=int(macros['Fat (grams/day)'])
    cal=macros['Food Energy (Calories/dayor)'].replace(',', '')
    cal=int(cal)
    return cal,protein,carbs,fat
 
   
if __name__=="__main__":
    recipe_file="Recipes@.csv"
    macros_cal,macros_protein,macros_carbs,macros_fat=calculate_macros(178,89.8,'Male',22,0,'Overweight_Level_II')
    print("Recommended Daily Calorie Intake", macros_cal,"Cal")
    print("Recommended Daily Protein Intake", macros_protein,"grams")
    print("Recommended Daily Carbs Intake", macros_carbs,"grams")
    print("Recommended Daily Fat Intake", macros_fat,"grams")

    x,cals,protein,carbs,fat=ga_algo(recipe_file,180,99,'Male',41,2,'Obesity_Type_I')
    print(x)
    print("Total Calories in the Meal :",cals,"Cal")
    print("Total Protein in the Meal :",protein,"grams")
    print("Total Carbs in the Meal :",carbs,"grams")
    print("Total Fat in the Meal :",fat,"grams")
    pd.set_option('display.max_columns', None)
   
