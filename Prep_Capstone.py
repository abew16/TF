import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# adult = '/home/abew16/python practice/adult.csv'
adult_local = 'C:\Users\Abe\Google Drive\Python\Data_Science\Data_Sets\Adult.csv'

df = pd.read_csv(adult_local)
number_of_rows = df.shape[0]
number_of_columns = df.shape[1]

print('There are {} rows and {} columns.'.format(number_of_rows, number_of_columns))

df.index.name = 'Index'
#df.columns = map(str.capitalize, df.columns)
df.columns = [col.capitalize() for col in df.columns]

cols = ['Age']
percentiles = [.1,.2,.25,.3,.4,.5,.6,.7,.75,.8,.9]
for col in cols:
    print (col + ':')
    print (df[col].describe(percentiles=percentiles))
    print ('-' * 20 + '\n')

#df['Age'].hist(color='k', alpha=0.5, bins=50)
plt.boxplot(df['Age'])
plt.ylabel('Age')
plt.yticks([10,20,30,40,50,60,70,80,90,100],[10,20,30,40,50,60,70,80,90,100])
plt.ylim((0,100))
plt.show()
