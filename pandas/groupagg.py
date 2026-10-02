import pandas as pd

df = pd.DataFrame({ 
    'Dept': ['HR','IT','HR','IT'], 
    'Salary': [50000,60000,55000,65000] 
})

#department wise printing average salary
print(df.groupby('Dept')['Salary'].mean())

#applying multple function
print(df.groupby('Dept').agg({'Salary': ['sum','count','mean']}))



