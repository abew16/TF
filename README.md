# TF

This Repository contains all drills relating to the TF Prep Course.

Author: Abe Waziri
abe.waziri@gmail.com

##Prep Capstone Project
This project is intended to explore the concepts of data science and is a preliminary Capstone for the Thinkful Data Science Bootcamp

###Data Science Concepts:
Investigated and explored the topics of hypothesis testing and data visualization as well as practicing Python programming.  

###Instructions:
file of interest(s):

 - Prep_Capstone_UnX.py

Installation:

	>>>sudo pip3 install numpy
	>>>sudo pip3 install scipy
	>>>sudo apt-get install python3-matplotlib
	>>>pip3 install pandas

Run the script:
	
	>>>python3 Prep_Capstone_UnX.py

###Environment and Dependencies:

	- Ubuntu 16.04.1
	- Python 3.5
	- numpy 1.12.0
	- scipy 0.18.1
	- matplotlib 1.5.1

###Proposal:
This data set shows whether an individual either makes more or less than 50K per year and factors which may effect that (age, education, race, sex, etc…). The data is from the 2014 census.
This project will focus on the effect of education on income. More specifically, what level of education someone must have in order to have a 50% probability of having an income greater than 50K

###Implementation techniques:
Data set contains a sample of over 30,000 with 15 different attributes. I used a random sample of 1,000 to speed up the program, while keeping the data integrity. I used a bar chart & pie charts to visualize the population makeup of each education group. Finally, I used hypothesis tests to decide if a level of education gave one a better than 50% chance of having a >50K income.

###Procedures:
1. Reduce data set from 32,560 to 1,000
2. Consolidate certain education values into buckets for better readability
  a. No-HS, HS-Drop Out Associate
3. List education values
4. Create dictionary with education value as key and amount per category as value
5. Use the dictionary to create a bar and pie chart
6. Create binary column in data frame with a value of 1 if >50K is true and 0 if false
7. Present the mean of that column grouped by education value 
8. Run a hypothesis test for each value of education

###Findings:
The majority of the sample were high school graduates and graduates with some college education. The smallest groups were those with doctorates and professional degrees:


High School: 343 People - 34.3%
Some College: 224 People - 22.4%
...
Prof School: 12 People - 12.2%
Doctorate: 12 People - 12.2%

![education charts](https://cloud.githubusercontent.com/assets/25283369/23106278/a8484f6e-f69f-11e6-9cc4-9985468b0b82.png)



The table below shows the percentage of each group with an income >50K. The trend shows that those with more years of schooling have better chance of having a higher income:

![Percentage of Sample >50K Income](https://cloud.githubusercontent.com/assets/25283369/23105880/884b7ff6-f69a-11e6-8bcc-b6b8369ffbee.PNG)




In order to reject the null hypothesis for the alternative (>50% chance to have a >50K income) the t-test must be positive and the P-Value must be below .1 at a 10% significance level. As you can see from the table below, only a doctorate or professional degree has enough evidence to show that there is a greater than 50% chance to have a 50K income. 

![Hypothesis Tests](https://cloud.githubusercontent.com/assets/25283369/23105877/859670fe-f69a-11e6-9984-55edbb4bd533.PNG)


###Issues and Problems: 
Although the data set is very clean, it only has two values for income, >50K or <=50K. If the data included values for gross income as well, we could better estimate the marginal effect of education on income. 

Code Issues:  
I wanted to create an ANOVA table using the Pyvtble however the module was not working. I left the commented code in for the future:

    import pyvttble
        # df_400_pvyt = pt.DataFrame(df_400)
    # print (df_400_pvyt.anova1way('Income_Value','Education'))
    
###Conclusion:
According to the hypothesis test, only a doctorate and a professional degree increase one's chance of having an income above 50K over 50%. That being said, in general someone with a higher level of education has a greater chance of having a higher income. 

Although the data shows this correlation, it does not definitely prove that education causes a higher income. Students who go on to have more education could be more intrinsically motivated and might be able to earn a higher income regardless. 

###Further Study:
How has the effect of education on income changed over time? The ratio of people with a bachelor's degree has increased dramatically over the past half century. Using the same data in this set from differnet years can give us an understanding of how the value of  degree has changed over time. 

Education is correlated with other factors in this data set, especially age. In the future it would be useful to de-correlate these variables and identify each effect individually.

What is the marginal effect of education on income? If we had the gross income's of each person in the sample, we could calculate the marginal effect of education on income. Calculating this effect can help prospective students gain a better understanding about the ROI on their education. 




