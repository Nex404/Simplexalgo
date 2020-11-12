#####################################################################################
# This is an open source project for the implementation of the Simplex Algorithm    #
# If you use this Code, you have to include the author of the original code.        #
# You are free to modify this code                                                  #
# @author Lukarion20000, Nex404                                                     #
#####################################################################################

import numpy as np

dim = 0
zf = []
vars = [] #n-dim: x1...xn
operator = []
res = []
schnittpunkte = []
valid_bool = [] #schnittpunkte valid
####NEU
iterators = [] #iteratoren um n-dimensionale aufgaben zu lösen
letzter_schnittpunkt = True
carry_flag = True
####


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
        # print(x)
        return x
    else:
        print("not solvable")
        return 0

# einlesen in NF, ZF und NB
def einleser():
    global dim 
    dim = int(input("In welcher Dimension wird gerechnet?:"))

    ####NEU
    for x in range(dim)
    	iterators.append(x) #iteratoren starten auf [0][1]...[n]
    ####

    global zf
    zf = input("Bitte gebe die ZF an (Bsp.: 3*x1+2*x2+17*x3 == 3, 2, 17):").split(",")
    zf = list(zf)
    # print(type(zf))
    # print(type(zf[1]))
    for x in range(len(zf)):
        zf[x] = float(zf[x])

    # print(type(zf[1]))
    global optimierungsrichtung
    optimierungsrichtung = input("Eingabe der Optimierungsrichtung (min/max):")
    while True:
        if input("Weitere NB? (y/n):") == "y":
            v = input("Bitte gebe die NB in NF an (Variablenteil):").split(",")
            v = list(v)
            # print(v)
            # print(type(v))

            for x in range(len(v)):
                v[x] = float(v[x])   

            # print(type(v[1])) 
            # print(v)
            # print(type(v))
            # print(type(v[0]))
            # global vars
            vars.append(v)

            op = input("Operator eingeben (<= : k, >= : g):")
            if op == "k":
                operator.append("<=")
            else:
                operator.append(">=")


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
                weitere_nb.append(1) 
            else:
                weitere_nb.append(0)
        vars.append(weitere_nb)

    # print(vars)
    # Berrechnung Anzahl Schnittpunkte der NBs

    ####NEU
    # double check the dimension iterators (Wiederholung der Funktion würde sonst nur abbrechen)
    for x in range(dim)
    	iterators[x] = x
    letzter_schnittpunkt = False
    while(letzter_schnittpunkt == False)
    	new_array_var = []
    	new_array_res = []
    	for d in range(dim)
    		new_array_var.append(vars[iterators[d]])
    		new_array_res.append(vars[iterators[d]])
    	try:
            schnittpunkte.append(calc_cut(new_array_var,new_array_res))
        except Exception as e:
            pass	
    	for d in range(dim)
    		if iterators[dim-(1+d)] == len(vars)-(1+d):
    			letzter_schnittpunkt = True
    		else:
    			letzter_schnittpunkt = False
    			break
    	carry_flag == True
    	if letzter_schnittpunkt == False:
    		for d in range(dim):
    			if iterators[dim-(1+d)] == len(vars)-(1+d) and carry_flag == True:
    				iterators[dim-(1+d)] = iterators[dim-(2+d)] + 2
    				carry_flag = True
    			elif iterators[dim-(1+d)] != len(vars)-(1+d) and carry_flag == True:
    				iterators[dim-(1+d)] = iterators[dim-(1+d)] + 1
    				carry_flag = False


    ####

    #for x in range(len(vars)):
    #    for j in range(x+1, len(vars)):
    #        # print(j)
    #        new_array_var = []
    #        new_array_var.append(vars[x])
    #        new_array_var.append(vars[j])
    #        # print(new_array_var)
    #        
    #        # hier bei res muesste ein fehler passieren
    #        new_array_res = []
    #        new_array_res.append(res[x])
    #        new_array_res.append(res[j])
    #        # print(new_array_res)
    #        # print(new_array_var)
    #        # print(new_array_res)
    #        try:
    #            schnittpunkte.append(calc_cut(new_array_var,new_array_res))
    #        except Exception as e:
    #            pass


def test_valid():
    # testen der Schnittpunkte ob in allen NB valide
    # iterieren durch die Schnittpunkte
    for x in range(len(schnittpunkte)):
        # iterieren durch die NBs
        valid_bool.append(True)
        for y in range(len(vars)):
            ergebnis = 0
            hilf = vars[y]
            schnittpunkte_hilf = schnittpunkte[x]
            for n in range(dim):
                ergebnis += hilf[n] * schnittpunkte_hilf[n]
            
            # Ergebnis Valide?
            if operator[y] == "<=":
                if ergebnis > res[y]:
                    valid_bool[x] = False
                    break

            if operator[y] == ">=":
                if ergebnis < res[y]:
                    valid_bool[x] = False
                    break
            # print(x,y)
            # normalerweise noch casn von "<" bzw ">"

                    
                
    # speichern der nicht validen schnittpunkt STELLEN in ein extra array

    # entfernen der Schnittpunkte an den Stellen von hinten nach vorn


def opt():
    # optimalen Punkt (Eckpunkt) ermitteln und ausgeben
    opt = 0
    
    # unterschied min/max
    dim_of_zf = len(zf)
    # print(dim_of_zf)
    num_opt = 0
    for alpha in range(len(valid_bool)):
        if valid_bool[alpha] == True:
            num_opt = alpha
            break
    # schnittpunkte an der Stelle Alpha
    s_start = schnittpunkte[num_opt]
    # setzen eines allgemeinen Startwerts von opt
    for q in range(dim_of_zf):
        opt += s_start[q] * zf[q] 


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
dim = 2
zf = [-5,-8]
vars = [[5,2], [1,5], [1,1]]
optimierungsrichtung = "min"
res = [24, 24, 6]
operator = ["<=", "<=", "<="]#, "<=", "<="]

# calc_cut(vars, res)
# einleser()
calc_schnittpunkte()
# for x in schnittpunkte:
#     print(x)
test_valid()
# for x in valid_bool:
#     print(x)
opt()