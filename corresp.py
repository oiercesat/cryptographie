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


#Cryptage de Cesar prenant en parametre le message la cle (le decalage) et l'alphabet utilisé

def chiffreCesar(message,cle,alpha):
    resultat=""
    dic=corresp(alpha)
    for lettre in message:
        numero=(dic[lettre]+cle)%len(alpha)
        resultat+=recupereLettre(numero, dic)
    return resultat


#Decryptage de Cesar prenant en parametre le message la cle (le decalage) et l'alphabet utilise

def deChiffreCesar(message,cle,alpha):
    resultat=""
    dic=corresp(alpha)
    for lettre in message:
        numero=(dic[lettre]-cle)%len(alpha)
        resultat+=recupereLettre(numero, dic)
    return resultat

#--------------------- Euclide etendu ---------------------

def euclide_etendu(nombre1,nombre2):
    
    # Les restes
    r0=nombre1  # reste initialise avec le premier nombre qui sera uitlise comme Rn-2
    r1=nombre2  # reste initialise avec le deuxieme nombre qui sera uitlise comme Rn-1
    r=0         # reste initialise a 0 nombre qui sera uitlise comme Rn
    
    # Coefficent de Bezout
    
    #Initialisation des coefficients u
    u0=1        #coefficent u de la premiere etape 
    u1=0        #coefficent u de la deuxieme etape
    u=0         #coefficent u de l'etape n
    
    #Initialisation des coefficients v
    v0=0        #coefficent v de la premiere etape
    v1=1        #coefficent v de la deuxieme etape
    v=0         #coefficent v de l'etape n
    
    while (r1!=0):
        
        # Calculs 
        r=r0%r1         #calcule le reste de la division euclidienne 
        q=r0//r1        #calcule le quotient de la divion euclidienne
        u=u0-q*u1       #calcule le coefficient Un grace à Un-2 et Un-1
        v=v0-q*v1       #calcule le coefficient Un grace à Vn-2 et Vn-1
        
        # Affectation des nouvelles valeurs
        # les reste
        r0=r1           #Rn-2 prend la valeure de Rn-1
        r1=r            #Rn-1 prend la valeure de Rn
        
        # Les coefficients U
        u0=u1           #Un-2 prend la valeure de Un-1
        u1=u            #Un-1 prend la valeure de Un
        
        # Les coefficents V
        v0=v1           #Vn-2 prend la valeure de Vn-1
        v1=v            #Vn-1 prend la valeure de Vn
        
    return r0,u0,v0
    
    
        
        
        
        