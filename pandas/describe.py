import pandas as pd

data = {
    'Product':['A','B','A','C'],
    'Sales':[290,300,400,240],
    'Returns':[5,9,20,23]
}

df = pd.DataFrame(data)

#to get stactical summary
print(df[['Sales','Returns']].describe())

#occruence of product
print(df['Product'].value_counts())

#relationship between column
print(df[['Sales','Returns']].corr())
