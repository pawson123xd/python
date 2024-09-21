import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df[df['Data zamowienia']>='2005- -'])
print(data)
data.to_csv('zamówienia_2005.csv')
import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(data=pd.DataFrame(df[(df['Data zamowienia']>='2004- -') & (df['Data zamowienia']<'2005- -')]))
print(data)
data.to_csv('zamówienia_2004.csv')