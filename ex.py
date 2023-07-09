# Corolla Price Analysis

import pandas as pd

# import data
corolla = pd.DataFrame(pd.read_csv(r"C:\Users\Hailong\OneDrive\Desktop\DMV\Cars\corolla.csv"))
# create age of car
age = 2021 - corolla["Toyota Corolla"]
# append age to table corolla
corolla["Age"] = age

corolla[["Age", "Mile", "Price"]].describe()

corolla.head(5)

