import pandas as pd

data = {
    'Name': ["hitee","mihu",None,"vency"],
    'Age': [25,None,25,30],
    'city': ["la","ny","daman","anand"]
}

df = pd.DataFrame(data)
print(df)

#fill None in name with unknown
df['Name'].fillna('unknown',inplace=True)

#fill None in age with mean
df['Age'].fillna(df['Age'].mean(),inplace=True)

#remove duplicate
df.drop_duplicates(inplace=True)

#cover age to int
df['Age'] = df['Age'].astype(int)

print(df)
