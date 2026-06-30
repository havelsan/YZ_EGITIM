import matplotlib.pyplot as plt
import numpy as np

## "discrete" entropy
# generate data
N = 1000
numbers = np.ceil( 8*np.random.rand(N)**2 )
numbers[numbers==7] = 4
plt.plot(numbers,'o')

## "discrete" entropy
# generate data
N = 1000
numbers = np.ceil( 8*np.random.rand(N)**2 )
# get counts and probabilities
u = np.unique(numbers)
probs = np.zeros(len(u))
for ui in range(len(u)):
    probs[ui] = sum(numbers==u[ui]) / N
# compute entropy
entropee = -sum( probs*
                 np.log2(probs+np.finfo(float).eps) )

# plot
plt.bar(u,probs)
plt.title('Entropy = %g'%entropee)
plt.xlabel('Data value')
plt.ylabel('Probability')
plt.show()

## for random variables
# create Brownian noise
N = 1123
brownnoise = np.cumsum( np.sign(np.random.randn(N)) )
fig,ax = plt.subplots(2,1,figsize=(4,6))
ax[0].plot(brownnoise)
ax[0].set_xlabel('Data index')
ax[0].set_ylabel('Data value')
ax[0].set_title('Brownian noise')
ax[1].hist(brownnoise,30)
ax[1].set_xlabel('Data value')
ax[1].set_ylabel('Counts')
plt.show()

### now compute entropy
# number of bins
nbins = 50
# bin the data and convert to probability
nPerBin,bins = np.histogram(brownnoise,nbins)
probs = nPerBin / sum(nPerBin)
# compute entropy
entro = -sum( probs*np.log2(probs+np.finfo(float).eps) )
print('Entropy = %g'%entro)

