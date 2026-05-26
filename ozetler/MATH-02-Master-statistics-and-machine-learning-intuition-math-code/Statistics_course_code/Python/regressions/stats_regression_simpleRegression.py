import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

## example: effects of sleep on food spending
sleepHours = [5, 5.5, 6, 6, 7, 7, 7.5, 8, 8.5, 9]
dollars = [47, 53, 52, 44, 39, 49, 50, 38, 43, 40]
# start by showing the data
plt.plot(sleepHours,dollars,'ko',markerfacecolor='k')
plt.xlabel('Hours of sleep')
plt.ylabel('Fijian dollars')
plt.show()


## "manual" regression via least-squares fitting
# create the design matrix
desmat = np.vstack((np.ones(10),sleepHours)).T
print(desmat)

# compute the beta parameters (regression coefficients)
beta = np.linalg.lstsq(desmat,dollars,rcond=None)[0]
print(beta)

# predicted data values
yHat = desmat@beta


## show the predicted results on top of the "real" data
# show previous data
plt.plot(sleepHours,dollars,'ko',markerfacecolor='k')

# predicted results
plt.plot(sleepHours,yHat,'s-')

# show the residuals
for i in range(10):
    plt.plot([sleepHours[i],sleepHours[i]],[dollars[i], yHat[i]],'m--')
    
plt.legend(('Data (y)','Model ($\^{y}$)','Residuals'))
plt.xlabel('Hours of sleep')
plt.ylabel('Fijian dollars')
plt.show()

## now with scipy
slope,intercept,r,p,std_err = stats.linregress(sleepHours,dollars)
print(intercept,slope)
print(beta)

