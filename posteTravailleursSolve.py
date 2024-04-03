from gurobipy import *


def solve(*args):
    rh = Model("Ressources Humaines")
    x = []
    j=args
    for i in range(len(args)):
        x.append(rh.addVar(lb=0, vtype=GRB.INTEGER, name='J' + str(i + 1)))

    rh.setObjective(quicksum(x[i] for i in range(len(args))), GRB.MINIMIZE)


    for k in range(len(j)):
        if (k < len(j)-2):
            limit1 = k + 1
            limit2 = limit1 + 1
        elif (k == len(j)-2):
            limit1 = len(j)-1
            limit2 = 0
        else:
            limit1 = 0
            limit2 = 1
        rh.addConstr(
                quicksum( x[i] for i in range(len(args)) if i != limit1 and i != limit2) >= j[k],
                "nombre-travailleurs" + str(k)
            )

    rh.optimize()
    print(rh.getVars(),rh.objVal)
    for var in rh.getVars():
        print(var.varName, '=', var.x)

    print("Objective value =", rh.objVal)
    return rh

#solve(17,13,15,19,14,16,11)


