import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel('turystyka11.xlsx').T
data=pd.DataFrame(df)
rok=data[data[0]==2019][1]
rok2=data[data[0]==2018][1]
lista=['kategorii *****','kategorii ****','kategorii *** ','kategorii ** ','kategorii *  ']
plt.subplot(2,1,1)
plt.pie(rok,labels=lista,autopct='%1.1f%%')
plt.title('rok 2019')
plt.subplot(2,1,2)
plt.pie(rok2,labels=lista,autopct='%1.1f%%')
plt.title('rok 2018')
plt.savefig("zadanie3.jpg")
plt.show()