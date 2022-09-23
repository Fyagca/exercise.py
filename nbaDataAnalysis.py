import pandas as pd

data = pd.read_csv("nba.csv")
df = pd.DataFrame(data)
firstTenRec = df.head(10)  # 10 records from head
totalRecords = len(df.index)  # total records
averageSalary = df["Salary"].mean()
maxSalary = df["Salary"].max()
maxSalaryPlayer = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]
a = df[(df["Age"] >= 20) & (df["Age"] <= 25)][["Name", "Team", "Age"]].sort_values("Age", ascending=False)
b = df[df["Name"] == "John Holland"][["Name", "Team"]]  # .iloc[0] also works # find the players team.
c = df.groupby("Team").mean()["Salary"]  # average salary for each team
d = len(df.groupby("Team"))  # Also df["Team"].nunique() works for finding the number of teams
e = df["Team"].value_counts()  # counting the value numbers which matches with values
df.dropna(inplace=True)


# f = df[df["Name"].str.contains("and")] # names which contains "and"
def str_find(name):
    if "and" in name.lower():
        return True
    return False


result = df[df["Name"].apply(str_find)]
print(result)
