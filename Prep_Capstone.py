import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

## Show a Distrubtion of values for Age
raw_input('\nDistrubtion of Age:')
cols = ['Age']
print (df[cols].describe())

raw_input('\nBox Plot:')
plt.boxplot(df['Age'])
plt.ylabel('Age')
plt.yticks([10,20,30,40,50,60,70,80,90,100],[10,20,30,40,50,60,70,80,90,100])
plt.ylim((0,100))
plt.savefig('Age Box Plot.png')
# plt.show()

raw_input('\nEducation Levels:')
## Create buckets for people who didn't go to HS or dropped out
no_hs = ['1st-4th', '5th-6th', '7th-8th', 'Preschool']
hs_drop_out = ['9th', '10th', '11th', '12th']
masters = ['Masters', 'Prof-school']
associate = ['Assoc-acdm', 'Assoc-voc']
df = df.replace(no_hs, 'No-HS')
df = df.replace(hs_drop_out, 'HS-DropOut')
df = df.replace(associate, 'Associate')

## Check buckets and view unique values for Education
education_names = []
for col in df.columns:
    if col == 'Education':
        unique_values = sorted(df[col].unique())
        education_names.append(unique_values)
        print('Education : {}').format(unique_values)

## Create bar chart for Education
x_length = np.arange(len(df['Education'].unique()))
df_grouped = df.groupby('Education').count()
education_values = []
for index, row in df_grouped.iterrows():
        education_values.append(row['Age'])
plt.bar(x_length, education_values, width=.35, align='center')
plt.xticks(x_length, education_names[0], rotation=45, fontsize='small')
plt.savefig('Education Bar Chart.png')
# plt.show()

raw_input('\nENTER')
df_filtered = df[df['Income']=='>50K']
df__grouped = df_filtered.groupby('Education').count()
df_percentages = df__grouped / df_grouped



