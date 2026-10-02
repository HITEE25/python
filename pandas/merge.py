import pandas as pd

df1 = pd.DataFrame({
    'ID':[1,2],
    'Name':["Alice","Bob"],
})

df2 = pd.DataFrame({
    'ID':[1,2],
    'Marks':[40,50]
})

print(pd.merge(df1,df2,on='ID'))

print(pd.concat([df1,df2],axis=1))

print(df1.join(df2.set_index('ID'), on='ID'))