from gurobipy import *

def solve(zone_site,sites,zones,weights):
#site1          A B C 0 0 0
#site2          0 0 0 D E F
#site3  ou se trouve se site    zone_site[i][0]*x[i]

    pos = Model("positionnement")
    x = []
    for i in range(sites):
        x.append(pos.addVar(lb=0, vtype=GRB.BINARY, name='site' + str(i+1)))

    pos.setObjective(quicksum(x[i] for i in range(sites)), GRB.MINIMIZE)

    w = weights  #zone 4 antennas >= 2  noMin/zone

    for j in range(zones):
        pos.addConstr(
            quicksum(zone_site[i][j] * x[i] for i in range(sites)) >= weights[j],
            "le min des Antennes pour la zone " + str(j)
        )

    pos.optimize()

    for var in pos.getVars():
        print(var.varName, '=', var.x)

    print("Objective value =", pos.objVal)
    return pos
