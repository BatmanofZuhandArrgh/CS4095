#!/usr/bin/env python
# coding: utf-8

# ## Glop Optimization with Lists: Sidneyville Manufacturing

# In[2]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp


# In[3]:


# input parameters
product = ['Roll_Top', 'Regular']        # list of product names
wood = ['Fabrication', 'Cedar', 'Maple']        # list of constraint names
profit = [115.00, 90.00]                 # list of product profit coefficients
wood_req = [[10, 20], [4, 16], [15, 10]] # two dimensional list of wood constraint coefficients
                                         # each sublist corresponds to a constraint
wood_rhs = [200, 128, 220]               # list of board feet available for each type of wood


# In[4]:


# initialize LP model object
# first argument is the name of the model and second argument is the type of model

mymodel = glp.Solver('Sidneyville', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[13]:


# define decision variables
dvar = list(range(len(product)))         # create a list to store one variable for each product
for i in range(len(product)):            # loop to create a variable for each product
    dvar[i] = mymodel.NumVar(0, mymodel.infinity(), product[i])
                                         # arguments: (lower bound, upper bound, name)
print (dvar[0])


# In[6]:


# define objective function
TotProfit = mymodel.Objective()          # create objective function object
TotProfit.SetMaximization()              # set direction of optimization
for i in range(len(product)):      # loop to set the objective coefficient for each product variable
    TotProfit.SetCoefficient(dvar[i], profit[i])
                                         # arguments: (variable, coefficient)


# In[7]:


# define constraints
constr = list(range(len(wood)))          # create a list to store each constraint
for w in range(len(wood)):               # loop to create each constraint
    constr[w] = mymodel.Constraint(-mymodel.infinity(), wood_rhs[w])
                                         # arguments: (lower bound, upper bound)
    for p in range(len(product)):        # loop to set the constraint coefficient for each variable
        constr[w].SetCoefficient(dvar[p], wood_req[w][p]) #args: (variable, coefficient)


# In[8]:


# Solve the model and print optimal solution
status = mymodel.Solve()                 # solve mymodel and display the solution

print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Profit = %.2f' % TotProfit.Value())

# The value of each variable in the solution.
for p in range(len(product)):
    print('%s = %.2f' % (product[p], dvar[p].solution_value()))


# In[9]:


# display constraint Information
print('Wood \t LHS \t RHS \t Slack \t Dual')
LHS = mymodel.ComputeConstraintActivities()
for w in range(len(wood)):
    slack = wood_rhs[w] - LHS[w]
    print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % (wood[w], LHS[w], wood_rhs[w], slack, constr[w].dual_value()))


# In[ ]:




