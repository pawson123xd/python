import pandas as pd
import numpy as np
df=pd.read_csv('IMIONA_ur_01.01.2019-30.06.2019.csv')
data=pd.DataFrame(df)
print(df[df['Liczba']>1000]) 
import pandas as pd
import numpy as np
df=pd.read_csv('IMIONA_ur_01.01.2019-30.06.2019.csv')
data=pd.DataFrame(df)
print(data[data['Imie']=='PAWEŁ'])
import pandas as pd
import numpy as np
df=pd.read_csv('IMIONA_ur_01.01.2019-30.06.2019.csv')
data=pd.DataFrame(df['Liczba']).sum()
print(data)
import pandas as pd
import numpy as np
df=pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')
data=pd.DataFrame(df)
print(data[(data['Rok']>=2000) & (data['Rok'])<=2005]['Liczba'].sum())
import pandas as pd
import numpy as np
df=pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')
data=pd.DataFrame(df)
print(data[(data['Płeć']=='M')]['Liczba'].sum())
print(data[(data['Płeć']=='K')]['Liczba'].sum())


import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
print(data.sort_values(by='Utarg',ascending=False).head())
import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
print(data.groupby(['Sprzedawca'])['Utarg'].count())

import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
print(data.groupby(['Kraj'])['Utarg'].sum())

import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
print(data[(data['Data zamowienia']>='2005- -') & (data['Kraj']=='Polska')].groupby(['Sprzedawca'])['Utarg'].sum())

import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
print(data[(data['Data zamowienia']>='2004- -') & (data['Data zamowienia']<'2005- -')]['Utarg'].mean())
