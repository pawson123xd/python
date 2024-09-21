import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("uczniowie2.xlsx")
print(df)
dane1=df.groupby(["Rok"])['Wartość'].sum()
x=df['Rok'].sort_values().drop_duplicates()
plt.scatter(x,dane1,s=126,c="green", marker='^',label='Wartość')
plt.legend()
plt.savefig('zad2.jpg')
plt.show()