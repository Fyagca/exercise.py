import pandas as pd

data = pd.read_csv("nba.csv")

data.dropna(inplace= True)

#data["Name"] = data["Name"].str.upper()#makes all characters uppercase
#data["Name"] = data["Name"].str.lower()#makes all characters lowercase
#data["index"] = data["Name"].str.find('a')# finds all character indexes which contains 'a' letter
#data = data[data.Name.str.contains('Jordan')]# finds all the records which contains "Jordan"
#data = data.Team.str.replace(' ','-').str.replace('*','')
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand = True)



print(data.head(10))