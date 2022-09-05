import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index= ['a','c','e','f','h'], columns=['column1','column2','column3'])
df = df.reindex(['a','b','c','d','e','f','g','h'])
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1",axis= 1)#axis 1 is column 0 is row
result = df.drop(["column1","column2"],axis= 1) #for deleting multiple columns
result = df.drop('a',axis= 0) # deleting the rows of a index
result = df.drop(['a','b','h'],axis= 0) # deleting multiple rows of indexes


result = df.isnull() # returns t/f value if there isn't a data
result = df.notnull() # returns a boolean value if there is data in a row or column
result = df.isnull().sum()
result = df["column1"].isnull().sum()
result = df[df["column1"].isnull()] # selects the value where is null in column1
result = df[df["column1"].isnull()]["column1"]# selects the value where is null in coulmn1 and bring only column1
result = df[df["column1"].notnull()]["column1"]# selects the value where is not null in column1


result = df.dropna() # default axis value is zero,it checks if there is a nan value, it doesnt matter multiple or not deletes all the row
result = df.dropna(axis = 1) # deletes all the column if there is a nan value
result = df.dropna(how= "any") # if there is even a single nan value deletes all the row
result = df.dropna(how="all") #if there is a row full of nan value it deletes the row
result = df.dropna(subset=["column1","column2"], how= "all")
result = df.dropna(subset=["column1","column2"], how= "any")
result = df.dropna(thresh=2)
result = df.dropna(thresh=4)


result = df.fillna(value = 'no input')
result = df.fillna(value = 1)


result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()


def average(df):
    summary = df.sum().sum()
    pieces = df.size - df.isnull().sum().sum()
    return summary / pieces
result = df.fillna(value=average(df))



print(result)
