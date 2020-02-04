#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import random as rd
import numpy as np

# Original parameters
Cost_per_shirt = 50
Price_per_shirt = 75
Price_per_shirt_left = 15
Order_quantity = 550
trials = 10000


# In[2]:


#Demand is normally distributed with the mean of mu and std.dev of sigma
mu, sigma = 500, 75 # mean and standard deviation
Demand = np.random.normal(mu, sigma, trials)
#for i in range(trials):
 #   print(Demand[i])


# In[3]:


#Calculate cost and populate Demand array
Cost = Cost_per_shirt * Order_quantity
Revenue = list()
for i in range(10000):
    if(Demand[i] >= Order_quantity):
        Revenue.append(Order_quantity * Price_per_shirt)
    else:
        Revenue.append(Demand[i] * Price_per_shirt + (Order_quantity - Demand[i])*Price_per_shirt_left)
        


# In[4]:


#Show and check Revenue
#for i in range(10000):
#    print(Revenue[i])
# Plot of Randomly generated Demand (normally distributed)
plt.xlim(0,100000)
(a,b,c) = plt.hist(Revenue, edgecolor='k')


# In[106]:


# Populate Array of profit
Profit = list()
for i in range(10000):
    if Revenue[i] > Cost:
        Profit.append(Revenue[i] - Cost)
    else:
        Profit.append(0)


# In[107]:


# Plot of Randomly generated Demand (normally distributed)
plt.xlim(200,800)
(a,b,c) = plt.hist(Demand, edgecolor='k')


# In[112]:


# Show and check Profit
#for i in range(10000):
 #  print(Profit[i])
# Plot of Randomly generated Demand (normally distributed)
plt.xlim(0,30000)
(a,b,c) = plt.hist(Profit, edgecolor='k')


# In[113]:


#a. Distribution of Lucy's profit seems to be the left half of a normal distribution graph (A bell curve).
#Then there's an unusually high frequency of the mean.


# In[114]:


#b. Calculating the mean of these simulated profits
AverageProfit = 0
for i in range(10000):
    AverageProfit = AverageProfit + Profit[i]/10000
print("The average profit simulated is: $" ,AverageProfit)


# In[116]:


#c. Calculating the probability of having net loss
Netloss = 0
for i in range(10000):
    if Profit[i]==0 :#and Demand[i] != Cost:
        Netloss = Netloss + 1

        
print("The probability of a net loss is roughly ", Netloss/100, '%.')


# In[ ]:


#d. Calculating the order quantity that maximize mean total profit

