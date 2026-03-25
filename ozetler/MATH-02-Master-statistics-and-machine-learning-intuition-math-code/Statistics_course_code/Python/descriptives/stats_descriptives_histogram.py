import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

## create some data
# number of data points
n = 1000
# number of histogram bins
k = 40
# generate log-normal distribution
data = np.exp( np.random.randn(n)/2 )
# one way to show a histogram
plt.hist(data,k)
plt.xlabel('Value')
plt.ylabel('Count')
plt.show()

## try the Freedman-Diaconis rule
r = 2*stats.iqr(data)*n**(-1/3)
b = np.ceil( (max(data)-min(data) )/r )
plt.hist(data,int(b))
# or directly from the hist function
#plt.hist(data,bins='fd')
plt.xlabel('Value')
plt.ylabel('Count')
plt.title('F-D "rule" using %g bins'%b)
plt.show()

# small aside on Seaborn
import seaborn as sns
sns.displot(data) # uses FD rule by default

## lots of histograms with increasing bins
bins2try = np.round( np.linspace(5,n/2,30) )
fig, axs = plt.subplots(5,int(len(bins2try)/5))
for bini in range(len(bins2try)):
    i,j=int(bini%5),int(bini/5)
    y,x = np.histogram(data,int(bins2try[bini]))
    x = (x[:-1]+x[1:])/2
    axs[i,j].plot(x,y,'.-')
    axs[i,j].set_title(str(bini))

plt.show()
