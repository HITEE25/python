import pandas as pd

Data = {
    'Name':["alice","bob","lily","kenney"],
    'Age':[21,20,20,19],
    'Marks':[45,55,46,47]
}

df = pd.DataFrame(Data)

print(df.loc[0:1, ['Name','Marks']])

print(df.iloc[0:2 , 0:2])

print(df[df['Marks'] > 50])


