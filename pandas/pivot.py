import pandas as pd

df = pd.DataFrame({
    'dept':['hr','hr','it','it'],
    'salary':[2000,2200,1000,1100],
    'year':[2022,2023,2022,2023]
})

print(pd.pivot_table(df,values='salary',index='dept',columns='year',aggfunc='mean'))