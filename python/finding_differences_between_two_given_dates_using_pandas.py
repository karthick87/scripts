import datetime as dt
import pandas as pd

d0 = dt.date(2018, 1, 1)
d1 = dt.date(2018, 2, 22)

ls = []
for i in range((d1 - d0).days):
    ls.append(d0 + dt.timedelta(days=i))

data = pd.DataFrame(data=ls)
writer = pd.ExcelWriter('Difference.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
