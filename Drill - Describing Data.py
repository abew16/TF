import numpy as np
import pandas as pd
from collections import Counter

ages = [14, 12, 11, 10, 8, 6, 8]

df = pd.DataFrame(ages)
df.columns = ['ages']

mean_ages = np.mean(df['ages'])
median_ages = np.median(df['ages'])
data = Counter(df['ages'])
mode_ages = data.most_common(1)
mode_ages = mode_ages[0][0]

print ('Orignal values')
print ('Median: {}').format(median_ages)
print ('Mean: {}').format(mean_ages)
print ('Mode: {}\n').format(mode_ages)

ages = [14, 12, 11, 10, 8, 7, 8]

df = pd.DataFrame(ages)
df.columns = ['ages']

mean_ages = np.mean(df['ages'])
median_ages = np.median(df['ages'])
data = Counter(df['ages'])
mode_ages = data.most_common(1)
mode_ages = mode_ages[0][0]

print ('Values after Cindys birthday')
print ('Median: {}').format(median_ages)
print ('Mean: {}').format(mean_ages)
print ('Mode: {}\n').format(mode_ages)

ages = [14, 12, 11, 10, 8, 6]

df = pd.DataFrame(ages)
df.columns = ['ages']

mean_ages = np.mean(df['ages'])
median_ages = np.median(df['ages'])
data = Counter(df['ages'])
mode_ages = data.most_common(1)
mode_ages = mode_ages[0][0]

print ('Values after removing Oliver')
print ('Median: {}').format(median_ages)
print ('Mean: {}').format(mean_ages)
print ('Mode: {}').format(mode_ages)
