import pandas as pd

list = [["Ahmet",50],["Ali",60],["Yağmur",70]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[60,50,70,90]}
dict_list =[

    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":50},
    {"Name":"Yağmur","Grade":50},
    {"Name":"Çınar","Grade":50},


            ]

# df = pd.DataFrame(list)
#df = pd.DataFrame(dict)
#df = pd.DataFrame(dict_list)
#df = pd.DataFrame(dict_list,index=["212","155","911","400"])
df = pd.read_csv("data.csv")
print(df)