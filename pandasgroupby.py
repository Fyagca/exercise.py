import pandas as pd
import numpy as np
staff = {
    'Employee': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Department':['Human Resources','IT','Accounting','Human Resources','IT','Accounting','Human Resources'],
    'Age':['30','25','45','50','23','34','42'],
    'District': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Salary': [5000,3000,4000,3500,2750,6500,4500]
}


df = pd.DataFrame(staff)
result = df
result = df["Salary"].sum()
result = df.groupby("Department").groups
result = df.groupby(["Department","District"]).groups
districts = df.groupby("District")
department = df.groupby("Department")
# visualize the staff info depending on districts
for name, group in districts:
    print(name)
    print(group)
# visualize the staff info depending on departments
for name, group in department:
    print(name)
    print(group)
# select employees with query where District =  "Kadıköy"
result = df.groupby("District").get_group("Kadıköy")
# where Department = "Accounting"
result = df.groupby("Department").get_group("Accounting")
result = df.groupby("Department").sum()
result = df.groupby("Department").mean()
result = df.groupby("Department")["Salary"].mean()
result = df.groupby("District")["Age"].mean()
result = df.groupby("District")["Employee"].count()
result = df.groupby("Department")["Age"].max()
result = df.groupby("Department")["Salary"].min()["Accounting"]
result = df.groupby("Department").agg(np.mean)
result = df.groupby("Department")["Salary"].agg([np.sum,np.mean,np.max,np.min])
print(result)