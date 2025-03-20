import pandas as pd
import os 


data1={
    "Name" : ["harshita", "Anubhav", "dhruv", "Rishi"],
    "Age" :[21, 22,20,23],
    "City" :["Noida", "Delhi", "Ghaziabad", "Jaipur" ]
    }
df1=pd.DataFrame(data1)
# print(df1)

# print(df1.info())

data={
    "Name" :["yash", "riya", "raj", "dev", "prabhu", "dhruv", "yashi" , "harshit"],
    "age":[22,25,20,33,24,20,21,20],
    "Score":[99,67,85,34,22,55,90,95],
    "sal":[5500,6699,4433,7890,2356,8899,99999,548907]
}
df=pd.DataFrame(data)
print(df)
print(df.describe())
