import pandas as pd
import os
if(os.path.exists("coffee.csv")):
    df=pd.read_csv("coffee.csv", encoding="latin1")
    print(df)
else:
    print(f"the file 'coffee.csv' does not exists")

print(pd.__version__)