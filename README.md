	# TF

This Repository contains all drills relating to the TF Prep Course.

**Contributors:**

* Author: [Abe Waziri]

* Reviewer:  [William Hoang]

##Prep Capstone Project
This project is intended to explore the concepts of data science and is a preliminary Capstone for the Thinkful Data Science Bootcamp

###Data Science Concepts:
The intent is to investigate and explore the topics of hypothesis testing and data visualization on a data set through the practice of Python programming.  

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
The data set in experiment shows whether an individual makes either more or less than $50K (USD) per year and factors in which attributes may effect that question.  The attributes considered are: age, education, race, sex, etc… 

The data is from the [2014 US census].  This project will focus on the effect of the level of education has on income. More specifically, what level of education the individual must have in order to have a 50% probability of having an income greater than $50K

###Implementation techniques:
The data set contains a sample of over 30,000 entries with 15 different attributes. I used a random sample of 1,000 of those entries to speed up the program analysis while keeping the data integrity. I used a bar chart & pie charts to visualize the population makeup of each education group. Finally, I used hypothesis tests to decide if a particular level of education resulted in a better than 50% chance of having an income greater than $50K.

###Procedures:
1. Reduce data set from 32,560 entries to 1,000 entries
2. Consolidate certain education values into buckets for better readability:
	- No-HS
	- HS-Drop Out 
	- Associate
3. List education values
4. Create python dictionary with education value as key and amount per category as value
5. Use the dictionary to create bar and pie chart represenations
6. Create binary column in data frame with a value of 1 if greater than >50K is true and 0 if false
7. Present the mean of that column grouped by education value 
8. Run a hypothesis test for each value of education

###Findings:
The majority of the sample were high school graduates and graduates with some college education. The smallest groups were those with doctorates and professional degrees:

 - **High School:** 343 People - 34.3%

 - **Some College:** 224 People - 22.4%
 
 ...
 
 ..
 

 - **Prof School:** 12 People - 12.2%

 - **Doctorate:** 12 People - 12.2%


![education charts](https://cloud.githubusercontent.com/assets/25283369/23106278/a8484f6e-f69f-11e6-9cc4-9985468b0b82.png "Sample Size Per Education Category")



The table below shows the percentage of each group with an income greater than $50K. The trend shows that those with more years of schooling have better chance of having a higher income:



![Percentage of Sample >50K Income](https://cloud.githubusercontent.com/assets/25283369/23105880/884b7ff6-f69a-11e6-8bcc-b6b8369ffbee.PNG "Percentage of Sample >50K Income")




**Hyopthesis Tests:**

There are two important values in this table: The T value and the P value. The t value measures the difference between the observed mean and the hypothesized mean. If the t value is large, then we are more likely to accept the alternate hypothesis. The p value shows how likely it is to see a more extreme mean in the direction of the alternate hypothesis assuming that the originall hypothesis is true. If the p value is small, then we are more likely to reject the original hypothesis for the alternative. The final call whether or not we should reject or accept the orignal hypothesis is set from the alpha level, also called the significance level. The higher the significance level, the stronger we need the evidence to be in order to reject our original hypothesis.


In order to reject the null hypothesis for the alternative (>50% chance to have a >50K income) the t-test must be positive and the P-Value must be below .1 at a 10% significance level. As you can see from the table below, only a doctorate or professional degree has enough evidence to show that there is a greater than 50% chance to have a 50K income. 

![Hypothesis Tests](https://cloud.githubusercontent.com/assets/25283369/23105877/859670fe-f69a-11e6-9984-55edbb4bd533.PNG "Hypothesis Tests")


###Issues and Problems: 
One recurring issue I had was dealing with the index column in the pandas data frame. When I created a random sample, the index column did not reindex to match the new sample. Instead, the index number from the original data frame stayed with its row. Instead of starting at 1 and going to 1000, the sample index was random. I circumvented this by exporting the data frame as a csv and then importing it without that index column

Another issue I spent some time dealing with was matching the values in my charts to its correct label. I tackled this by creating two lists from a grouped data frame and zipping them together into a dictionary. 


**Code Issues:**  
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


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.) 


   [William Hoang]: <https://github.com/WilliamHoang>
   [Abe Waziri]: <https://github.com/abew16>
   [2014 US census]:  <https://www.census.gov/population/projections/data/national/2014.html>
