import numpy as np

dim = 0
zf = []
vars = [] #n-dim: x1...xn
operator = []
res = []
schnittpunkte = []
valid_bool = [] #schnittpunkte valid



# listofvars(array of array)    | list of results(array)
# x1 + x2 + x3 | e1
# x1 + x2 + x3 | e2
# x1 + x2 + x3 | e3
# Loesen eines LGS n-ter ordnung
def calc_cut(listofvars, listofresults):
    a = np.array(listofvars)
    b = np.array(listofresults)
    x = np.linalg.solve(a,b)

    if np.allclose(np.dot(a,x),b):
        print(x)
        return x
    else:
        print("not solvable")
        return 0

# einlesen in NF, ZF und NB
def einleser():
    global dim 
    dim = int(input("In welcher Dimension wird gerechnet?:"))
    global zf
    zf = [input("Bitte gebe die ZF an (Bsp.: 3*x1+2*x2+17*x3 == 3, 2, 17):")]
    global optimierungsrichtung
    optimierungsrichtung = input("Eingabe der Optimierungsrichtung (min/max):")
    while True:
        if raw_input("Weitere NB? (y/n):") == "y":
            v = input("Bitte gebe die NB in NF an (Variablenteil):")
            v = list(v)
            print(v)

            for x in range(len(v)):
                v[x] = float(v[x])    
            # print(v)
            # print(type(v))
            # print(type(v[0]))
            # global vars
            vars.append(v)

            # op = input("Operator eingeben (<,>,<=,>=):")
            op = "<="
            operator.append(op)

            r = input("Bitte gebe die NB in NF an (Ergebnisteil):")
            r = float(r)
            # global res
            res.append(r)
            # global anzahl_nb
        else:
            break

#  Loesen der n-verschiedenen gleichungen um die Schnittpunkte zu erhalten
def calc_schnittpunkte():
    # pushing axen bzw Ebenen in NB
    for y in range(dim):
        weitere_nb = []
        res.append(0)
        operator.append(">=")
        for z in range(dim):
            if z == y:
                # hier soll was schief laufen
                weitere_nb[z] = 1
            else:
                weitere_nb[z] = 0  
        vars.append(weitere_nb)


    # Berrechnung Anzahl Schnittpunkte der NBs
    for x in vars:
        j = x+1
        for j in range(len(vars)):
            new_array_var = []
            new_array_var.append(vars[x])
            new_array_var.append(vars[j])
            # hier bei res muesste ein fehler passieren
            new_array_res = []
            new_array_res.append(res[x])
            new_array_res.append(res[j])
            schnittpunkte.append(calc_cut(new_array_var, new_array_res))

def test_valid():
    # testen der Schnittpunkte ob in allen NB valide
    # iterieren durch die Schnittpunkte
    for x in range(len(schnittpunkte)):
        # iterieren durch die NBs
        for y in range(len(vars)):
            ergebnis = 0
            hilf = vars[y]
            schnittpunkte_hilf = schnittpunkte[x]
            for n in range(dim):
                ergebnis += hilf[n] * schnittpunkte_hilf[n]
            
            # Ergebnis Valide?
            if operator[y] == "<=":
                if ergebnis <= res[y]:
                    valid_bool[x] = True
                else:
                    valid_bool[x] = False

            if operator[y] == ">=":
                if ergebnis >= res[y]:
                    valid_bool[x] = True
                else:
                    valid_bool[x] = False
            
            # normalerweise noch casn von "<" bzw ">"
            
            if valid_bool[x] == False:
                break
                    
                
    # speichern der nicht validen schnittpunkt STELLEN in ein extra array

    # entfernen der Schnittpunkte an den Stellen von hinten nach vorn


def opt():
    # optimalen Punkt (Eckpunkt) ermitteln und ausgeben
    opt = 0
    
    # unterschied min/max
    dim_of_zf = len(zf)
    # print(dim_of_zf)
    num_opt = 0
    for alpha in valid_bool:
        if valid_bool[alpha] == True:
            num_opt = alpha
            break
    # schnittpunkte an der Stelle Alpha
    s_start = schnittpunkte[num_opt]
    # setzen eines allgemeinen Startwerts von opt
    for q in range(dim_of_zf):
        opt += zf[q] * s_start[q]


    for x in range(len(schnittpunkte)):
        # print(len(schnittpunkte))
        if valid_bool[x] == True:
            s_klein = schnittpunkte[x]
            zwischenergebnis = 0
            # zf ist aarray / schnittpunkte ist ein array of arrays
            for q in range(dim_of_zf):
                zwischenergebnis += zf[q] * s_klein[q]
            # hier noch unterschied zwischen min max
            if optimierungsrichtung == "min":
                if zwischenergebnis <= opt:
                    opt = zwischenergebnis
                    num_opt = x
            elif optimierungsrichtung == "max":
                if zwischenergebnis >= opt:
                    opt = zwischenergebnis
                    num_opt = x
    print("Optimaler Schnittpunkt ist " + str(schnittpunkte[num_opt]) +" mit Wert " + str(opt))  
    return num_opt     
    





# Test ohne einleser
zf = [0.5,1]
vars = [[2,1], [-0.5,1]]
res = [7,2]
operator = ["<=", "<="]

# einleser()
calc_schnittpunkte()
test_valid()
opt()