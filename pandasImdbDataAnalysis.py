import pandas as pd

df = pd.read_csv("imdbTop250.csv")
result = df
result = df.columns # shows the columns
result = df.info # shows info
result = df.head(5) # shows first 5 record on top
result = df.tail() # shows last 5 record on bot
result = df.head(10) # shows first 10 record on top
result = df["Title"] # shows the info of Title column only
result = df["Title"].head() # shows first 5 record of title column
result = df[["Title","Rating"]] # shows title and rating columns
result = df[["Title","Rating"]].tail(7) # last 7 record of selected columns
result = df[5:20][["Title","Rating"]].head() # shows first 5 column after seeking 5 columns
result = df[df["Rating"]>= 8.0][["Title","Rating"]].head(50) #first 50 record of info with filtering
result = df[(df["Date"] >= 2014) & (df["Date"]<= 2015)][["Title","Date"]]
print(result)