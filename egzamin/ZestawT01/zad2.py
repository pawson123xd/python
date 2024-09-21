import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
df=pd.read_excel("mieszkania1.xlsx")
data=df[df["Rok"]==2016].groupby(["Formy budownictwa"])['Wartość'].sum()
Formybudownictwa=df["Formy budownictwa"].sort_values().drop_duplicates()
plt.pie(data,labels=Formybudownictwa,autopct="%1.1f%%")
plt.title("Porownanie ceny mieszkania w 2016")
plt.savefig("zad2.pdf")
plt.show()