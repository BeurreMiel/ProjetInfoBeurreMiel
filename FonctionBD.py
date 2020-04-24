  
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
# Fonction de creation de compte 
def ajout_compte(users): 
    # On suppose que le compte qui a accès à cette fonction est administrateur
    new = {}
    new['ID'] = {}
    while True : 
        type_user = input("Entrez le type d'utilisateur que vous souhaitez creer : (G/D) ")
        if type_user in ["G","g","D","D"] : #teste si c'est bien le bon type 
            break
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

def gestion_suggestion(): 
    n = len(sugges)
    while n > 0 :
        print("#####################################################")
        print("Voici la suggestion : ") 
        print("Nom du pays : ", sugges[0][0])
        print("Superficie du pays : ", sugges[0][1])
        print("Population du pays : ", sugges[0][2])
        print("Croissance démographique du pays : ", sugges[0][3])
        print("Inflation du pays : ", sugges[0][4])
        print("Dette du pays : ", sugges[0][5])
        print("Taux de chômage du pays : ", sugges[0][6])
        print("Depense sante du pays : ", sugges[0][7])
        print("Depense education du pays : ", sugges[0][8])
        print("Depense militaire du pays : ", sugges[0][9])
        print("Taux age1 : ", sugges[0][10])
        print("Taux age2 : ", sugges[0][11])
        print("Taux age3 : ", sugges[0][12])
        print("Taux age4 : ", sugges[0][13])
        print("Taux age5 : ", sugges[0][14])
        print("#####################################################")
        while True : 
            res = input("Vous pouvez accepter (A) ou rejeter (R) cette suggestion : ")
            if res in ["A","a","R","r"]: 
                break 
        
        if res in ["A","a"] : # Si l'admin accepte la suggestion 
            liste_info= sugges[0]
            nom_pays = liste_info.pop(0) # Recupere le nom du pays pour le placer correctement
            print ("Le pays ",nom_pays, "va être modifié :")
            nom_pays = get_code(nom_pays)
            # Test de présence du pays
            if len(liste_info) >0 : 
                if liste_info[0] not in ['None','none']: 
                    data[nom_pays]['Geography']['Area']['total']['text'] = liste_info[0]
                if liste_info[1] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Population']['text'] = liste_info[1]
                if liste_info[2] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Population growth rate']['text'] = liste_info[2]
                if liste_info[3] not in ['None','none']: 
                    data[nom_pays]['Economy']['Inflation rate (consumer prices)']['text'] = liste_info[3]
                if liste_info[4] not in ['None','none']: 
                    data[nom_pays]['Economy']['Debt - external']['text'] = liste_info[4]
                if liste_info[5] not in ['None','none']: 
                    data[nom_pays]['Economy']['Unemployment rate']['text'] = liste_info[5]
                if liste_info[6] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Health expenditures']['text'] = liste_info[6]
                if liste_info[7] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Education expenditures']['text'] = liste_info[7]
                if liste_info[8] not in ['None','none']: 
                    data[nom_pays]['Military and Security']['Military expenditures']['text'] = liste_info[8]
                if liste_info[9] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Age structure']['0-14 years']['text'] = liste_info[9]
                if liste_info[10] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Age structure']['15-24 years']['text'] = liste_info[10]
                if liste_info[11] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Age structure']['25-54 years']['text'] = liste_info[11]
                if liste_info[12] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Age structure']['55-64 years']['text'] = liste_info[12]
                if liste_info[13] not in ['None','none']: 
                    data[nom_pays]['People and Society']['Age structure']['65 years and over']['text'] = liste_info[13]
                print('Vos informations complementaires ont bien ete enregistrees : ')

        
        # Si la suggestion est refusée ou quand la modification a ete enregistree 
        del sugges[0]
        n= len(sugges) # On supprime le premier element de la liste de selection 
    
    print("La liste de suggestion est vide")

### Fonction représentation graphique ###

def representationgraphique(critere):
    
    #Erreurs
    if critere<2 or critere>10 :
        return('Critère inexistant')
        
    tranche1=[]
    tranche2=[]
    tranche3=[]
    tranche4=[]
    tranche5=[]
    crit=[]
    pays=[]

    #Séparation des tranches d'âges
    for j in range (len(data)):
        if data[j].get('People and Society'):
            if data[j]['People and Society'].get('Age structure'):
                tranche1.append(data[j]['People and Society']['Age structure']['0-14 years']['text'])
                tranche2.append(data[j]['People and Society']['Age structure']['15-24 years']['text'])
                tranche3.append(data[j]['People and Society']['Age structure']['25-54 years']['text'])
                tranche4.append(data[j]['People and Society']['Age structure']['55-64 years']['text'])
                tranche5.append(data[j]['People and Society']['Age structure']['65 years and over']['text'])
   
    #On garde les pourcentages
    TR1=[]
    for z in range(len(tranche1)):
        TR1.append(float(tranche1[z][:tranche1[z].find('%')]))
                         
    TR2=[]
    for z in range(len(tranche2)):
        TR2.append(float(tranche2[z][:tranche2[z].find('%')]))
    
    TR3=[]
    for z in range(len(tranche3)):
        TR3.append(float(tranche3[z][:tranche3[z].find('%')]))    
    
    TR4=[]
    for z in range(len(tranche4)):
        TR4.append(float(tranche4[z][:tranche4[z].find('%')]))    
   
    TR5=[]
    for z in range(len(tranche5)):
        TR5.append(float(tranche5[z][:tranche5[z].find('%')]))
        
        
        
    #Pour réaliser le diagramme en barres d’un certain critère  
    for i in range (len(data)):
        if critere==2:
            if data[i].get('Geography') and data[i].get('Government'):
                if data[i]['Geography'].get('Area') and data[i]['Government'].get('Country name'):
                    if data[i]['Geography']['Area'].get('total') and data[i]['Government']['Country name'].get('conventional short form'):
                        
                        crit.append(data[i]['Geography']['Area']['total']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==3:
             if data[i].get('People and Society') and data[i].get('Government'):
                if data[i]['People and Society'].get('Population') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
                        
                            crit.append(data[i]['People and Society']['Population']['text'])
                            pays.append(data[i]['Government']['Country name']['conventional short form']['text'])        
        
        elif critere==4:
             if data[i].get('People and Society') and data[i].get('Government'):
                if data[i]['People and Society'].get('Population growth rate') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
                        
                        crit.append(data[i]['People and Society']['Population growth rate']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==5:
             if data[i].get('Economy') and data[i].get('Government'):
                if data[i]['Economy'].get('Inflation rate (consumer prices)') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
                        
                        crit.append(data[i]['Economy']['Inflation rate (consumer prices)']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==6:
             if data[i].get('Economy') and data[i].get('Government'):
                if data[i]['Economy'].get('Debt - external') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
            
                        crit.append(data[i]['Economy']['Debt - external']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==7:
             if data[i].get('Economy') and data[i].get('Government'):
                if data[i]['Economy'].get('Unemployment rate') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
            
                        crit.append(data[i]['Economy']['Unemployment rate']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==8:
             if data[i].get('People and Society') and data[i].get('Government'):
                if data[i]['People and Society'].get('Health expenditures') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
            
                        crit.append(data[i]['People and Society']['Health expenditures']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==9:
             if data[i].get('People and Society') and data[i].get('Government'):
                if data[i]['People and Society'].get('Education expenditures') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
            
                        crit.append(data[i]['People and Society']['Education expenditures']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        
        elif critere==10:
             if data[i].get('Military and Security') and data[i].get('Government'):
                if data[i]['Military and Security'].get('Military expenditures') and data[i]['Government'].get('Country name'):
                    if data[i]['Government']['Country name'].get('conventional short form'):
            
                        crit.append(data[i]['Military and Security']['Military expenditures']['text']) 
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
        

           

    #Diagramme en barre du critère
    plt.bar(pays,crit)
    plt.show()
    
    #Boxplot des tranches d'âges
    plt.boxplot([TR1,TR2,TR3,TR4,TR5])
    plt.show()
        
