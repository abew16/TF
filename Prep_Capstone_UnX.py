import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import operator
# from pyvttbl import anova1way

adult = '/home/abew16/python practice/Data_Sets/adult.csv'
df = pd.read_csv(adult)

## capitalize headers
df.index.name = 'Index'
df.columns = [col.capitalize() for col in df.columns]

## Create sample from data set
input('\nCreate Sample Data Frame')
df_400 = df.sample(n=400)
df_400.to_csv('/home/abew16/python practice/Data_Sets/Adult_Trimmed.csv')
usecols = df.columns
df_400 = pd.read_csv('/home/abew16/python practice/Data_Sets/Adult_Trimmed.csv', usecols=usecols)
print (df_400.head())
#print ('There are {} rows now').format(df_400.shape[0])

## Create buckets for people who didn't go to HS or dropped out
no_hs = ['1st-4th', '5th-6th', '7th-8th', 'Preschool']
hs_drop_out = ['9th', '10th', '11th', '12th']
associate = ['Assoc-acdm', 'Assoc-voc']
df_400 = df_400.replace(no_hs, 'No-HS')
df_400 = df_400.replace(hs_drop_out, 'HS-DropOut')
df_400 = df_400.replace(associate, 'Associate')

## Check buckets and view unique values for Education
input('\nEducation Levels:')
for col in df_400.columns:
    if col == 'Education':
        education_names = sorted(df_400[col].unique())
        print('Education : {}'.format(education_names))
df_grouped = df_400.groupby('Education').count()
## Get Amounts for each education value
education_values = []
for index, row in df_grouped.iterrows():
        education_values.append(row['Age'])
education_dictionary = dict(zip(education_names, education_values))
sorted_education = sorted(education_dictionary.items(), key=operator.itemgetter(1))

input('\nCharts for amount of people per Education Level')
# Create bar chart for Education
x_length = range(len(sorted_education))
education_values = list(zip(*sorted_education))[1]
education_names = list(zip(*sorted_education))[0]
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.bar(x_length, education_values, width=.35, align='center')
plt.xticks(x_length, education_names, rotation=45, fontsize='small')
plt.ylabel('Amount / Education Level')
plt.subplot(1, 2, 2)
# Create pie chart for education and put on the same chart as the bar above
plt.pie(education_values, labels=education_names, autopct='%1.1f%%')
plt.savefig('/home/abew16/python practice/charts/Education Charts.png')
plt.tight_layout()
plt.show()

## Create new column replacing 1 for >50K and 0 for <=50K
input('\nPercentage of sample with income >50K per education level:')
income_list = df_400['Income']
income_list = [1 if x == '>50K' else 0 for x in income_list]
df_400['Income_Value'] = income_list
df_grouped = df_400.groupby('Education').mean()
df_grouped = df_grouped.sort_values('Income_Value', ascending=False)['Income_Value']
print (df_grouped)

## Print the value of all the hypothesis tests
input('\nHypothesis Tests:')
df_education_values = pd.DataFrame()
education_names = df_grouped.index.values
for education in education_names:
    df_education = list(df_400.ix[lambda df: df_400['Education']==education,'Income_Value'])
    print ('{}: T-Stat:{}, P-Value:{}'.format(education, list(stats.ttest_1samp(df_education, .5))[0], list(stats.ttest_1samp(df_education, .5))[1]))

# input('\nANOVA')
# df_400_pvyt = pt.DataFrame(df_400)
# print (df_400_pvyt.anova1way('Income_Value','Education'))
