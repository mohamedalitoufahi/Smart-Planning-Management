from gurobipy import *
from gurobipy import Model
from gurobipy import GRB
from gurobipy import quicksum

def chausseTous(months,s0,no0,Sal,cHsup,cMpr,h,H,Hmax,R,L,csr,dr):
    months = months
    s0 = s0
    no0 = no0
    Sal = Sal
    cHsup = cHsup

    h = h
    H = H
    Hmax = Hmax

    R = R
    L = L
    cMp = []
    cs = []
    nhs = []  # no heures supplementaires chaque mois
    nch = []  # no chaussures prod chaque mois
    nor = []  # no ouvriers recrutés chaque mois
    nol = []  # no ouvriers licenciés chaque mois
    s = []  # stock au debut du mois i
    no = []  # nombre d'ouvriers disponibles chaque mois
    d = []

    chTous = Model("ChausseTous")

    # s[0] = s0
    # no[0] = no0

    s.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='stock de pair de chaussures par mois' + str(0)))
    no.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='no ouvriers le mois' + str(0)))

    for i in range(months):
        nhs.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='no heure supplementaire mois' + str(i + 1)))
        nch.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='no chaussures fabriqués mois' + str(i + 1)))
        nor.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='no ouvriers recrutées mois' + str(i + 1)))
        nol.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='no ouvriers licenciés mois' + str(i + 1)))
        s.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='stock de pair de chaussures par mois' + str(i + 1)))
        no.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='no ouvriers le mois' + str(i + 1)))
        cs.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='cout de stockage le mois' + str(i + 1)))
        d.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='la demande du mois' + str(i + 1)))
        cMp.append(chTous.addVar(lb=0, vtype=GRB.CONTINUOUS, name='cout de matiere premiere/chaussure le mois' + str(i + 1)))

    f = quicksum(Sal * no[i] for i in range(1, months + 1)) + quicksum(
        cs[i] * s[i] +R * nor[i] + L * nol[i] + cHsup * nhs[i] + cMp[i] * nch[i] for i in range(months))

    chTous.setObjective(f, GRB.MINIMIZE)

    for i in range(months):
        chTous.addConstr(s[i + 1] == (s[i] + nch[i] - d[i]))
        chTous.addConstr(no[i + 1] == no[i] + nor[i] - nol[i])
        chTous.addConstr(nhs[i] <= no[i] * Hmax)
        chTous.addConstr(h * nch[i] <= nhs[i] + no[i] * H)
        chTous.addConstr(s[i] + nch[i] >= d[i])
        chTous.addConstr(cs[i] == csr[i])
        chTous.addConstr(d[i] == dr[i])
        chTous.addConstr(cs[i] == csr[i])
        chTous.addConstr(cMp[i] == cMpr[i])

    chTous.addConstr(s[0] == s0)
    chTous.addConstr(no[0] == no0)
    chTous.optimize()

    # Affichage des résultats
    for var in chTous.getVars():
        print(var.varName, '=', var.x)

    print("Objective value =", chTous.objVal)

# months1 = 4 #nombre de mois
# s01 = 500 #stock initiale
# no01 = 100 #no ouvrier initiale
# Sal1 = 1500 #salaire
# #
# cHsup1 = 13 #cout 1h supp
# cMp1 = [15,13,14,15] #cout mp /paire de ch
# h1 = 4 #cout en heure /paire de chaussure
# H1 = 160 #volume horaire /mois pour un ouvrier
# Hmax1 = 20 #heure sup max /ouvrier /mois
# #
# R1 = 1600 #frais de recrutement
# L1 = 2000  #frais de licenciemenet
# #
# cs1 = [200,3,1,5] #cout de stockage
# d1 = [3000, 5000, 2000, 1000] #demande pour chaque mois
# chausseTous(months1,s01,no01,Sal1,cHsup1,cMp1,h1,H1,Hmax1,R1,L1,cs1,d1)