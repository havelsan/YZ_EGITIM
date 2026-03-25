import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

## create the data
n = 1000
thresh = 5 # threshold for cropping data
data = np.exp( np.random.randn(n) )
data[data>thresh] = thresh + np.random.randn(sum(data>thresh))*.1
# show histogram
plt.hist(data,30)
plt.title('Histogram')
plt.show()

# show violin plot
plt.violinplot(data)
plt.title('Violin')
plt.show()

# another option: swarm plot
import seaborn as sns
sns.swarmplot(data,orient='v')

