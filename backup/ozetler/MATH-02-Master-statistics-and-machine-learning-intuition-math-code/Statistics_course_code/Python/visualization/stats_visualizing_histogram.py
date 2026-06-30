import matplotlib.pyplot as plt
import numpy as np
n = 1000
data = np.exp( np.random.randn(n)/2 )

# number of histogram bins
k = 40
plt.hist(data,bins=k)
plt.show()

# another option
y,x = np.histogram(data,bins=k)
xx = (x[1:]+x[:-1])/2
plt.plot(xx,y)
plt.show()





