import pandas as pd

Data = {
    'Name':["alice","bob","lily","kenney"],
    'Age':[21,20,20,19],
    'Marks':[45,55,46,47]
}

df = pd.DataFrame(Data)

print(df.sort_values('Marks'))

print(df.sort_values('Marks',ascending=False))

print(df.sort_index())