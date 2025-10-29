#Naming your own index
import pandas as pd

#dataset
Data={
    'Student':['Jal','Mayank','Kartikeya','Heet','Mudit'],
    'Marks':[40,45,50,49,30],
    'Rank':[4,3,1,2,5]
}
                                
df = pd.DataFrame(Data,index=['s1','s2','s3','s4','s5'])
print("Student records:\n",df)