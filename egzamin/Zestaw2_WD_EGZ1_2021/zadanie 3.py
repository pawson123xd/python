import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("nieruchomosci2.csv",sep=";",decimal='.',header=None).T
df[3]= df[3].str.replace(' ', '')
df[3]=df[3].astype({3:"int"})
watorśc=df[df[0]=='rynek pierwotny'][3]
watorśc1=df[df[0]=='rynek wtórny'][3]
watorś=df[df[0]=='rynek pierwotny'][1]
watorś1=df[df[0]=='rynek wtórny'][1]
print(watorś)
plt.subplot(2,1,1)
plt.pie(watorśc, autopct='%1.1f%%',labels=watorś)
plt.title("rynek pierwotny")
plt.subplot(2,1,2)
plt.pie(watorśc1, autopct='%1.1f%%',labels=watorś1)
plt.title("rynek wtórny")
plt.savefig("zadanie3.pdf")
plt.show()