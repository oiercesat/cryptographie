# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:01:44 2022

@author: oierc
"""

#Variables globales

alpha = 'abcdefghijklmnopqrstuvwxyz'


#Fonction pour les alphabets

def corresp(alpha):
     dic={}
     for i in range (len(alpha)):
         dic[alpha[i]]=i
     return dic

def recupereLettre(nombre, dico):
    for lettre in dico:
        if (dico[lettre]==nombre):
            return lettre