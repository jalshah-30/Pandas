#Creating pandas dataframe 

import pandas as pd

#dataset

Data={
    'Student':['Jal','Mayank','Kartikeya','Heet','Mudit'],
    'Marks':[40,45,50,49,30],
    'Rank':[4,3,1,2,5]
}

df = pd.DataFrame(Data)
# print(Data)
print("Student Data Records 2025\n",df)