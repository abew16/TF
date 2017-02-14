import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator

# adult = '/home/abew16/python practice/adult.csv'
adult_local = 'C:\Users\Abe\Google Drive\Python\Data_Science\Data_Sets\Adult.csv'
df = pd.read_csv(adult_local)

## capitalize headers for legibility
df.index.name = 'Index'
df.columns = [col.capitalize() for col in df.columns]

## General make up of data set
raw_input('Welcome to my capstone. Press ENTER to start:')
number_of_rows = df.shape[0]
number_of_columns = df.shape[1]
print('\nThere are {} rows and {} columns. \n'.format(number_of_rows, number_of_columns))
raw_input('Data in this set: (Press ENTER) \n')
print('Columns:')
for col in df.columns:
    print('{}').format(col)

raw_input('\nCreate Sample Data Frame')
df_400 = df.sample(n=400)
df_400.to_csv('C:\Users\Abe\Google Drive\Python\Data_Science\Data_Sets\Adult_Trimmed.csv')
usecols = df.columns
df_400 = pd.read_csv('C:\Users\Abe\Google Drive\Python\Data_Science\Data_Sets\Adult_Trimmed.csv', usecols=usecols)
print ('There are {} rows now').format(df_400.shape[0])

## Show a Distrubtion of values for Age
raw_input('\nDistrubtion of Age:')
cols = ['Age']
print (df[cols].describe())

raw_input('\nDistrubtion of Age for sample:')
cols = ['Age']
print (df_400[cols].describe())

## Create a box plot
raw_input('\nBox Plot:')
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.boxplot(df_400['Age'])
plt.title('Sample')
plt.ylabel('Age')
plt.yticks([10,20,30,40,50,60,70,80,90,100],[10,20,30,40,50,60,70,80,90,100])
plt.ylim((0,100))

plt.subplot(1, 2, 2)
plt.boxplot(df['Age'])
plt.ylabel('Age')
plt.title('Population')
plt.yticks([10,20,30,40,50,60,70,80,90,100],[10,20,30,40,50,60,70,80,90,100])
plt.ylim((0,100))
plt.savefig('C:\Users\Abe\Google Drive\Python\Data_Science\Charts\Prep_Capstone\Age Box Plot.png')
plt.show()


## Create buckets for people who didn't go to HS or dropped out
no_hs = ['1st-4th', '5th-6th', '7th-8th', 'Preschool']
hs_drop_out = ['9th', '10th', '11th', '12th']
associate = ['Assoc-acdm', 'Assoc-voc']
df_400 = df_400.replace(no_hs, 'No-HS')
df_400 = df_400.replace(hs_drop_out, 'HS-DropOut')
df_400 = df_400.replace(associate, 'Associate')

## Check buckets and view unique values for Education
raw_input('\nEducation Levels:')
for col in df_400.columns:
    if col == 'Education':
        education_names = sorted(df_400[col].unique())
        print('Education : {}').format(education_names)
df_grouped = df_400.groupby('Education').count()
## Get Amounts for each education value
education_values = []
for index, row in df_grouped.iterrows():
        education_values.append(row['Age'])
## Create a dictionary with the Education Value Names as keys and amounts as values
education_dictionary = dict(zip(education_names, education_values))
## Sorted list of tuples
sorted_education = sorted(education_dictionary.items(), key=operator.itemgetter(1))

# Create bar chart for Education
x_length = range(len(sorted_education))
education_values = zip(*sorted_education)[1]
print (education_values)
education_names = zip(sorted_education)[0]
# plt.bar(x_length, education_values, width=.35, align='center')
# plt.xticks(x_length, education_names, rotation=45, fontsize='small')
# plt.savefig('C:\Users\Abe\Google Drive\Python\Data_Science\Charts\Prep_Capstone\Education Bar Chart.png')
# plt.show()

raw_input('\nENTER')
df_filtered = df[df['Income']=='>50K']
df__grouped = df_filtered.groupby('Education').count()
df_percentages = df__grouped / df_grouped
