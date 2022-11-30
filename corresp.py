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
        
    resulat=[]
    resulat.append(r0)
    resulat.append(u0)
    resulat.append(v0)
    return resulat
    
# --------------------- Chiffrement affine et déchiffrement affine --------------------- 

from collections import Counter


#fonction premetant de faire une analyse frequencielle des lettres presente dans le message
def lettreLesPlusFrequentes(message):
    c=Counter(message)
    freq=c.most_common(10)
    return freq

#permet de calculer l'inverse dans un modulo
def inverseMod(nb,mod):
    inverse=euclide_etendu(nb,mod)
    return inverse[1]

#Chiffrement affine
def chiffrementAffine(messageACrypte,a,b):
    resultat=""
    alphaDico=corresp(alpha)                        #cree un dico avec la la lettre comme cle et le rang comme valeur
    
    for iterator in range(len(messageACrypte)):
        j=alphaDico[messageACrypte[iterator]]       #recupere le rang de la lettre
        i=(j-b)*inverseMod(a, 26)                   #fait le calcule inverse de j=ai+b
        i=i%26                                      #met le resultat modulo 26
        lettreI=recupereLettre(i,alphaDico)         #recupere la lettre correspondant au rang i que l'ont vient de calculer
        resultat=resultat+lettreI
    return resultat

#Dechiffrement affine
def dechiffrementAffine(messageCrypte,a,b):
    alphaDico=corresp(alpha)                        #cree un dico avec la la lettre comme cle et le rang comme valeur
    resultat=""
    
    for iterator in range(len(messageCrypte)):
        j=alphaDico[messageCrypte[iterator]]        #recupere le rang de la lettre
        i=a*j+b                                     #fait le calcule de j=ai+b
        i=i%27                                      #met le resultat modulo 26
        lettreI=recupereLettre(i,alphaDico)         #recupere la lettre correspondant au rang i que l'ont vient de calculer
        resultat=resultat+lettreI
    return resultat


#chiffrement Vigenere


def chiffrementVigenere (message,cle):
    
    resultat=""
    alphaDico=corresp(alpha)
    tabCorresp =[]
    
    for lettre in cle :
        tabCorresp.append(alphaDico[lettre])
    
    for i in range(0,len(message),len(cle)):
        if (i+len(cle)<len(message)):
            for j in range(0,len(cle)):
                numero=(alphaDico[message[i+j]]+tabCorresp[j])%len(alpha)
                resultat+=recupereLettre(numero, alphaDico)
        else :
            lenRestant=len(message)-i
            for j in range(0,lenRestant):
                numero=(alphaDico[message[i+j]]+tabCorresp[j])%len(alpha)
                resultat+=recupereLettre(numero, alphaDico)
      
    print (resultat)
    
def dechiffrementVigenere(message,cle):
    
    resultat=""
    alphaDico = corresp(alpha)
    tabCorresp =[]
    
    for lettre in cle :
        tabCorresp.append(alphaDico[lettre])
    
    for i in range(0,len(message),len(cle)):
        if (i+len(cle)<len(message)):
            for j in range(0,len(cle)):
                numero=(alphaDico[message[i+j]]-tabCorresp[j])%len(alpha)
                resultat+=recupereLettre(numero, alphaDico)
        else :
            lenRestant=len(message)-i
            for j in range(0,lenRestant):
                numero=(alphaDico[message[i+j]]-tabCorresp[j])%len(alpha)
                resultat+=recupereLettre(numero, alphaDico)
    
    print (resultat)