# -*- coding: utf-8 -*-
#Close
import time
import os

etat = open("etat.txt", "r")
etat = etat.read()
if(etat == "Ouvert !"):
    os.system("gpio mode 2 in; gpio mode 3 out")
    # Attendre
    time.sleep(17)
    os.system("gpio mode 2 in; gpio mode 3 in")
    etat = open("etat.txt", "w")
    etat.write("Fermé !")
elif(etat == "Fermé !"):
    print("Déjà fermé !")
else:
    print("ERROR !!")
