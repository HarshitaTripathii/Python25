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

'''
#soongle columns selection
col1=df["Name"]
print(col1)
print(type(col1))'''

'''c=0
for i in col1:
    print(f"name {c+1} is {i}")
    c=c+1'''

'''# multiple columns
dfc=df[["Name", "age"]]
print(type(dfc))
print(dfc)'''

'''# single filtering 
row1=df[df['age']>23]
print(row1)
print(type(row1))'''

'''# multiple filtering
row2=df[(df["Score"]>80)& (df["age"]>18)]
print(row2)
'''

# ADVANCED PANDAS : UPDATE : ADD : REMOVE

'''# adding using assignment
l=['A', 'B','C', 'D','E','F','G','H']
df["alpha"]=l
df["bonus"]=df["sal"]*0.01
print(df)'''

'''#using insert fucntion
l=[x*10 for x in range(1,9) ]
df.insert(0,"ID", l)
print(df)'''

#updation
'''#  df.loc[row_index, "col_name"]=new_value
df.loc[3,"Score"]=88
print(df)'''

'''# can modify the existing column as well.
df["sal"]=df["sal"]*10
print(df)'''

'''# changing age from 20 to 37
r1=df["age"]==20
df.loc[r1,"age"]=37
print(df.index)'''


'''#removing columns : rows : using df.drop(index=[], columns=[]) for multiple or df.drop(index_value, "columns_Name") for single row and column
l=df["sal"]*0.01
df.insert(4, "bonus", l)
print(df)

rowToDrop=df[df["age"]>25].index
df.drop(index=rowToDrop,columns="bonus", inplace=True)
print(df)

#deleting single row

df.drop(index=4, columns="Score", inplace=True)
print(df)'''


