import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
dane=[50,42,39,21,25,30]
dane1=[21,33,45,78,70,50]
misiace=['Styczeń',"Luty","Marzec","Kwiecień","Maj","Czerwiec"]
plt.plot(misiace,dane,linestyle='--',label="Filmy",color="blue")
plt.plot(misiace,dane1,label="Gry",color="g")
plt.grid(True)
plt.ylim(0,100)
plt.xlabel('Miesiąc')
plt.ylabel('Zyski')
plt.title("Zyski z filmów,i gier")
plt.legend()
plt.savefig("zad1.pdf")
plt.show()