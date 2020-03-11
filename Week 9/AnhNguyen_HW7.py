#!/usr/bin/env python
# coding: utf-8

# In[65]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp


# In[66]:


# input parameters
Machine = ['Machine 1', 'Machine 2']  # list of subcontractors (agents)
Product = ['Product 1', 'Product 2', 'Product 3']  # list of projects (tasks)
hourcost = [[0.5, 2, 0.75],   # assignment costs - Machine 1                 
        [1, 1, 0.5] ]   # Machine 2
profit = [30, 50, 20]
LaborHrsConstraint = 100
MachineHrsConstraint = 40
PercentageConstraint1 = [(-0.5), 0.5, 0.5]
PercentageConstraint3 = [0.2, 0.2, (-0.8)]


# In[67]:


# initialize LP model object
mymodel = glp.Solver('BetterProductionsInc', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[68]:


# define decision variables
dvar = list(range(len(Product)))         # create a list to store one variable for each product

for i in range(len(Product)):
    dvar[i] = mymodel.NumVar(0, mymodel.infinity(), Product[i])


# In[69]:


# define objective function
TotProfit = mymodel.Objective()          # create objective function object
TotProfit.SetMaximization()              # set direction of optimization
for j in range(len(Product)):
    TotProfit.SetCoefficient(dvar[j], profit[j])


# In[70]:


# define constraints
constr = list(range(5))          # create a list to store each constraint

#1. Constraint with Number of units of Product 1
constr[0] = mymodel.Constraint(0, mymodel.infinity())
                                         # arguments: (lower bound, upper bound)
for a in range(len(Product)):        # loop to set the constraint coefficient for each variable
    constr[0].SetCoefficient(dvar[a], PercentageConstraint1[a]) #args: (variable, coefficient)
p=0


#2. Constraint with Number of units of Product 3
constr[1] = mymodel.Constraint(-mymodel.infinity(), 0)
                                         # arguments: (lower bound, upper bound)
for q in range(len(Product)):        # loop to set the constraint coefficient for each variable
    constr[1].SetCoefficient(dvar[q], PercentageConstraint3[q]) #args: (variable, coefficient)

#3. Constraint with machine hours
for w in range(len(Machine)):               # loop to create each constraint
    constr[w+2] = mymodel.Constraint(-mymodel.infinity(), MachineHrsConstraint)
                                         # arguments: (lower bound, upper bound)
    for p in range(len(Product)):        # loop to set the constraint coefficient for each variable
        constr[w+2].SetCoefficient(dvar[p], hourcost[w][p]) #args: (variable, coefficient)
p = 0

#4. Constraints with labor hours
constr[4] = mymodel.Constraint(-mymodel.infinity(), LaborHrsConstraint)
                                         # arguments: (lower bound, upper bound)
for p in range(len(Product)):        # loop to set the constraint coefficient for each variable
    constr[4].SetCoefficient(dvar[p], (2*hourcost[0][p] + hourcost[1][p])) #args: (variable, coefficient)
p = 0
    


# In[71]:


# Solve the model and print optimal solution
status = mymodel.Solve()
print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Profit = %.2f' % TotProfit.Value())

# The value of each variable in the solution.
for c in range(len(Product)):
    print('%s = %.2f' % (Product[c], dvar[c].solution_value()))


# In[77]:


# display constraint Information
print('Constraint \t \t LHS \t RHS \t Slack \t Dual')
LHS = mymodel.ComputeConstraintActivities()
print(LHS)
print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % ('ConstraintProd1', LHS[0], constr[0].Lb(),(constr[0].Lb() - LHS[0]), constr[0].dual_value()))
print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % ('ConstraintProd3', LHS[1], constr[1].Ub(),(constr[1].Ub() - LHS[1]), constr[1].dual_value()))
print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % ('Machine 1 hours', LHS[2], constr[2].Ub(),(constr[2].Ub() - LHS[2]), constr[2].dual_value()))
print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % ('Machine 2 hours', LHS[3], constr[3].Ub(),(constr[3].Ub() - LHS[3]), constr[3].dual_value()))
print('%s \t %.1f \t %.1f \t %.1f \t %.1f' % ('Labor hours    ', LHS[4], constr[4].Ub(),(constr[4].Ub() - LHS[4]), constr[4].dual_value()))

    
    


# In[78]:


#c. The value of an additional hour of labor is $12.5


# In[ ]:




