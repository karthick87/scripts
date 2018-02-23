import pandas as pd
 
df = pd.read_excel("output.xlsx")
date1 = df.loc[0, 'Start_Date']
date2 = df.loc[0, 'End_Date']

data = pd.DataFrame(data=pd.date_range(date1, date2))
data1 = data
writer = pd.ExcelWriter('Difference.xlsx', engine='xlsxwriter')
data1.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
