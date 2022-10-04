#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[59]:


print("This is Ravi's Assignment-1")
print("student_ID: 6805329")


# In[46]:


##Question-1
import math
i = 0
for i in range(0,15):
    i=i+1
    result = math.factorial(i)
    if(result<10**8):
        print(result,'This is not required because less that 10^8')
    else:
        print(result,'This is required')


# In[ ]:





# In[44]:



#Quesion-3

def powerfunc(mylist):
    for i in mylist:
        result= i[0]**i[1]
        print(result)

l = [[5,6], [5,7], [4,2], [3,6], [9,8], [1,3], [9,3], [7,1], [5,4], [2,7],
[9,1], [9,3], [2,5]]

powerfunc(l)


# In[43]:


##Question4

from random import random
l = [random()for i in range(20)]
x = random()
y = l.sort()
l


# In[57]:


#Question-5
def thesearemycircles(x=1,y=1):
    pi = 3.14
    area_of_xradius = pi*x*x
    area_of_yradius = pi*y*y
    if(area_of_xradius<area_of_yradius):
        return((area_of_xradius/area_of_yradius)*100)
    else:
        return((area_of_yradius/area_of_xradius)*100)
thesearemycircles(2,4)
##I think the code works because for x=2 
##and y=4, the smaller circle covers about 25% of the larger circle.


# In[47]:


##q6

##this function 
def letsgetproportionate(item,list1):
    check=0
    for i in list1:
        if i<=item:
            check = check + 1
    return(round(check/len(list1),2))  
##this is a funtion that just takes in a list of numbers and 
## returns a dictionary
def making_dictionary(list1):
    dict1 = {}
    for item in list1:
        dict1[item] = letsgetproportionate(item,list1)
    return(dict1)

list1 = [2,4,8,3,10]
making_dictionary(list1)


# In[66]:


#q7
def gettime(seconds):
    hours = seconds//3600
    seconds = seconds%3600
    minutes = seconds%60
    return hours, minutes, seconds
    
##total seconds in a day (ON EARTH) 86400
h, m, s = gettime(86400)
if h <13 :
    print(h,m,s,"AM")
else:
    print(h,m,s,"PM")
        
## after 86400s the day is compelete hence 24PM?


# In[49]:


#q8

import pandas as pd
dict1 = {'A': [1,2,2,1], 'B': [3.1,4.2,1.5,6.3], 'C': [800,150,400,210]}  #dict1 is the dictionary with the given data
df = pd.DataFrame(dict1)
df = df.to_string(index = False)  #we don not want the indexx to be counted in the output i.ie, 0,1,2,3
print(df)


# In[ ]:




