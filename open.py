# -*- coding: utf-8 -*-
#Open
import time
import os

etat = open("etat.txt", "r")
etat = etat.read()
if(etat == "Fermé !"):
    os.system("gpio mode 2 out; gpio mode 3 in")
    # Attendre
    time.sleep(17)
    os.system("gpio mode 2 in; gpio mode 3 in")
    etat = open("etat.txt", "w")
    etat.write("Ouvert !")
elif(etat == "Ouvert !"):
    print("Déjà ouvert !")
else:
    print("ERROR !!")
