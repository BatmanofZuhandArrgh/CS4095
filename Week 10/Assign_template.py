#!/usr/bin/env python
# coding: utf-8

# ## Assignment Problem

# In[15]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp


# In[16]:


# input parameters
sub = ['Westside', 'Federated', 'Goliath', 'Universal']  # list of subcontractors (agents)
proj = ['A', 'B', 'C']  # list of projects (tasks)
cost = [[50, 36, 16],   # assignment costs - Westside                 
        [28, 30, 18],   # Federated
        [35, 32, 20],   # Goliath
        [25, 25, 14]]   # Universal


# In[17]:


# initialize LP model object
mymodel = glp.Solver('Sub_Assignment', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[18]:


# create two dimensional list of assignment variables
assign = list(range(len(sub)))
for i in range(len(sub)):
    assign[i] = list(range(len(proj))) # create a variable list for each subcontractor
    for j in range(len(proj)):
        assign[i][j] = mymodel.NumVar(0, 1, sub[i] + '-' + proj[j])
        
        


# In[19]:


# define objective function
TotCost = mymodel.Objective()
TotCost.SetMinimization()
for i in range(len(sub)):  # loop to set the objective coefficient for each assignment variable
    for j in range(len(proj)):
        TotCost.SetCoefficient(assign[i][j], cost[i][j])


# In[20]:


# define subcontractor (agent) constraints
sub_constr = list(range(len(sub)))
for i in range(len(sub)):
    sub_constr[i] = mymodel.Constraint(0,1)
    for j in range(len(proj)):
        sub_constr[i].SetCoefficient(assign[i][j], 1)


# In[21]:


# define project (task) constraints
proj_constr = list(range(len(proj)))
for j in range(len(proj)):
    proj_constr[j] = mymodel.Constraint(1,1)
    for i in range(len(sub)):
        proj_constr[j].SetCoefficient(assign[i][j], 1)


# In[22]:


# Solve the model and print optimal solution
status = mymodel.Solve()                 # solve mymodel and display the solution

print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Cost = %.2f' % TotCost.Value())


# In[23]:


# Display the assignments
for i in range(len(sub)):
    print(sub[i])
    for j in range(len(proj)):
        print(proj[j], assign[i][j].solution_value())
        


# In[ ]:




