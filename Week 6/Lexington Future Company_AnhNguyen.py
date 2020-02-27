#!/usr/bin/env python
# coding: utf-8

# In[23]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp


# In[24]:


# input parameters
Product = ['Chairs', 'Desks','Tables']   # list of product names
Department = ['Fabrication', 'Assembly', 'Shipping'] # list of constraint names
profit = [15.00, 24.00,18.00]                 # list of product profit coefficients
Hours_req = [[4, 6, 2], [3, 5, 7], [3, 2, 4]] # 3 dimensional list of department constraint coefficients
                                         # each sublist corresponds to a constraint
Hours_rhs = [1850, 2400, 1500]               # list of board feet available for each type of wood

Max_sales = [360, 300, 100]


# In[25]:


# initialize LP model object
# first argument is the name of the model and second argument is the type of model

mymodel = glp.Solver('Lexington', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[26]:


# define decision variables
dvar = list(range(len(Product)))         # create a list to store one variable for each product
for i in range(len(Product)):            # loop to create a variable for each product
    dvar[i] = mymodel.NumVar(0, Max_sales[i], Product[i])
                                         # arguments: (lower bound, upper bound, name)
    


# In[27]:


# define objective function
TotProfit = mymodel.Objective()          # create objective function object
TotProfit.SetMaximization()              # set direction of optimization
for i in range(len(Product)):      # loop to set the objective coefficient for each product variable
    TotProfit.SetCoefficient(dvar[i], profit[i])
                                         # arguments: (variable, coefficient)


# In[28]:


# define constraints
constr = list(range(len(Department)))          # create a list to store each constraint
for w in range(len(Department)):               # loop to create each constraint
    constr[w] = mymodel.Constraint(-mymodel.infinity(), Hours_rhs[w])
                                         # arguments: (lower bound, upper bound)
    for p in range(len(Product)):        # loop to set the constraint coefficient for each variable
        constr[w].SetCoefficient(dvar[p], Hours_req[w][p]) #args: (variable, coefficient)
        


# In[29]:


# Solve the model and print optimal solution
status = mymodel.Solve()                 # solve mymodel and display the solution

print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Profit = %.2f' % TotProfit.Value())

# The value of each variable in the solution.
for p in range(len(Product)):
    print('%s = %.2f' % (Product[p], dvar[p].solution_value()))
    


# In[31]:


# display constraint Information
print('Dept \t \t LHS \t \t RHS \t \t Slack \t Dual')
LHS = mymodel.ComputeConstraintActivities()
for w in range(len(Department)):
    slack = Hours_rhs[w] - LHS[w]
    print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % (Department[w], LHS[w], Hours_rhs[w], slack, constr[w].dual_value()))
    


# In[ ]:


#b. The binding constraint is Fabrication, where LHS == RHS
# The marginal values of Fabrications is 4 hours, and for 
# both Assembly and Shipping are 0.

