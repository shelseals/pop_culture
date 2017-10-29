
# coding: utf-8

# In[1]:

#US Baby Names x IMDB Highest-Grossing Films

#What is the most popular name in each state 1992-2002?
#What is the most popular name in US 1992-2002?

#What state has most influence on popular names in US 2000-2002?
#Are boys more likely to have the same names than girls?

#What was the highest grossing movie 2000-2002?
#What is the name of the top actors in the highest grossing movie 1992-2002?

import pandas as pd
import seaborn as sns
import numpy as np

from collections import Counter

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

data_natl = pd.read_csv('NationalNames.csv')
data_state = pd.read_csv('StateNames.csv')


# In[3]:

data_natl.head()


# In[17]:

data_state_2000 = data_state.loc[data_state['Year'] == 2000]

data_state_2000.head()


# In[11]:

#{1992: {name1: count1,...,namek: countk},...2002: {name1: count1,...,namek: countk}}
girl_names_by_year = dict()
for year in range(1992, 2003):
    print(year) #Check to make sure it works
    girl_names_by_year[year] = dict()
    #filling dictionary containing names with their counts for each year
    for index, row in data_natl.iterrows():
        if row['Year'] == year and row['Gender'] == 'F':
            girl_names_by_year[year][row['Name']] = row['Count']
            
boy_names_by_year = dict()
for year in range(1992, 2003):
    print(year) 
    boy_names_by_year[year] = dict()
    #filling dictionary containing names with their counts for each year
    for index, row in data_natl.iterrows():
        if row['Year'] == year and row['Gender'] == 'M':
            boy_names_by_year[year][row['Name']] = row['Count']
        


# In[13]:

print('Top girl names 1992-2002')
for year in girl_names_by_year:
    top_3_girl = Counter(girl_names_by_year[year]).most_common(3)
    print(year)
    print(top_3_girl)
    
print('Top boy names 1992-2002')
for year in boy_names_by_year:
    top_3_boy = Counter(boy_names_by_year[year]).most_common(3)
    print(year) 
    print(top_3_boy)


# In[18]:

#{AL: {2002: {name1: count1,...,namek: countk}},...}

state_list = list()
for index, row in data_state_2000.iterrows():
    if row['State'] not in state_list:
        state_list.append(row['State'])
        
#filling dictionary containing names with their counts for 2000 only          
girl_names_by_state = dict()
for state in state_list:
    girl_names_by_state[state] = dict()
    for index, row in data_state_2000.iterrows():
        if row['State'] == state and row['Gender'] == 'F':
            girl_names_by_state[state][row['Name']] = row['Count']
    print('one state')
                
#print('check')
#print(list(girl_names_by_state.keys()))


# In[7]:

print(girl_names_by_state['AK'])


# In[19]:

#{AL: {2002: {name1: count1,...,namek: countk}},...}

#state_list = list()
#for index, row in data_state_2000.iterrows():
    #if row['State'] not in state_list:
        #state_list.append(row['State'])
        
#filling dictionary containing names with their counts for 2000 only          
boy_names_by_state = dict()
for state in state_list:
    boy_names_by_state[state] = dict()
    for index, row in data_state_2000.iterrows():
        if row['State'] == state and row['Gender'] == 'M':
            boy_names_by_state[state][row['Name']] = row['Count']
    print('one state')


# In[21]:

print('Top girl names 2000 by state')
for state in girl_names_by_state:
    top_3s_girl = Counter(girl_names_by_state[state]).most_common(3)
    print(state)
    print(top_3s_girl)
    
print('Top boy names 2000 by state')
for state in boy_names_by_state:
    top_3s_boy = Counter(boy_names_by_state[state]).most_common(3)
    print(state)
    print(top_3s_boy)


# In[ ]:

# Girls results
#2000 national: Emily', 25952), ('Hannah', 23073), ('Madison', 19967)
#States with 3 in common with nat'l in 2000: KS, MO, OK, MI, WV, PA, SC, OR, ID, AR, WA, UT, GA, NV, AK, TN, CO, IA, KY
    #IN, OH, NE, NC
#States with 2 in common: LA, RI, MT, FL, ND, SD, VA, NH, MN, ME, MA, MD, TX, MS, AL, WY
    #IL
#States with 1 in common: VT, DE, NY, CT, CA, NJ, AZ
#States with 0 in common: DC, NM, HI
#DC [('Kayla', 74), ('Katherine', 56), ('Elizabeth', 50)]
#NM [('Alexis', 141), ('Alyssa', 135), ('Destiny', 115)]
#HI [('Kayla', 63), ('Taylor', 63), ('Alyssa', 61)]

#Boy results
#2000 national: [('Jacob', 34465), ('Michael', 32025), ('Matthew', 28569)]
#3 in common: DE, PA, IL
#2 in common: VT, KS, RI, MO, MI, WV, NY, OR, ID, CT, NM, VA, NH, MN, MA, AR, WA, MD, AK, NJ, CO, WY, HI, OH, AZ
#1 in common: LA, MT, OK, FL, ND, SD, SC, ME, UT, GA, TX, NV, AL, TN, IA, KY, IN, WI, NE, NC
#0 in common: DC, MS, CA

#Next steps
#Sort movie dataset by year then by gross (largest to smallest), then find highest grossing film
#in 1992-2002 then search films to get names of main female and male characters
#then count number of appearances of those names in title year versus other years in period 
#use hypothesis test to see if difference is significant? 
#compare appearance of national names to top names in coastal areas versus midwest/south

#Model: could try to predict whether, given list of main character names and features about an 
    #upcoming film, whether the name will become more popular the following year 


# In[10]:

#Have greatest suspicion Anastasia was more popular after the film came out, will test 1st
#1st look only at national names
Anastasia_count_0 = dict()
constraint = data_natl['Year'].map(lambda x: x in range(1997, 2000))
natl_199789 = data_natl[constraint]
#natl_199789.head()

for year in range(1997, 2000):
    Anastasia_count_0[year] = 0
    for index, row in natl_199789.iterrows():
        if row['Year'] == year and row['Gender'] == 'F' and 'Anasta' in row['Name']:
            Anastasia_count_0[year] += row['Count']


# In[11]:

Anastasia_count_0


# In[13]:

#So it seems like the name becomes more popular after its release at the end of 
#1997 then wanes in popularity the following year

#grab the frequencies over a greater range of years to plot more data points
Anastasia_count = dict()
constraint2 = data_natl['Year'].map(lambda x: x in range(1990, 2011))
natl_1990_2010 = data_natl[constraint2]

for year in range(1990, 2011):
    Anastasia_count[year] = 0
    for index, row in natl_1990_2010.iterrows():
        if row['Year'] == year and row['Gender'] == 'F' and 'Anasta' in row['Name']:
            Anastasia_count[year] += row['Count']
    print('oneyear')


# In[19]:

#Let's plot the frequency count of Anastasia-like names over the years

years = range(1990, 2011)
Anastasia_list = list()
for key in Anastasia_count: 
    Anastasia_list.append(Anastasia_count[key])
Anastasia_list

f, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([1990, 2010])

plt.plot(years, Anastasia_list, label='Frequency of Anastasia names', color='b')
plt.scatter(1998, Anastasia_count[1998], label='Anastasia in 1998', color='r')

ax.set_ylabel('Count')
ax.set_xlabel('Year')
ax.set_title('Popularity of Anastasia-like names over time')
legend = plt.legend(loc='best', frameon=True, borderpad=1, borderaxespad=1)


# In[21]:

#I also have a suspicion that Harriet became more popular after Harriet the spy mid 1996 
#and Fiona after Shrek mid 2001 

#Let's look at counts around the premiere year for Harriet 
Harriet_count = dict()
constraint3 = data_natl['Year'].map(lambda x: x in range(1995, 1999))
natl_1995_8 = data_natl[constraint3]

for year in range(1995, 1999):
    Harriet_count[year] = 0
    for index, row in natl_1995_8.iterrows():
        if row['Year'] == year and row['Gender'] == 'F' and 'Harriet' in row['Name']:
            Harriet_count[year] += row['Count']
            
#Let's look at counts around the premiere year for Fiona
Fiona_count = dict()
constraint4 = data_natl['Year'].map(lambda x: x in range(1999, 2005))
natl_1999_05 = data_natl[constraint4]

for year in range(1999, 2005):
    Fiona_count[year] = 0
    for index, row in natl_1999_05.iterrows():
        if row['Year'] == year and row['Gender'] == 'F' and row['Name'] == 'Fiona':
            Fiona_count[year] += row['Count']

print('Harriet_count')
print(Harriet_count)
print('Fiona_count')
print(Fiona_count)


# In[22]:

#Hmmm it looks like Harriet was not more popular during the year of/right after the film came
#out and it looks like Fiona became more popular right after Shrek and continued to 
#increase in popularity 

#Let's look at the name Roland from The Wood to consider a male name here then start plotting

#Let's look at counts around the premiere year for The Wood - mid 1999
Roland_count = dict()
constraint5 = data_natl['Year'].map(lambda x: x in range(1997, 2002))
natl_1997_01 = data_natl[constraint5]

for year in range(1997, 2002):
    Roland_count[year] = 0
    for index, row in natl_1997_01.iterrows():
        if row['Year'] == year and row['Gender'] == 'M' and row['Name'] == 'Roland':
            Roland_count[year] += row['Count']
            
Roland_count          


# In[23]:

#Interesting...frequency of Roland seems fairly constant in this range
#So we'll just plot Fiona over time

#Let's grab the frequencies over a greater range of years so we can plot more data points
Fiona_count_plt = dict()
#constraint2 = data_natl['Year'].map(lambda x: x in range(1990, 2011))
#natl_1990_2010 = data_natl[constraint2]

for year in range(1990, 2011):
    Fiona_count_plt[year] = 0
    for index, row in natl_1990_2010.iterrows():
        if row['Year'] == year and row['Gender'] == 'F' and row['Name'] == 'Fiona':
            Fiona_count_plt[year] += row['Count']

years = range(1990, 2011)
Fiona_list = list()
for key in Fiona_count_plt: 
    Fiona_list.append(Fiona_count_plt[key])

f, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim([1990, 2010])

plt.plot(years, Fiona_list, label='Frequency of Fiona', color='b')
plt.scatter(2002, Fiona_count_plt[2002], label='Fiona in 2002', color='r')

ax.set_ylabel('Count')
ax.set_xlabel('Year')
ax.set_title('Popularity of Fiona name over time')
legend = plt.legend(loc='best', frameon=True, borderpad=1, borderaxespad=1)


# In[ ]:



