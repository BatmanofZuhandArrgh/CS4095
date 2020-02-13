#!/usr/bin/env python
# coding: utf-8

# In[269]:


import numpy as np
import random as rd
import matplotlib.pyplot as plt


# In[270]:


#1.
#Input_Parameter
TotalCar = 120
Rent_per_day = 95
OperationCost = 35
ProbNotShowingUp = 0.1
Refund = 140
Reservation_limit = 135
trials = 10000
show_ups = [0,1]
show_ups_rates = [ProbNotShowingUp,1-ProbNotShowingUp]


# In[271]:


#1a. 
rd.seed(4373) 
total_profit = list()
total_revenue = list()
total_cost = list()

Reservations = Reservation_limit

#Caculating across 10,000 the number of people who show up 
NumberofShowups = list() 
for j in range(trials): 
    showupcount = 0
    for i in range(Reservations): 
        showup = rd.choices(show_ups,show_ups_rates, k=1)
        showupcount = showupcount+showup[0]
        
    NumberofShowups.append(showupcount)
    
#for i in range(trials):
 #   print(NumberofShowups[i])
#print(np.mean(NumberofShowups))
plt.hist(NumberofShowups, edgecolor = 'k')


# In[272]:


#Calculating the simulated revenue
for i in range(trials):
    #if(NumberofShowups[i]>TotalCar):
     #   total_revenue.append(TotalCar*Rent_per_day)
    #else:
        total_revenue.append(Reservations*Rent_per_day)
#for i in range(trials):
 #   print(total_revenue[i])
plt.hist(total_revenue, edgecolor = 'k')


# In[273]:


#Calculating the simulated cost
for i in range(trials):
    if(NumberofShowups[i]>TotalCar):
        total_cost.append((NumberofShowups[i]-TotalCar)*(Refund+Rent_per_day) + OperationCost*TotalCar)
    else:
        total_cost.append(OperationCost*NumberofShowups[i])
#for i in range(trials):
 #   print(total_cost[i])
plt.hist(total_cost, edgecolor = 'k')


# In[274]:


#Calculating the simulated profit
for i in range(trials):
    if(total_revenue[i]>=total_cost[i]):
        total_profit.append(total_revenue[i]-total_cost[i])
    else:
        total_profit.append(0)
#for i in range(trials):
 #   print(total_profit[i])
plt.hist(total_profit, edgecolor = 'k')


# In[275]:


#1b. 
MeanProfit = np.mean(total_profit)
print('The mean total profit is: $%5.2f' % MeanProfit)


# In[276]:


#1c. 
Stddev = np.std(total_profit)
MeanStdError = Stddev/(np.sqrt(len(total_profit)))
Z90=1.645

moe = Z90*MeanStdError
lcl = (MeanProfit-moe)
ucl = (MeanProfit+moe)

print('Lower limit for 90% interval is: $',lcl)
print('Upper limit for 90% interval is: $',ucl)


# In[278]:


#1d. 
x = 0 
for i in range(trials): 
    if(total_profit[i]>=8700): 
        x = x+1 
Proportion1 = x/len(total_profit) 
        
print("The probability of profit exceeding $8700 is: %5.2f" %(Proportion1*100), '%')


# In[288]:


#1e.
z95 = 1.96
moe = z95 * ((Proportion1 *(1-Proportion1)/len(total_profit))**0.5)
lcl = (Proportion1-moe)
ucl = (Proportion1+moe)

#print("Lower limit for 90% interval is:", lcl)
#print("Upper limit for 90% interval is:", ucl)

print('The 95%% confidence interval for making at least $8700 is (%5.4f%%,%5.4f%%).'% (lcl*100,ucl*100))


# In[281]:


#1f.
overbooked = list(range(121,135))
rd.seed(23) 
overbooked_meanprofit = list()

for a in range(len(overbooked)):
#Caculating across 10,000 the number of people who show up 
    total_profit = list()
    total_revenue = list()
    total_cost = list()

    Reservations = overbooked[a]

    NumberofShowups = list() 
    for j in range(trials): 
        showupcount = 0
        for i in range(Reservations): 
            showup = rd.choices(show_ups,show_ups_rates, k=1)
            showupcount = showupcount+showup[0]
        
        NumberofShowups.append(showupcount)
    
    for i in range(trials):
        total_revenue.append(Reservations*Rent_per_day)


    #Calculating the simulated cost
    for i in range(trials):
        if(NumberofShowups[i]>TotalCar):
            total_cost.append((NumberofShowups[i]-TotalCar)*(Refund+Rent_per_day) + OperationCost*TotalCar)
        else:
            total_cost.append(OperationCost*NumberofShowups[i])

    #Calculating the simulated profit
    for i in range(trials):
        if(total_revenue[i]>=total_cost[i]):
            total_profit.append(total_revenue[i]-total_cost[i])
        else:
            total_profit.append(0)
    #Creating the profit mean list
    overbooked_meanprofit.append(np.mean(total_profit))

print("The maximum profit mean is: $", max(overbooked_meanprofit))
print('The maximum overbooked amount to get that profit is: ',overbooked[overbooked_meanprofit.index(np.max(overbooked_meanprofit))])



# In[282]:


#2.
#Input Parameter
Total_home = 35
Probability_Finding = 0.7
Probability_Purchase = 0.33
MeanPurchase = 27
StddevPurchase = 6
Success = [0,1]
FoundRates = [1-Probability_Finding,Probability_Finding]
PurchasedRates = [1-Probability_Purchase,Probability_Purchase]


# In[283]:


#Model
sample = list()

for i in range(trials):
    Rev = 0
    for b in range(Total_home):
        Found = rd.choices(Success, FoundRates,k=1)
        Purchased = rd.choices(Success, PurchasedRates,k=1)
        if Found[0] == 1 and Purchased[0] == 1:
            Rev = Rev + rd.normalvariate(MeanPurchase,StddevPurchase)
    sample.append(Rev)
    
#for i in range(trials):
 #   print(sample[i])
    
plt.hist(sample, edgecolor = 'k')


# In[284]:


#2a. 
sample_mean = np.mean(sample)
print("The total revenue expected is $ %5.2f" %sample_mean)


# In[285]:


#2b.
sample_std = np.std(sample)
z95 = 1.96
moe = z95 * sample_std/len(sample)**0.5 ##magrin of error
lcl = sample_mean - moe 
ucl = sample_mean + moe
print('The 95%% confidence interval for the sample is (%6.2f,%6.2f).' % (lcl,ucl))


# In[286]:


#2c.
Proportion = 0
for i in range(trials):
    if(sample[i]>=300):
        Proportion = Proportion+1
        
Proportion = Proportion/len(sample)
print("The probability of revenue exceeding $300 is: %5.2f" %(Proportion*100), '%')
 


# In[289]:


#2d
z90 = 1.645
moe = z90 * (Proportion *((1-Proportion)/len(sample))**0.5)
lcl = (Proportion-moe)
ucl = (Proportion+moe)

#print("Lower limit for 90% interval is:", lcl)
#print("Upper limit for 90% interval is:", ucl)

print('The 90%% confidence interval for proportion of sample is (%5.4f%%,%5.4f%%).'% (lcl*100,ucl*100))


# In[ ]:




##Fuck you, Sam
