#!/usr/bin/env python
# coding: utf-8

# In[86]:


import matplotlib.pyplot as plt
import random as rd
import numpy as np
from math import *

SalesMin = 18.95
SalesMax = 26.95
SalesMode = 24.95

CostMax = 15
CostMin = 12

trials = 10000

#Sales Price per Unit
SalesperUnit = np.random.triangular(SalesMin, SalesMode, SalesMax, trials)

#Cost per Unit
CostperUnit = np.random.uniform(CostMin, CostMax, trials)

#Random Term
mu, sigma = 0, 10 # mean and standard deviation
RandomTerm = np.random.normal(mu, sigma, trials)

#Fixed Cost
mu1, sigma1 = 30000, 5000
FixedCost = np.random.normal(mu1, sigma1, trials)


# In[87]:


#Building the Quantity models
Quantity = list()
for i in range(trials):
    Quantity.append(10000 - 250*SalesperUnit[i] + RandomTerm[i])
    
#List of Revenue
Revenue = list()
for i in range(trials):
    Revenue.append(Quantity[i]*SalesperUnit[i])
    
#List of Revenue
Cost = list()
for i in range(trials):
    Cost.append(FixedCost[i] + Quantity[i]*CostperUnit[i])
    
#List of Profit
Profit = list()
for i in range(trials):
    Profit.append(Revenue[i] - Cost[i])


# In[88]:


# Show and check Profit
#for i in range(10000):
 #  print(Profit[i])
# Plot of Randomly generated Demand (normally distributed)
plt.xlim(-20000,40000)
(a,b,c) = plt.hist(Profit, edgecolor='k')


# In[89]:


#b. Calculating the mean of these simulated profits
AverageProfit = 0
for i in range(trials):
    AverageProfit = AverageProfit + Profit[i]/trials
print("The average profit/ expected value simulated is: $" ,AverageProfit)
Stddev = np.std(Profit)
print("The standard deviation simulated is: $" , Stddev)


# In[90]:


#a. The profit seems to be normally distributed, creating a bell curve
#Its mean hovering around 10000, with the std deviation around $6800


# In[91]:


#c. Calculating the probability of having net loss
Netloss = 0
for i in range(trials):
    if Profit[i]<0 :#and Demand[i] != Cost:
        Netloss = Netloss + 1
        
print("The probability of a net loss is roughly ", Netloss/(trials/100), '%.')


# In[92]:


#d. Finding the maximum loss
print("The maximum loss is: $", (-1)*min(Profit))


# In[ ]:




