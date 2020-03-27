#!/usr/bin/env python
# coding: utf-8

# ## HW8, Problem 1 Data

# In[1]:


# import Glop linear solver package
from ortools.linear_solver import pywraplp as glp

# each row (sublist corresponds to a single student)
# each element of a sublist corresponds to a project
proj = ["Project 0", "Project 1","Project 2","Project 3",
       "Project 4","Project 5","Project 6",]
    
student = list()
for stu in range(28):
    student.append("Student " + str(stu))
    
preference = [[2,5,3,2,4,4,5],
              [1,5,1,2,2,4,5],
              [2,5,4,4,5,5,3],
              [2,5,3,1,5,4,4],
              [2,4,3,1,5,5,5],
              [5,5,2,2,2,3,5],
              [2,5,2,3,4,5,5],
              [2,5,3,1,3,5,4],
              [1,5,2,3,4,5,1],
              [3,5,4,2,3,5,5],
              [2,5,2,2,2,2,5],
              [1,5,1,2,2,5,4],
              [1,4,1,2,1,4,5],
              [1,5,1,2,2,5,4],
              [1,5,1,1,4,5,4],
              [2,5,3,2,4,5,3],
              [1,5,1,2,4,3,4],
              [3,4,2,1,3,5,4],
              [5,4,3,5,5,4,5],
              [5,5,1,4,5,5,1],
              [2,5,1,1,4,5,4],
              [1,4,4,5,2,2,3],
              [4,5,1,1,5,5,5],
              [1,4,1,3,5,2,3],
              [1,3,1,2,2,4,5],
              [2,5,4,4,5,5,3],
              [2,4,3,2,3,5,4],
              [3,5,3,1,4,5,5]]


# In[2]:


# initialize LP model object
mymodel = glp.Solver('Consulting Projects', glp.Solver.GLOP_LINEAR_PROGRAMMING)


# In[3]:


# define decision variables
assign = list(range(len(student)))
for g in range(len(student)):
    assign[g] = list(range(len(proj)))
    for h in range(len(proj)): 
        assign[g][h] = mymodel.NumVar(0, 1, student[g] + '-' + proj[h])
        


# In[4]:


# define objective function
TotScore = mymodel.Objective()          # create objective function object
TotScore.SetMaximization()              # set direction of optimization
for a in range(len(student)):
    for b in range(len(proj)): 
        TotScore.SetCoefficient(assign[a][b], preference[a][b])


# In[5]:


# define student constraints
stu_constr = list(range(len(student)))
for i in range(len(student)):
    stu_constr[i] = mymodel.Constraint(1,1)
    for j in range(len(proj)):
        stu_constr[i].SetCoefficient(assign[i][j], 1)


# In[6]:


# define project (task) constraints
proj_constr = list(range(len(proj)))
for j in range(len(proj)):
    proj_constr[j] = mymodel.Constraint(4,4)
    for i in range(len(student)):
        proj_constr[j].SetCoefficient(assign[i][j], 1)


# In[7]:


# Solve the model and print optimal solution
status = mymodel.Solve()
print('Solution Status =', status)
print('Number of variables =', mymodel.NumVariables())
print('Number of constraints =', mymodel.NumConstraints())

print('Optimal Solution:')

# The objective value of the solution.
print('Total Score = %.2f' % TotScore.Value())


# In[16]:


# The value of each variable in the solution.
for i in range(len(student)):
    print (student[i])
    for j in range(len(proj)): 
        #dvar[a][b] = mymodel.NumVar(0,1, "Student" + str(a) + "Project" + str(b))
        if (assign[i][j].solution_value() == 1):
            print("Assigned to: ", proj[j])


# In[ ]:




