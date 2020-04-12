import pandas as pd
import os
os.chdir('C:/Users/AmitPrakash/Desktop/python code')
excel_file='example.xlsx'
df=pd.read_excel(excel_file)
doc=df['Name'].where(df['Job']=='Doctor')
print(doc.dropna())

print('Below will show all Lines which match')
print(df[df['Job']=='Doctor'])
#total_count=df.groupby(['Job']).count()
##print(total_count['Name'])
#print('below is logical statment where job is Engineer then print')

