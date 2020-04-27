  
from Data import data
from Data import users
from Data import sugges
import matplotlib.pyplot as plt
import json
import numpy
import os

#
clear = lambda: os.system('cls') #on Windows System

#### FICHIER DE REGROUPEMENT DES FONCTIONS ANNEXES ####

# Fonction de creation de pays vide 
def pays_vide(): 
    entree = {}
    entree['Government'] = {}
    entree['Government']['Country name'] = {}
    entree['Government']['Country name']['conventional short form']={}

    entree['People and Society'] = {}
    entree['People and Society']['Population'] = {}
    entree['People and Society']['Population growth rate']={}
    entree['People and Society']['Health expenditures']={}
    entree['People and Society']['Education expenditures']={}

    entree['Military and Security'] ={}
    entree['Military and Security']['Military expenditures']={}

    entree['People and Society']['Age structure'] = {}
    entree['People and Society']['Age structure']['0-14 years'] = {}
    entree['People and Society']['Age structure']['15-24 years'] = {}
    entree['People and Society']['Age structure']['25-54 years'] = {}
    entree['People and Society']['Age structure']['55-64 years'] = {}
    entree['People and Society']['Age structure']['65 years and over'] = {}

    entree['Economy'] = {}
    entree['Economy']['Inflation rate (consumer prices)'] = {}
    entree['Economy']['Debt - external'] = {}
    entree['Economy']['Unemployment rate'] = {}

    entree['Geography'] = {}
    entree['Geography']['Area'] = {}
    entree['Geography']['Area']['total'] = {}
    print ("Creation de pays vide terminee")

    return(entree)

# Fonction test d'un nombre ou d'une chaîne de caractère
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Fonction de récupération de code pays 
def get_code(nom_pays): 
    code = ''
    for code_pays in range(len(data)) :
        code = ''
        # On verifie la presence des noms à chaque etape

        if data[code_pays].get('Government') : 
            if data[code_pays]['Government'].get('Country name') :
                if data[code_pays]['Government']['Country name'].get('conventional long form') :
                    if data[code_pays]['Government']['Country name']['conventional long form']['text'] == nom_pays :
                        code = code_pays
                        
                        break
                if data[code_pays]['Government']['Country name'].get('conventional short form') :
                    if data[code_pays]['Government']['Country name']['conventional short form']['text'] == nom_pays :
                        code = code_pays
                        
                        break
                if data[code_pays]['Government']['Country name'].get('local long form') :
                    if data[code_pays]['Government']['Country name']['local long form']['text'] == nom_pays :
                        code = code_pays
                        
                        break
                if data[code_pays]['Government']['Country name'].get('local short form') :
                    if data[code_pays]['Government']['Country name']['local short form']['text'] == nom_pays :
                        code = code_pays
                        
                        break

    if code == '' :
        raise NameError('Pays introuvable')
    else :
        return(code)

# Fonction de création de listes 
# liste des comptes 
def account_list(users): 
    liste =[]
    for i in users : 
        liste.append(i['ID']['username'])
    return(liste)

def password_list(users): 
    liste =[]
    for i in users : 
        liste.append(i['ID']['mdp'])
    return(liste)

def type_liste(users): 
    liste =[]
    for i in users : 
        liste.append(i['type'])
    return(liste)
