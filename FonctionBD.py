from Data import data
from Data import users
from Data import sugges
import json
import numpy
# Les bases de données ne sont pas modifíées totalement pour l'instant, à faire après 

#### Fonctions sur les pays ####

# Fonction annexe de creation de pays vide 
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
# Fonction teste d'un nombre ou d'une chaîne de caractère

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Fonction affichage d'un pays sous forme de tableau

def affichage(nom_ou_code_pays):

    if is_number(nom_ou_code_pays) is False :

        code = ''

        for code_pays in range(len(data)) :

            if data[code_pays].get('Government') :
                if data[code_pays]['Government'].get('Country name') :
                    if data[code_pays]['Government']['Country name'].get('conventional long form') :
                        if data[code_pays]['Government']['Country name']['conventional long form']['text'] == nom_ou_code_pays :
                            code = code_pays
                    if data[code_pays]['Government']['Country name'].get('conventional short form') :
                        if data[code_pays]['Government']['Country name']['conventional short form']['text'] == nom_ou_code_pays :
                            code = code_pays
                    if data[code_pays]['Government']['Country name'].get('local long form') :
                        if data[code_pays]['Government']['Country name']['local long form']['text'] == nom_ou_code_pays :
                            code = code_pays
                    if data[code_pays]['Government']['Country name'].get('local short form') :
                        if data[code_pays]['Government']['Country name']['local short form']['text'] == nom_ou_code_pays :
                            code = code_pays

        if code == '' :
            raise NameError('Pays introuvable')
        else :
            nom_ou_code_pays = code


    inf1 = data[nom_ou_code_pays]['Government']['Country name']['conventional short form']['text']
    inf2 = data[nom_ou_code_pays]['Geography']['Area']['total']['text']
    inf3 = data[nom_ou_code_pays]['People and Society']['Population']['text']
    inf4 = data[nom_ou_code_pays]['People and Society']['Population growth rate']['text']
    inf5 = data[nom_ou_code_pays]['Economy']['Inflation rate (consumer prices)']['text']
    inf6 = data[nom_ou_code_pays]['Economy']['Debt - external']['text']
    inf7 = data[nom_ou_code_pays]['Economy']['Unemployment rate']['text']
    inf8 = data[nom_ou_code_pays]['People and Society']['Health expenditures']['text']
    inf9 = data[nom_ou_code_pays]['People and Society']['Education expenditures']['text']
    inf10 = data[nom_ou_code_pays]['Military and Security']['Military expenditures']['text']
    inf11 = data[nom_ou_code_pays]['People and Society']['Age structure']

    return numpy.array([['Nom du pays', inf1],
                        ['Superficie', inf2],
                        ['Population', inf3],
                        ['Croissance démographique', inf4],
                        ['Inflation', inf5],
                        ['Dette', inf6],
                        ['Taux de chômage', inf7],
                        ['Taux de dépenses en santé', inf8],
                        ['Taux de dépenses en éducation', inf9],
                        ['Taux de dépenses militaires', inf10],
                        ['Classe des 0-14 ans', inf11['0-14 years']['text']],
                        ['Classe des 15-24 ans', inf11['15-24 years']['text']],
                        ['Classe des 25-54 ans', inf11['25-54 years']['text']],
                        ['Classe des 55-64 ans', inf11['55-64 years']['text']],
                        ['Classe des 65 ans et plus', inf11['65 years and over']['text']]])

# Fonction suppression d'un pays

def suppression(nom_ou_code_pays):
    if is_number(nom_ou_code_pays) is True :
        if nom_ou_code_pays > len(data) :
            raise NameError('Pays introuvable')

    if is_number(nom_ou_code_pays) is False :

        code = ''

        for code_pays in range(len(data)) :

            if data[code_pays].get('Government') :
                if data[code_pays]['Government'].get('Country name') :
                    if data[code_pays]['Government']['Country name'].get('conventional long form') :
                        if data[code_pays]['Government']['Country name']['conventional long form']['text'] == nom_ou_code_pays :
                            code = code_pays
                    if data[code_pays]['Government']['Country name'].get('conventional short form') :
                        if data[code_pays]['Government']['Country name']['conventional short form']['text'] == nom_ou_code_pays :
                            code = code_pays
                    if data[code_pays]['Government']['Country name'].get('local long form') :
                        if data[code_pays]['Government']['Country name']['local long form']['text'] == nom_ou_code_pays :
                            code = code_pays
                    if data[code_pays]['Government']['Country name'].get('local short form') :
                        if data[code_pays]['Government']['Country name']['local short form']['text'] == nom_ou_code_pays :
                            code = code_pays

        if code == '' :
            raise NameError('Pays introuvable')
        else :
            nom_ou_code_pays = code

    del data[nom_ou_code_pays]

    return data
# Fonction ajout / modification 
def ajout_pays(data): 
    while True : 
        Nom = input("Entrer le nom du pays a ajouter : ") 
        #on suppose dans un premier temps que l'user rentre quelque chose 
        if Nom != 'none':
            break
    
    # La fonction demande à l'utilisateur s'il souhaite ajouter des informations
    complementaire = input('Voulez vous ajouter des informations ? (Y/N)')
    # Si l'utilisateur accepte 
    if complementaire in ["Y","y"]: 
        liste_info = []
        superficie = input('Entrez la superficie du pays en km2, tapez None pour passer la question :')
        liste_info.append(superficie)
        pop = input('Entrez la population du pays en million d\'individus , tapez None pour passer la question :')
        liste_info.append(pop)
        crois = input('Entrez la croissance demographique du pays en pourcentage , tapez None pour passer la question :')
        liste_info.append(crois)
        inflation = input('Entrez l\'inflation du pays en pourcetage, tapez None pour passer la question :')
        liste_info.append(inflation)
        dette = input('Entrez la dette du pays en million de dollars, tapez None pour passer la question :')
        liste_info.append(dette)
        chom = input('Entrez la taux de chomage du pays en pourcentage, tapez None pour passer la question :')
        liste_info.append(chom)
        sante = input('Entrez le taux de depense en sante du pays en pourcentage, tapez None pour passer la question :')
        liste_info.append(sante)
        edu = input('Entrez le taux de depense en education du pays en pourcentage, tapez None pour passer la question :')
        liste_info.append(edu)
        army = input('Entrez le taux de depense militaire du pays en pourcentage, tapez None pour passer la question :')
        liste_info.append(army)

        # Entree des 5 classes d\'age
        age1 = input('Entrez le pourcentage de la classe 1, tapez None pour passer la question :')
        liste_info.append(age1)
        age2 = input('Entrez le pourcentage de la classe 2, tapez None pour passer la question :')
        liste_info.append(age2)
        age3 = input('Entrez le pourcentage de la classe 3, tapez None pour passer la question :')
        liste_info.append(age3)
        age4 = input('Entrez le pourcentage de la classe 4, tapez None pour passer la question :')
        liste_info.append(age4)
        age5 = input('Entrez le pourcentage de la classe 5, tapez None pour passer la question :')
        liste_info.append(age5)

    # Creation de l'entree
    entree = pays_vide()
    entree['Government']['Country name']['conventional short form']['text'] = Nom
    print("Votre pays a bien ete cree")
    if len(liste_info) >0 : 
        if liste_info[0] not in ['None','none']: 
            entree['Geography']['Area']['total']['text'] = liste_info[0]
        if liste_info[1] not in ['None','none']: 
            entree['People and Society']['Population']['text'] = liste_info[1]
        if liste_info[2] not in ['None','none']: 
            entree['People and Society']['Population growth rate']['text'] = liste_info[2]
        if liste_info[3] not in ['None','none']: 
            entree['Economy']['Inflation rate (consumer prices)']['text'] = liste_info[3]
        if liste_info[4] not in ['None','none']: 
            entree['Economy']['Debt - external']['text'] = liste_info[4]
        if liste_info[5] not in ['None','none']: 
            entree['Economy']['Unemployment rate']['text'] = liste_info[5]
        if liste_info[6] not in ['None','none']: 
            entree['People and Society']['Health expenditures']['text'] = liste_info[6]
        if liste_info[7] not in ['None','none']: 
            entree['People and Society']['Education expenditures']['text'] = liste_info[7]
        if liste_info[8] not in ['None','none']: 
            entree['Military and Security']['Military expenditures']['text'] = liste_info[8]
        if liste_info[9] not in ['None','none']: 
            entree['People and Society']['Age structure']['0-14 years']['text'] = liste_info[9]
        if liste_info[10] not in ['None','none']: 
            entree['People and Society']['Age structure']['15-24 years']['text'] = liste_info[10]
        if liste_info[11] not in ['None','none']: 
            entree['People and Society']['Age structure']['25-54 years']['text'] = liste_info[11]
        if liste_info[12] not in ['None','none']: 
            entree['People and Society']['Age structure']['55-64 years']['text'] = liste_info[12]
        if liste_info[13] not in ['None','none']: 
            entree['People and Society']['Age structure']['65 years and over']['text'] = liste_info[13]
        print('Vos informations complementaires ont bien ete enregistrees')
        print("Le pays suivant va etre ajoute : ")
        print(entree)

    data.append(entree)


#### Fonctions sur les comptes ####

# Fonctions annexes 
# liste des comptes 
def account_list(users): 
    liste =[]
    for i in users : 
        liste.append(i['ID']['username'])
    return(liste)

# Fonction de creation de compte 
def ajout_compte(users): 
    # On suppose que le compte qui a accès à cette fonction est administrateur
    new = {}
    new['ID'] = {}
    type_user = input("Entrez le type d'utilisateur que vous souhaitez creer : ")
    id_user = input("Entrez l'ID utilisateur que vous souhaitez creer : ")
    new['ID']['username'] = id_user
    mdp_user = input("Entrez le mot de passe utilisateur que vous souhaitez creer : ")
    mdp_confirmation = input("Confirmez votre mot de passe : ")
    while mdp_user != mdp_confirmation : 
        mdp_confirmation = input("Les deux mots de passe ne correspondent pas, veuiller reessayer : ")
    new['ID']['mdp'] = mdp_user
    new['type'] = type_user

    print("L'utilisateur",id_user,"vient d'etre cree et va etre ajouter a la base")
    users.append(new)
    with open("user.json", "w") as write_file:
        json.dump(users, write_file)

# Fonction de suppression
def suppression_compte(users): 
    liste = account_list(users)
    nom = input("Veuillez donner le nom du compte a supprimer : ")
    if nom in liste : 
        numero = liste.index(nom)
        del users[numero]
    with open("user.json", "w") as write_file:
        json.dump(users, write_file)

#### Suggestions #### 

def ajout_suggestion(): 
    liste_info = []
    Nom = input("Entrer le nom du pays a ajouter : ") 
    liste_info.append(Nom)
    superficie = input('Entrez la superficie du pays en km2, tapez None pour passer la question :')
    liste_info.append(superficie)
    pop = input('Entrez la population du pays en million d\'individus , tapez None pour passer la question :')
    liste_info.append(pop)
    crois = input('Entrez la croissance demographique du pays en pourcentage , tapez None pour passer la question :')
    liste_info.append(crois)
    inflation = input('Entrez l\'inflation du pays en pourcetage, tapez None pour passer la question :')
    liste_info.append(inflation)
    dette = input('Entrez la dette du pays en million de dollars, tapez None pour passer la question :')
    liste_info.append(dette)
    chom = input('Entrez la taux de chomage du pays en pourcentage, tapez None pour passer la question :')
    liste_info.append(chom)
    sante = input('Entrez le taux de depense en sante du pays en pourcentage, tapez None pour passer la question :')
    liste_info.append(sante)
    edu = input('Entrez le taux de depense en education du pays en pourcentage, tapez None pour passer la question :')
    liste_info.append(edu)
    army = input('Entrez le taux de depense militaire du pays en pourcentage, tapez None pour passer la question :')
    liste_info.append(army)

    # Entree des 5 classes d\'age
    age1 = input('Entrez le pourcentage de la classe 1, tapez None pour passer la question : ')
    liste_info.append(age1)
    age2 = input('Entrez le pourcentage de la classe 2, tapez None pour passer la question : ')
    liste_info.append(age2)
    age3 = input('Entrez le pourcentage de la classe 3, tapez None pour passer la question : ')
    liste_info.append(age3)
    age4 = input('Entrez le pourcentage de la classe 4, tapez None pour passer la question : ')
    liste_info.append(age4)
    age5 = input('Entrez le pourcentage de la classe 5, tapez None pour passer la question : ')
    liste_info.append(age5)

    sugges.append(liste_info)
    with open("Suggestions.json", "w") as write_file:
        json.dump(sugges, write_file)



    