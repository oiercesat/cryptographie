# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:01:44 2022

@author: oierc
"""

#Variables globales

alpha = 'abcdefghijklmnopqrstuvwxyz'



#---------------------#Fonction pour les alphabets---------------------

#Assigne un index pour chaque lettre dans un dictionnaire

def corresp(alpha):
     dic={}
     for i in range (len(alpha)):
         dic[alpha[i]]=i
     return dic

#Renvoie la lettre correspondant au nombre dans un dictionnaire d'alphabet passe en parametre

def recupereLettre(nombre, dico):
    for lettre in dico:
        if (dico[lettre]==nombre):
            return lettre
        
        
        
        
#---------------------Fonction de cryptage avec l'algorithme de César---------------------


#Cryptage de César prenant en parametre le message la cle (le decalage) et l'alphabet utilisé

def chiffreCesar(message,cle,alpha):
    resultat=""
    dic=corresp(alpha)
    for lettre in message:
        numero=(dic[lettre]+cle)%len(alpha)
        resultat+=recupereLettre(numero, dic)
    return resultat


#Decryptage de César prenant en parametre le message la cle (le decalage) et l'alphabet utilisé

def deChiffreCesar(message,cle,alpha):
    resultat=""
    dic=corresp(alpha)
    for lettre in message:
        numero=(dic[lettre]-cle)%len(alpha)
        resultat+=recupereLettre(numero, dic)
    return resultat

#--------------------- Euclide étendu ---------------------

def euclide_etendu(nombre1,nombre2):
    r0=nombre1
    r1=nombre2
    r=0
    u0=1
    v0=0
    u1=0
    v1=1
    u=0
    v=0
    
    while (r1!=0):
        
        r=r0%r1
        q=r0//r1
        u=u0-q*u1
        v=v0-q*v1
        r0=r1
        r1=r
        u0=u1
        u1=u
        v0=v1
        v1=v
        print(r,q,u,v,r0,r1)
        
    return r0,u0,v0
    
    
        
        
        
        