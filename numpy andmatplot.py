
import matplotlib.pyplot as plt

year = [2015, 2016, 2017, 2018, 2018, 2019]
tata = [1000, 2000, 2500, 1000, 2000, 1500]
benz = [2000, 1000, 1500, 3000, 2000, 1000]
ford = [3000, 1500, 1500, 2400, 1000, 2000]
suz = [1200, 2000, 2000, 3200, 1500, 700]
"""
plt.plot(year, tata,label="tata",linestyle="-",marker="o")
plt.plot(year, benz,label="benz",linestyle=":",marker="+")
plt.plot(year, ford,label="ford",linestyle="-.",marker="d")
plt.plot(year, suz,label="suz",linestyle="--",marker="^")
plt.title("No. of unit sold per year")
plt.ylabel("unit sold")
plt.xlabel("year")
plt.legend()
plt.grid()
plt.show()"""
plt.subplot(2,2,1)
plt.plot(year, tata,label="tata",linestyle="-",marker="o")

plt.subplot(2,2,1)
plt.plot(year, benz,label="benz",linestyle="--",marker="o")

plt.subplot(2,2,1)
plt.plot(year, ford,label="ford",linestyle=":",marker="o")

plt.subplot(2,2,1)
plt.plot(year, suz,label="suz",linestyle="-.",marker="o")

plt.title("car sold record for last 6 years")
plt.xlabel("year")
plt.ylabel("unit sold")
plt.legend()
plt.grid()
plt.show()