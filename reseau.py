from gurobipy import *


def solve_network_flow(edge_costs, noeuds_nb):
    risou = Model("Reseau")

    link = []
    for key in edge_costs:
        link.append(risou.addVar(vtype=GRB.BINARY, name='link' + str(key)))

    noeuds_depart = [i for i, key in enumerate(edge_costs) if key[0] == 0]
    noeuds_dest = [i for i, key in enumerate(edge_costs) if key[1] == (noeuds_nb - 1)]

    def indicedepdest(i):
        l1 = [j for j, key in enumerate(edge_costs) if key[0] == i]
        l2 = [j for j, key in enumerate(edge_costs) if key[1] == i]
        return l1, l2

    f = quicksum(link[i] * edge_costs[key] for i, key in enumerate(edge_costs))
    risou.setObjective(f, GRB.MINIMIZE)

    risou.addConstr(quicksum(link[j] for j in noeuds_depart) == 1)
    risou.addConstr(quicksum(link[j] for j in noeuds_dest) == 1)

    for i in range(1, noeuds_nb - 1):
        ldep, ldest = indicedepdest(i)
        risou.addConstr(quicksum(link[dep] for dep in ldep) - quicksum(link[dest] for dest in ldest) == 0)

    risou.optimize()
    for var in risou.getVars():
        print(var.varName, '=', var.x)

    print("Objective value =", risou.objVal)

    return risou

"""
# Example usage:
edge_costs = {(0, 1): 4, (0, 2): 3, (1, 4): 5, (1, 3): 6, (2, 1): 3, (2, 4): 4, (2, 5): 6,
              (3, 4): 2, (3, 6): 1, (4, 6): 3, (5, 4): 6}
noeuds_nb = 7

result, obj_value = solve_network_flow(edge_costs, noeuds_nb)

for var_name, value in result.items():
    print(var_name, '=', value)

print("Objective value =", obj_value)"""
