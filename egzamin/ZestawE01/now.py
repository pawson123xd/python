import matplotlib.pyplot as plt
import numpy as np
roz=[38,38,40,35,37]
bars=("A","B","C","D","E")
plt.subplot(1,2,2)
plt.barh(bars,roz,color=['olive','mediumpurple','orange','green','olive'])
plt.title("wykrek 2")
plt.subplot(1,2,1)
roz1=[-35,-20,-50,-40,-45]
plt.barh(bars,roz1,color=['greenyellow','yellow','blue','mediumpurple','palevioletred'])
plt.title("wykrek 1")
plt.savefig('zdanie1.pdf')
plt.show()