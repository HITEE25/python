import pandas as pd

data = {
    'Dept':['hr','it','it','fina'],
    'Name':['mihu','alice','bob','vency'],
    'Salary':[95000,9000,9000,55000]
}

df = pd.DataFrame(data)

filtered = df[df['Salary'] > 9000]
print(filtered[['Name','Salary']])

group = df.groupby('Dept')[['Salary']].mean()
print(group)

sort = df.sort_values('Salary',ascending=True)
print(sort)