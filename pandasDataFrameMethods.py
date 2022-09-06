import pandas as pd
import numpy as np

data1 = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 13, 20, 25],
    "Column3": ["abc", "bca", "ade", "cba", "dea"]
}
df = pd.DataFrame(data1)


def square(x):
    return x * x


square2 = lambda x: x * x

result = df
result = df["Column2"].unique()  # brings data that is not recurring
result = df["Column2"].nunique()  # brings data that is beeing unique
result = df["Column2"].value_counts()  # counts the recurring value for each data
result = df["Column1"] * 2  # multiplies the datas with 2
result = df["Column1"].apply(square)  # with apply we can process a function for each data
result = df["Column1"].apply(square2)
df["Column4"] = df["Column3"].apply(len)  # counts the amount of character for each data
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3")  # sorts alphabetically because all the values are string
result = df.sort_values("Column3", ascending=False)  # sorts ascending

data = {
    "Ay": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan"],
    "Kategori": ["Elektronik", "Elektronik", "Elektronik", "Kitap", "Kitap", "Kitap", "Giyim", "Giyim", "Giyim"],
    "Gelir": [20, 30, 15, 14, 32, 42, 12, 36, 52]
}

df = pd.DataFrame(data)

df = df.pivot_table(index="Ay", columns="Kategori", values="Gelir")

result = df
print(result)
