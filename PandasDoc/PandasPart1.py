import pandas as pd
import os 


data={
    "Name" : ["harshita", "Anubhav", "dhruv", "Rishi"],
    "Age" :[21, 22,20,23],
    "City" :["Noida", "Delhi", "Ghaziabad", "Jaipur" ]
    }
df=pd.DataFrame(data)
print(df)
print(os.getcwd())
# df.to_csv(r"c:\Users\91912\Desktop\python -25\Python25\PandasDoc\Details.csv", index=False)
df.to_excel(r"c:\Users\91912\Desktop\python -25\Python25\PandasDoc\Details.xlsx", index=False)
df.to_json(r"c:\Users\91912\Desktop\python -25\Python25\PandasDoc\Details.json", index=False)
