import pandas as pd
import matplotlib.pyplot as plt
sample_data = pd.read_csv('countries.csv')
pakp = sample_data[sample_data.country == "Pakistan"].population
paky = sample_data[sample_data.country == "Pakistan"].year
plt.plot(pakp/10**3 , paky )
plt.title("Population of Pakistan")
plt.xlabel("Population")
plt.ylabel("Year")
plt.show()