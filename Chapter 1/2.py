#Accessing group of rows and columns from the Dataset

import pandas as pd

Data={
    'Student':['Jal','Mayank','Kartikeya','Heet','Mudit'],
    'Marks':[40,45,50,49,30],
    'Rank':[4,3,1,2,5]
}

df = pd.DataFrame(Data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student records:\n",df)

#Access the value in student col of row 1
print("Value =",df.loc['RowD','Student'])