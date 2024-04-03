from gurobipy import *

#rendement_values, prix_values, mo_ouvriers_values, temps_machine_values, eau_values, salaire_values,frais_fixe_values, water_value, workers_value, hour_value
def solve(*args):

    benefices = []
    depenses = []
    profit = []

    for i in range(len(args[0])):
        benefices.append(args[0][i] * args[1][i])
        dep = 0.1 * float(args[4][i]) + 30 * float(args[3][i]) + float(args[6][i])+int(args[2][i])*float(args[5][i])
        depenses.append(dep)
        profit.append(benefices[i] - depenses[i])

    agriculture = Model("agriculture")
    x = []
    cultures = args[10]
    zoneT = args[11]
    for i in range(cultures):
        x.append(agriculture.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x' + str(i+1)))

    agriculture.setObjective(quicksum(profit[i] * x[i] for i in range(cultures)), GRB.MAXIMIZE)
    listZone = []
    for i in range(cultures):
        listZone.append(1)
    ressources_consommations = [args[4], args[2], args[3], listZone]

    ressources_disponibilité = [args[7], args[8], args[9], zoneT]
    for j in range(len(ressources_disponibilité)):
        agriculture.addConstr(
            quicksum(ressources_consommations[j][i] * x[i] for i in range(cultures)) <= ressources_disponibilité[j],
            "Limitation_des_ressources_" + str(j)
        )

    agriculture.optimize()

    for var in agriculture.getVars():
        print(var.varName, '=', var.x)

    print("Objective value =", agriculture.objVal)
    return agriculture

"""
rendement_values =           [75, 60, 55, 50, 60]
prix_values =                [60, 50, 66, 110, 60]
mo_ouvriers_values =         [2, 1, 2, 3, 2]
temps_machine_values =        [30, 24, 20, 28, 25]
eau_values =                  [3000, 2000, 2500, 3800, 3200]
salaire_values =              [500, 500, 600, 700, 550]
frais_fixe_values =           [250, 180, 190, 310, 320]
water_value = 250000000
workers_value = 3000
hour_value = 24000
zone=1000
cult=5
solve(rendement_values, prix_values, mo_ouvriers_values, temps_machine_values, eau_values, salaire_values,
      frais_fixe_values, water_value, workers_value, hour_value,cult,zone)"""
# Solved in 4 iterations and 0.01 seconds (0.00 work units)
# Optimal objective  1.654000000e+06
# x1 = 400.0
# x2 = 0.0
# x3 = 600.0
# x4 = 0.0
# x5 = 0.0
# Objective value = 1654000.0


