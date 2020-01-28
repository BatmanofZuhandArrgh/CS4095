#!/usr/bin/env python
# coding: utf-8

# In[94]:


Cost_per_shirt = 50
Price_per_shirt = 75
Price_per_shirt_left = 15
Order_quantity = 420
Demand = 400


# In[95]:


#Cost = Order_quantity * Cost_per_shirt
#Revenue
#if Demand >= Order_quantity:
 #   Revenue = Price_per_shirt * Order_quantity
#else:
 #   Revenue = Demand*Price_per_shirt + (Order_quantity-Demand)*Price_per_shirt_left
    
#while Demand


# In[96]:


#Profit
#if Revenue>= Cost:
 #   Profit = Revenue - Cost
#else:
 #   Profit = 0
#print (Profit)


# In[111]:


#S1: Populate the Demand and Quantity Arrays
Demand_array = []
Quantity_array = []
i= 0
Demand = 400
while i <= 10:
    Demand_array.append(Demand)
    Quantity_array.append(Demand)
    Demand = Demand + 20
    i = i+1


# In[127]:


#initialize Profit 2D array
#S2: Populate the array with Profits

Profit_array = [[0 for x in range(11)] for y in range(11)]
i = 0
j = 0
while i<=10:
    j = 0
    while j<=10:
        Cost = Quantity_array[i] * Cost_per_shirt
#Revenue
        if Demand_array[j] >= Quantity_array[i]:
            Revenue = Price_per_shirt * Quantity_array[i]
        else:
            Revenue = Demand_array[j] * Price_per_shirt + (Quantity_array[i]-Demand_array[j])*Price_per_shirt_left
#Profit
        if Revenue>= Cost:
            Profit_array[i][j] = Revenue - Cost
        else:
            Profit_array[i][j] = 0  
           
        j = j + 1
    i = i + 1


# In[151]:


#Looping to build to top row
i = 400
print ('DEMAND($)', end = " ")
while i <= 600:
    print (i, end='       ')
    i = i+20
print ('\n')

print ('QUANTITY(shirts)')
#S3: Looping to create the table    
i = 0
j = 0
while i<=10:
    j = 0
    print(Quantity_array[i], end = ' ')
    while j<=10:
        print('   ', Profit_array[i][j], end = " ")
        j = j + 1
    print ('\n')
    i = i + 1


# In[152]:


#S4: Finding the average profit as order quantity varies from 400 to 600
AverageProfit = [0 for x in range(11)]
i = 0
j = 0
while j <= 10:
    i = 0
    while i <= 10:
        AverageProfit[j] = AverageProfit[j] + Profit_array[i][j]/11;
        i = i + 1
    j = j + 1 
print ('Average Profit as Quantity varies')
j = 0;
while j <= 10:
    print(' ',round(AverageProfit[j],2), end = ' ')
    j = j+1


# In[ ]:


#As demands grows and order quantity stays the same, the profit will reach a constant values.
#For the same demand, and order quantity increases, the profit will increase to a point and then decrease
#It's easy to see that profit will be maximized if demand is maximum and the order quantity satisfy that demand perfectly.
#Profit is at it's minumum when the person misjudge the demand and order too many, a lot more than the demand
#In this case, they're Demand = 400, Orderquantity = 600

