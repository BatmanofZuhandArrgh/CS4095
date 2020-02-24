#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import random as rd
import matplotlib.pyplot as plt


# In[54]:


MeanConsumption = 2600
StddevConsumption = 550
HydroGen = 700
GasGen = 1900
HydroCost = 21
HydroCapa = 700
GasCost = 45
GasCapa = 2400
MarketCost = 65

trials = 10000
rd.seed(101010)


# In[55]:


#a, Models for cost for meeting all customers' demand
TotalConsumption = np.random.normal(MeanConsumption, StddevConsumption, trials)
#for i in range(trials):
 #   print (TotalConsumption[i]);
#plt.xlim(0,5000)
#(a,b,c) = plt.hist(TotalConsumption, edgecolor='k')
TotalCost = list()

for i in range(trials):
    if TotalConsumption[i] <= HydroGen:
        TotalCost.append(HydroCost*TotalConsumption[i])
    elif (TotalConsumption[i] > HydroGen and TotalConsumption[i] <= (HydroGen+GasGen)):
        TotalCost.append(HydroCost * HydroGen + GasCost * (TotalConsumption[i] - HydroGen))
    else:
        TotalCost.append(HydroCost * HydroGen + GasCost * GasGen + MarketCost * (TotalConsumption[i] - HydroGen - GasGen))
        


# In[57]:


#b. Describing the distribution of daily generation cost
for i in range(trials):
    print (TotalCost[i]);
plt.xlim(0,250000)
(a,b,c) = plt.hist(TotalCost, edgecolor='k')


# In[58]:


#c. Confidence interval for cost
MeanCost = np.mean(TotalCost)
StddevCost = np.std(TotalCost)
margin_of_error = 1.96 * StddevCost/len(TotalCost)** 0.5
lcl = MeanCost - margin_of_error
ucl = MeanCost + margin_of_error
print('95%% confidence interval for the mean total daily cost of the current power gen plan is at (%3.3f , %3.3f)' % (lcl, ucl))


# In[59]:


#d. What is the probability that cost will exceed 150000
Benchmark = 150000
ProbabilityExceeds = 0
for i in range(trials):
    if TotalCost[i] > Benchmark:
        ProbabilityExceeds = ProbabilityExceeds + 1
        
Probability = ProbabilityExceeds/trials
print('There is a %5.2f%% the daily cost will exceed 150000'% (100*Probability))


# In[60]:


GasGenList = list()
for i in range(GasCapa - GasGen+1):
    GasGenList.append(GasGen + i)
#for i in range(len(GasGenList)):
#    print(GasGenList[i])

TotalCostChangingGasGen = list()

for j in range(GasCapa - GasGen+1):
    
    TotalCost = list()
    for i in range(trials):
        if TotalConsumption[i] <= HydroGen:
            TotalCost.append(HydroCost*TotalConsumption[i])
        elif (TotalConsumption[i] > HydroGen and TotalConsumption[i] <= (HydroGen+GasGenList[j])):
            TotalCost.append(HydroCost * HydroGen + GasCost * (TotalConsumption[i] - GasGenList[j]))
        else:
            TotalCost.append(HydroCost * HydroGen + GasCost * GasGenList[j] + MarketCost * (TotalConsumption[i] - HydroGen - GasGenList[j]))
        
    TotalCostChangingGasGen.append(np.mean(TotalCost))
    
#for i in range(GasCapa - GasGen+1):
 #   print (TotalCostChangingGasGen[i]);
#plt.xlim(0,250000)
#(a,b,c) = plt.hist(TotalCostChangingGasGen, edgecolor='k')

    


# In[61]:


print("The minimum Total cost while changing Gas Generation is %5.2f" % min(TotalCostChangingGasGen))
print("The amount of daily gas turbine power generation is %5.2f MWh" % GasGenList[TotalCostChangingGasGen.index(np.min(TotalCostChangingGasGen))])


# In[ ]:




