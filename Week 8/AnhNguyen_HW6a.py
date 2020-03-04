#!/usr/bin/env python
# coding: utf-8

# In[78]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp


# In[88]:


# input parameters
Stock = ['Std Oil', 'B&O Railroad','Dunder Mifflin']   # list of product names
Department = ['Fabrication', 'Assembly', 'Shipping'] # list of constraint names
Price = [50.00, 30.00,40.00]                 # list of product profit coefficients
AnnualReturn = [6,4,5]
MaximumInvestment = 800000
InvestmentLimit = [200000, 450000, 250000]


# In[89]:


# initialize LP model object
# first argument is the name of the model and second argument is the type of model

mymodel = glp.Solver('Lexington', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[90]:


# define decision variables
dvar = list(range(len(Stock)))         # create a list to store one variable for each product
for i in range(len(Stock)):            # loop to create a variable for each product
    dvar[i] = mymodel.NumVar(0, mymodel.infinity(), Stock[i])
                                         # arguments: (lower bound, upper bound, name)
    


# In[91]:


# define objective function
TotProfit = mymodel.Objective()          # create objective function object
TotProfit.SetMaximization()              # set direction of optimization
for i in range(len(Stock)):      # loop to set the objective coefficient for each product variable
    TotProfit.SetCoefficient(dvar[i], AnnualReturn[i])
                                         # arguments: (variable, coefficient)


# In[92]:


# define constraints
constr = list(range(len(Stock)+1))
constr[0] = mymodel.Constraint(0, MaximumInvestment, 'MaxInvestment')      # Aroma constraint
for c in range(len(Stock)):
    constr[0].SetCoefficient(dvar[c], Price[c])
    
for c in range(len(Stock)):                                         # available supply constraints
    constr[1+c] = mymodel.Constraint(-mymodel.infinity(), InvestmentLimit[c], Stock[c])
    constr[1+c].SetCoefficient(dvar[c], Price[c])
    
print(len(constr))


# In[93]:


# Solve the model and print optimal solution
status = mymodel.Solve()                 # solve mymodel and display the solution

print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Return = %.2f' % TotProfit.Value())

# The value of each variable in the solution.
for p in range(len(Stock)):
    print('%s = %.2f' % (Stock[p], dvar[p].solution_value()))
    


# In[94]:


# display constraint Information
print('AmountInvested \t LHS \t \t RHS \t \t Slack \t Dual')
LHS = mymodel.ComputeConstraintActivities()

for w in range(len(constr)):
    #if c < 1:
    slack = LHS[w] - constr[w].Ub()
    print('%s \t %.1f \t %.1f \t %.1f \t %.4f' % (constr[w].name(), LHS[w], constr[w].Ub(), slack, constr[w].dual_value()))
    


# In[ ]:





# In[ ]:




