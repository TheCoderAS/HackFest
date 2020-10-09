import numpy as np
import matplotlib.pyplot as plt
year=np.array([2015,2016,2017,2017,2018,2019,2020])
tata=np.array([1000,2000,3000,2500,4000,3000,6000])
bmw=np.array([500,1000,3000,2000,4000,3000,3000])
merd=np.array([5000,4000,3000,2700,2100,1000,4000])
ford=np.array([3000,3000,1111,2999,3000,1000,2000])

plt.bar(year,tata,label="tata",width=.7,edgecolor="black")
plt.bar(year,bmw,label="bmw",width=.5,edgecolor="black",bottom=tata)
plt.bar(year,merd,label="merd",width=.3,edgecolor="black",bottom=tata+bmw)
plt.bar(year,ford,label="ford",width=.2,edgecolor="black",bottom=tata+bmw+merd)
plt.xlabel("year")
plt.ylabel("unit sold")
plt.grid()
plt.legend()
plt.show()