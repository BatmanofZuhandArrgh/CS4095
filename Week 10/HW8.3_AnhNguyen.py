#!/usr/bin/env python
# coding: utf-8

# In[45]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp


# In[46]:


# initialize LP model object
mymodel = glp.Solver('Tri-County Utilities', glp.Solver.GLOP_LINEAR_PROGRAMMING)
Suppliers = ["Southern Gas", "Northwest Gas"]
Supply = [500, 400]
Counties = ["Hamilton", "Butler", "Clermont"]
Demand = [400, 200, 300]
DistUnitCost = [[10, 20, 15],
                [12, 15, 18]]


# In[47]:


# Creating 
dvar = list(range(len(Suppliers)))
for a in range(len(Suppliers)):
    dvar[a] = list(range(len(Counties)))
    for b in range(len(Counties)):
        dvar[a][b] = mymodel.NumVar(0, mymodel.infinity(), Suppliers[a] + " supplying for " + Counties[b])


# In[48]:


# define objective function
TotCost = mymodel.Objective()          # create objective function object
TotCost.SetMinimization()              # set direction of optimization
for a in range(len(Suppliers)):
    for b in range(len(Counties)):
        TotCost.SetCoefficient(dvar[a][b], DistUnitCost[a][b])
        
        


# In[49]:


# define Suppliers constraints
sup_constr = list(range(len(Suppliers)))
for i in range(len(Suppliers)):
    sup_constr[i] = mymodel.Constraint(Supply[i],Supply[i])
    for j in range(len(Counties)):
        sup_constr[i].SetCoefficient(dvar[i][j], 1)


# In[50]:


# define Suppliers constraints
cou_constr = list(range(len(Counties)))
for j in range(len(Counties)):
    cou_constr[j] = mymodel.Constraint(Demand[j],Demand[j])
    for i in range(len(Suppliers)):
        cou_constr[j].SetCoefficient(dvar[i][j], 1)


# In[51]:


# Solve the model and print optimal solution
status = mymodel.Solve()
print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Score = %.2f' % TotCost.Value())


# In[52]:


# The value of each variable in the solution.
for a in range(len(Suppliers)):
    print (Suppliers[a])
    for b in range(len(Counties)): 
        if dvar[a][b].solution_value() != 0:
            print('%s = %.2f units' % (dvar[a][b], dvar[a][b].solution_value()))


# In[ ]:


#Since the solution is optimal, the suppliers have no more units
#of gas to supply, if the demand increases for Butler County,
#all things stay the same, we cannot ask the SGas or NGas to supply
#more gas. Tri-County should reach out to a new supplier

