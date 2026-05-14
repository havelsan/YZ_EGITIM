import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

## generate the data
# the data (note the different sample sizes)
N1 = 30
N2 = 35

data1 = np.random.poisson(2,N1)
data2 = np.random.poisson(1,N2)

plt.plot(1+np.random.randn(N1)/10,data1,'ks',markerfacecolor='w')
plt.plot(2+np.random.randn(N2)/10,data2,'ro',markerfacecolor='w')

plt.xlim([0,3])
plt.xticks([1,2],labels=('data1','data2'))
plt.xlabel('Data group')
plt.ylabel('Data value')
plt.show()


## now for the test
U,p = stats.mannwhitneyu(data1,data2)
print(U,p)

