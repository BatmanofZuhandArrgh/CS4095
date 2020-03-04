#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import packages
from ortools.linear_solver import pywraplp as glp


# In[9]:


# input parameters
Product = ['MFrame', 'MSupport','MStrap'
           ,'PFrame','PSupport','PStrap']   # list of product names
Department = ['Cutting', 'Milling', 'Shaping'] # list of constraint names
Hours_req = [[3.5/60, 1.3/60, 0.8/60], 
             [2.2/60, 1.7/60, 0.0], 
             [3.1/60, 2.6/60, 1.7/60]] 
# 3 dimensional list of department constraint coefficients           
# each sublist corresponds to a constraint
MPCost = [38.00, 11.50, 6.50, 
          51.00, 15.00, 7.50]        # list of Manufacturing and Purchasing Cost per component
Capacity = [350 , 420 , 680]
Order = 5000


# In[10]:


# initialize LP model object
# first argument is the name of the model and second argument is the type of model

mymodel = glp.Solver('Frandec Company', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[11]:


# define decision variables
dvar = list(range(len(Product)))         # create a list to store one variable for each product
for i in range(len(Product)):            # loop to create a variable for each product
    dvar[i] = mymodel.NumVar(0, 2*Order, Product[i])
                                         # arguments: (lower bound, upper bound, name)
    


# In[12]:


# define objective function
TotCost = mymodel.Objective()          # create objective function object
TotCost.SetMinimization()              # set direction of optimization
for c in range(len(Product)):
    TotCost.SetCoefficient(dvar[c], MPCost[c])
                                         # arguments: (variable, coefficient)


# In[13]:


# define constraints
constr = list(range(6))          # create a list to store each constraint

for w in range(3):               # loop to create each constraint
    constr[w] = mymodel.Constraint(-1, Capacity[w], Department[w])
                                         # arguments: (lower bound, upper bound)
    for p in range(3):        # loop to set the constraint coefficient for each variable
        constr[w].SetCoefficient(dvar[p], Hours_req[w][p]) #args: (variable, coefficient)

        
constr[3] = mymodel.Constraint(Order, Order, 'Total Frame')      # Total Frame constraint
constr[3].SetCoefficient(dvar[0], 1)
constr[3].SetCoefficient(dvar[3], 1)

constr[4] = mymodel.Constraint(2*Order, 2*Order, 'Total Support')      # Total Support constraint
constr[4].SetCoefficient(dvar[1], 1)
constr[4].SetCoefficient(dvar[4], 1)

constr[5] = mymodel.Constraint(Order, Order, 'Total Strap')      # Total Strap constraint
constr[5].SetCoefficient(dvar[2], 1)
constr[5].SetCoefficient(dvar[5], 1)
    


# In[14]:


# Solve the model and print optimal solution
status = mymodel.Solve()                 # solve mymodel and display the solution

print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Cost = %.2f' % TotCost.Value())

# The value of each variable in the solution.
for p in range(len(Product)):
    print('%s = %.2f' % (Product[p], dvar[p].solution_value()))


# In[15]:


# display constraint Information
print('Constraint \t LHS \t RHS \t Slack \t Dual')
LHS = mymodel.ComputeConstraintActivities()
for c in range(mymodel.NumConstraints()):
    slack = LHS[c] - constr[c].Ub()
    print('%s \t %.1f \t %.1f \t %.1f \t %.4f' % (constr[c].name(), LHS[c], constr[c].Ub(), slack, constr[c].dual_value()))
    


# In[16]:


#b. For a marginal increase of 1 more hour total, the cost will decrease $161.5385
#Therefore, Frandec should be willing to spend maximum $161.


# In[17]:


#c.
MPCost = [38.00, 11.50, 6.50, 
          45.00, 15.00, 7.50]        # list of Manufacturing and Purchasing Cost per component
# initialize LP model object
mymodel1 = glp.Solver('Frandec Company1', glp.Solver.GLOP_LINEAR_PROGRAMMING)

# define decision variables
dvar = list(range(len(Product)))         # create a list to store one variable for each product
for a in range(len(Product)):            # loop to create a variable for each product
    dvar[a] = mymodel1.NumVar(0, 2*Order, Product[a])
                                         # arguments: (lower bound, upper bound, name)
        
# define objective function
TotCost = mymodel1.Objective()          # create objective function object
TotCost.SetMinimization()              # set direction of optimization
for b in range(len(Product)):
    TotCost.SetCoefficient(dvar[b], MPCost[b])
    
# define constraints
constr = list(range(6))          # create a list to store each constraint

for d in range(3):               # loop to create each constraint
    constr[d] = mymodel1.Constraint(-1, Capacity[d], Department[d])
                                         # arguments: (lower bound, upper bound)
    for e in range(3):        # loop to set the constraint coefficient for each variable
        constr[d].SetCoefficient(dvar[e], Hours_req[d][e]) #args: (variable, coefficient)

        
constr[3] = mymodel1.Constraint(Order, Order, 'Total Frame')      # Total Frame constraint
constr[3].SetCoefficient(dvar[0], 1)
constr[3].SetCoefficient(dvar[3], 1)

constr[4] = mymodel1.Constraint(2*Order, 2*Order, 'Total Support')      # Total Support constraint
constr[4].SetCoefficient(dvar[1], 1)
constr[4].SetCoefficient(dvar[4], 1)

constr[5] = mymodel1.Constraint(Order, Order, 'Total Strap')      # Total Strap constraint
constr[5].SetCoefficient(dvar[2], 1)
constr[5].SetCoefficient(dvar[5], 1)

# Solve the model and print optimal solution
status = mymodel1.Solve()                 # solve mymodel and display the solution

print('Solution Status =', status)
print('Number of variables =', mymodel1.NumVariables())
print('Number of constraints =', mymodel1.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Cost = %.2f' % TotCost.Value())

# The value of each variable in the solution.
for x in range(len(Product)):
    print('%s = %.2f' % (Product[x], dvar[x].solution_value()))
print('/n')
# display constraint Information
print('Constraint \t LHS \t RHS \t Slack \t Dual')
LHS = mymodel1.ComputeConstraintActivities()
for g in range(mymodel1.NumConstraints()):
    slack = LHS[g] - constr[g].Ub()
    print('%s \t %.1f \t %.1f \t %.1f \t %.4f' % (constr[g].name(), LHS[g], constr[g].Ub(), slack, constr[g].dual_value()))


# In[ ]:


#c. After remodelling, if the Frame seller offered them for $45
#Frandec definitely should purchase Frames from this supplier
#, in total 2714 of them

