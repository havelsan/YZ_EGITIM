import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

## create the data
# random number data
n = 1000
data = np.random.randn(n)**2
# rank-transform the data and scale to 1
dataR = stats.rankdata(data)/n
# find the values closest to 25% and 75% of the distribution
q1 = np.argmin((dataR-.25)**2)
q3 = np.argmin((dataR-.75)**2)
# get the two values in the data
iq_vals = data[[q1,q3]]
# IQR is the difference between them
iqrange1 = iq_vals[1] - iq_vals[0]
# or use Python's built-in function ;)
iqrange2 = stats.iqr(data)
print(iqrange1,iqrange2)

