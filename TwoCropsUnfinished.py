# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:28:05 2023

Note that this script is incomplete.
Locations marked with XXX need completion

LINEAR OPTIMIZATION EXAMPLE FOR A FARM GROWING 2 CROPS, USING FMINCON

As each optimization problem, this code consists of 3 main elements
1 a specification of independent (or decision, control) variables
2 a specification of the objective (or utility, goal) function, to be
  optimised
3 a specification of the domain of feasibility (or allowable solutions),
  which may involve upper/lower bounds as well as constraints
Next to that, some post processing and plotting of results is added

GENERAL PROBLEM DESCRIPTION

A farm grows 2 crops (A and B) and wants to optimize profit.
The crops differ in yield, costs, market price and water demands.
Natural resources are constrained (land and water).

@author: KrolMS
"""
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
from scipy.optimize import Bounds

"""
INDEPENDENT VARIABLES IN OPTIMIZATION

x:  x[0] production area crop A [ha]
    x[1] production area crop B [ha]


UTILITY FUNCTION

The profit function below quantifies farm profit to be used for MINIMIZE, a 
minus sign is added making it a net loss, as the algorithm is seeking for a
minimum
"""

def NetLoss(x):
# parameters on farm performance
    yA = 2.          # yield crop A [t/ha]
    yB = 5.          # yield crop B [t/ha]
    cA = 2.          # fixed cost production crop A [k$/ha]
    cB = 5.          # fixed cost production crop B [k$/ha]
    pA = 6.          # base market price crop A [k$/t]
    pB = 4.          # base market price crop B [k$/t]

# XXX ADD A PROFIT FUNCTION
    NetProfit = XXX
   
    return - NetProfit

"""
DOMAIN OF FEASIBILITY

Linear constraints result from limited water and land availability
"""
# parameters on constraints
LandTot  =    20.   # available land [ha]
WaterTot = 75000.   # available water [m3]
IA       =  2500.   # irrigation water use crop A [m3/ha]
IB       =  5000.   # irrigation water use crop B [m3/ha]

# defining linear constraint c <= A.*x <= b
# XXX FILL MATRIX AND ADD VALUES
ALinConstr = np.zeros([2,2])
ALinConstr[0,0] = XXX
ALinConstr[0,1] = XXX
ALinConstr[1,0] = XXX
ALinConstr[1,1] = XXX

# setting upper (and here redundant lower) values for the constraint
bLinConstr = np.zeros(2)
cLinConstr = -np.inf*np.ones(2)  # set a minus infinity: one-sided constraints
bLinConstr[0] = XXX
bLinConstr[1] = XXX
linear_constraints = LinearConstraint(ALinConstr,lb=cLinConstr,ub = bLinConstr)

xlb = np.zeros(2)                # areas non-negative
xub = LandTot                    # maximum area also upper bound for each crop
bounds = Bounds(lb=xlb,ub=xub)

"""
CALL OF OPTIMIZATION ALGORITHM

Preferably, first define a feasible initialization. It may save the need for
the algorithm to first find the domain of feasibility.
MINIMIZE uses x0 to define the dimensionality of the optimization problem.
"""
# XXX HERE ENTRE A FEASIBLE STARTING POINT
x0 = XXX

# Call of optimization procedure
res = minimize(NetLoss, x0, method='trust-constr',
               bounds=bounds, constraints=linear_constraints,
               options={'xtol': 1e-8, 'barrier_tol': 1e-8,'disp': True,
                        'maxiter':10000})

"""
GENERATION OF OUTPUT

Relevant optimization output to check out:

res.succes         % Process indicator of optimization process. Always
                     check! If True you can interpret results
                     Otherwise, diagnose how convergence can still be
                     achieved, or whether constraints are inconsistent.
res.x              % The optimal solution, where the objective is minimal 
-res.fun           % Maximum profit found (or, in general: fval is the
                     minimum identified. 
res.v[0]           % Lagrange multipliers for the inequality constraints
                     can be interpreted as "shadow prices" or opportunity
                     cost.
res.v[1]           % Lagrange multipliers for the bounds on the solution
"""

# XXX SOME OUTPUT VARIABLES, IF YOU LIKE THEM, NEED COMPLETION
print(" ")
print("Successfull optimization: ",res.success)
print("Message on termination: ",res.message)
print("Number of iteraions: ",res.nit)
print(" ")
print("Area A ", round(res.x[0],1),"ha")
print("Area B ", round(res.x[1],1),"ha")
print(" ")
print("Land use ", XXX,"ha, out of ", round(LandTot,1))
print("Water use ", XXX,"m3, out of ", round(WaterTot,0))
print(" ")
print("Net profit ", round(- res.fun,1),"k$")
print(" ")
print("Lagrangge multiplier for land constraint ", round(res.v[0][0],1),"k$/ha")
print("Lagrangge multiplier for water constraint ", round(res.v[0][1],4),"k$/m3")
print(" ")
print("Lagrangge multiplier for bounds crop A ", round(res.v[1][0],1),"k$/ha")
print("Lagrangge multiplier for bounds crop B ", round(res.v[1][1],1),"k$/ha")
