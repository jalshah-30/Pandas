#Iterating loops to display columns

import pandas as pd

#dataset
Data={
    'Student':['Jal','Mayank','Kartikeya','Heet','Mudit'],
    'Marks':[40,45,50,49,30],
    'Rank':[4,3,1,2,5]
}
                             #  0       1     2      3      4     
df = pd.DataFrame(Data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student records:\n",df)

#iterating
print("Using Iteration:\n")
for col in df:
    print(col)
