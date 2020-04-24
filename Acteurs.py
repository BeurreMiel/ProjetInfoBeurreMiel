from Data import *
import numpy
from FonctionBD import account_list
from FonctionBD import password_list
from FonctionBD import type_liste
from FonctionBD import get_code
from FonctionBD import is_number

class Individu:     
    def __init__(self):
        self.acteur="individu"
            
    def affichage(self,nom_ou_code_pays):

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

# Classe géographe
class Geographe(Individu): 
    def __init__(self):
        self.connecte = False
        self.type = "geo"
    
    def connexion(self): 
        lcomptes = account_list(users)
        lmdp = password_list(users)
        ltype = type_liste(users)

        pseudo = input("Veuillez entrer votre nom d'utilisateur : ")
        mdp = input("Veuillez entrer votre mot de passe : ")

        for i in range(len(lcomptes)): 
            if (self.type == ltype[i] and mdp == lmdp[i] and pseudo == lcomptes[i]): 
                self.connecte = True 
                print("Vous êtes connecté !")
                input("Appuyez sur n'importe quelle touche pour continuer : ")
                break
        
        if not self.connecte: 
            print("Échec de la connextion !")
            input("Appuyez sur n'importe quelle touche pour continuer : ")

        return self.connecte
    
    def deconnexion(self): 
        if not self.connecte: 
            print("Vous n'êtes pas connecté : ")
            return("On doit revenir au menu précédent")
        else : 
            confirmation = input("Voulez vous vraiment vous déconnecter ? (Y/N) ")
            if confirmation in ["Y","y"] : 
                self.connecte = False 
                print("Déconnexion réussie")
            else : 
                print ("Déconnextion échouée")
        
        return("On doit revenir au menu précédent")

    def ajout_pays(self): 
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            return("Normalement on doit revenir au menu précédent")

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

        return("Normalement on doit revenir au menu précédent")

    def gestion_suggestion(self):
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            return("Normalement on doit revenir au menu précédent") 
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

