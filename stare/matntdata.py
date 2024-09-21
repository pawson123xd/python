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
