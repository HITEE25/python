import pandas as pd

Data = {
    'Name' : ['A','B','C'],
    'Marks' : [45,47,49],
}

df = pd.DataFrame(Data)

#apply on specific coloumn
print(df['Marks'].apply(lambda x : x + 5))

#replace values using maping dict
print(df['Name'].map({'A':'ALICE','B':'BOB','C':'CHARLIE'}))

#apply on all entries
print(df[['Marks']].map(lambda x : x + 5))