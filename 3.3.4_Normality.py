import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 8))

plt.subplot(3, 3, 1)
binomialvar = np.random.binomial(6, .16666,[100])
plt.hist(binomialvar)
plt.axvline(binomialvar.mean(), color = 'b', linestyle='solid', linewidth=2)
plt.axvline(binomialvar.mean() + binomialvar.std(), color = 'b', linestyle ='dashed', linewidth=1)
plt.axvline(binomialvar.mean() - binomialvar.std(), color = 'b', linestyle='dashed', linewidth=1)
plt.title('Binomial')

plt.subplot(3, 3, 2)
multinomialvar = np.random.multinomial(20, [.344, .211, .11],[100])
plt.hist(multinomialvar)
plt.axvline(multinomialvar.mean(), color = 'b', linestyle='solid', linewidth=2)
plt.axvline(multinomialvar.mean() + binomialvar.std(), color = 'b', linestyle ='dashed', linewidth=1)
plt.axvline(multinomialvar.mean() - binomialvar.std(), color = 'b', linestyle='dashed', linewidth=1)
plt.title('multinomial')

plt.subplot(3, 3, 3)
paretovar = np.random.pareto(1,[100])
plt.hist(paretovar)
plt.axvline(paretovar.mean(), color = 'b', linestyle='solid', linewidth=2)
plt.axvline(paretovar.mean() + binomialvar.std(), color = 'b', linestyle ='dashed', linewidth=1)
plt.axvline(paretovar.mean() - binomialvar.std(), color = 'b', linestyle='dashed', linewidth=1)
plt.title('pareto')

plt.subplot(3, 3, 4)
betavar = np.random.beta(10,5,[100])
plt.hist(betavar)
plt.axvline(betavar.mean(), color = 'b', linestyle='solid', linewidth=2)
plt.axvline(betavar.mean() + binomialvar.std(), color = 'b', linestyle ='dashed', linewidth=1)
plt.axvline(betavar.mean() - binomialvar.std(), color = 'b', linestyle='dashed', linewidth=1)
plt.title('beta')

plt.subplot(3, 3, 5)
geometricvar = np.random.geometric(.256,[100])
plt.hist(geometricvar)
plt.axvline(geometricvar.mean(), color = 'b', linestyle='solid', linewidth=2)
plt.axvline(geometricvar.mean() + binomialvar.std(), color = 'b', linestyle ='dashed', linewidth=1)
plt.axvline(geometricvar.mean() - binomialvar.std(), color = 'b', linestyle='dashed', linewidth=1)
plt.title('geometric')

plt.subplot(3, 3, 6)
logseriesvar = np.random.logseries(.256,[100])
plt.hist(logseriesvar)
plt.axvline(logseriesvar.mean(), color = 'b', linestyle='solid', linewidth=2)
plt.axvline(logseriesvar.mean() + binomialvar.std(), color = 'b', linestyle ='dashed', linewidth=1)
plt.axvline(logseriesvar.mean() - binomialvar.std(), color = 'b', linestyle='dashed', linewidth=1)
plt.title('logseries')

plt.show()

norm_onevar = np.random.normal(5, .5, [100])
norm_twovar = np.random.normal(10, 1, [100])
new_normvar = norm_twovar + norm_twovar
plt.hist(new_normvar)
plt.axvline(new_normvar.mean(), color = 'b', linestyle = 'solid', linewidth=2)
plt.axvline(new_normvar.mean() + new_normvar.std(), color = 'b', linestyle = 'dashed', linewidth=1)
plt.axvline(new_normvar.mean() - new_normvar.std(), color = 'b', linestyle = 'dashed', linewidth=1)

plt.show()
