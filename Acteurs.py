""" Module des acteurs de l'applications 
"""

import json
import numpy
import matplotlib.pyplot as plt
import FonctionBD as fbd
from Menus.menu_ouvert import Ouvert
from Menus.menu_ferme import Ferme
import getpass

class Individu:     
    def __init__(self):
        self.type="individu"
        self.previous_menu_ini = {}
    # Permet à tout individu de quitter 
    def quitter(self,previous_menu): 
        """ Fonction permettant de quitter l'application

        Arguments:
            previous_menu {list} -- menu précédent l'appel de la fonction

        Returns:
            Ouvert(previous_menu) -- Renvoie le menu précédent
            Ferme() -- Quitte l'application
        """        
        print("{:^63}\n".format("\nVoulez vous quitter cette application ? (Y/N)"))
        check = input("Choix : ")
        if check in ["Y","y"] : 
            return Ferme()
        else : 
            return Ouvert(previous_menu)
    def suppression(self,previous_menu): #Pour éviter les erreurs
        if not self.type == "Administrateur": 
            print ("Vous n'êtes pas Administrateur \n Accès refusé")
            input( "Appuyez sur Entrer pour continuer ")
            return(Ouvert(previous_menu))

    def affichage(self,previous_menu):
        """ Affichage d'un pays 

        Arguments:
            previous_menu {list} -- Menu précédent l'appel de la fonction
            nom_ou_code_pays {string} -- Nom ou code du pays à afficher
        Returns:
            [Ouvert(previous_menu)] -- [Renvoie le menu précédent]
            
        """    
        # Chargement de la base de données 
        nom_ou_code_pays = input("Entrez le nom ou le code du pays : ")
        filename="DataTreatment/country.json"
        with open(filename) as json_file:
            data = json.load(json_file)
         
        try : 
            nom_ou_code_pays = int(nom_ou_code_pays)
        except : nom_ou_code_pays = fbd.get_code(nom_ou_code_pays)

        print("Code du pays sélectionné : ",nom_ou_code_pays,"\n")
        nom_ou_code_pays = int(nom_ou_code_pays)
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
    
        res = numpy.array([['Nom du pays', inf1],
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
        print(res)
        input("Affichage terminé, appuyez sur Entrer pour continuer. ")
        return(Ouvert(previous_menu))
# Classe consultant 
class Consultant(Individu):
    def __init__(self):
        self.type="Consultant"
        
    def ajout_suggestion(self,previous_menu): 
        """ Ajout de suggestions

        Arguments:
            previous_menu {list} -- Menu précédent l'appel de la fonction
        Returns:
            [Ouvert(previous_menu)] -- [Renvoie le menu précédent]
            
        """    
        
        liste_info = []
        Nom = input("Entrer le nom du pays de la suggestion : ") 
        liste_info.append(Nom)
        superficie = input('Entrez la superficie du pays en km2 totale, tapez None pour passer la question :')
        liste_info.append(superficie)
        superficie2 = input('Entrez la superficie du pays en km2 métropolitaine, tapez None pour passer la question :')
        liste_info.append(superficie2)
        pop = input('Entrez la population du pays, tapez None pour passer la question :')
        liste_info.append(pop)
        crois = input('Entrez la croissance demographique du pays en pourcentage , tapez None pour passer la question :')
        liste_info.append(crois)
        inflation = input('Entrez l\'inflation du pays en pourcentage pour l\'année 2016, tapez None pour passer la question :')
        liste_info.append(inflation)
        inflation2 = input('Entrez l\'inflation du pays en pourcentage pour l\'année 2015, tapez None pour passer la question :')
        liste_info.append(inflation2)
        dette = input('Entrez la dette en dollars - unité incluse (trillion, billion...) - pour l\'année 2016, tapez None pour passer la question :')
        liste_info.append(dette)
        dette2 = input('Entrez la dette en dollars - unité incluse (trillion, billion...) - pour l\'année 2016, tapez None pour passer la question :')
        liste_info.append(dette2)
        chom = input('Entrez la taux de chomage du pays en pourcentage pour l\'année 2015, tapez None pour passer la question :')
        liste_info.append(chom)
        chom2 = input('Entrez la taux de chomage du pays en pourcentage pour l\'année 2016, tapez None pour passer la question :')
        liste_info.append(chom2)
        sante = input('Entrez le taux de depense en sante du pays en pourcentage pour l\'année 2014, tapez None pour passer la question :')
        liste_info.append(sante)
        edu = input('Entrez le taux de depense en education du pays en pourcentage pour l\'année 2013, tapez None pour passer la question :')
        liste_info.append(edu)
        army = input('Entrez le taux de depense militaire du pays en pourcentage pour 2014, tapez None pour passer la question :')
        liste_info.append(army)
        army2 = input('Entrez le taux de depense militaire du pays en pourcentage pour 2013, tapez None pour passer la question :')
        liste_info.append(army2)
        army3 = input('Entrez le taux de depense militaire du pays en pourcentage pour 2012, tapez None pour passer la question :')
        liste_info.append(army3)

        # Entree des 5 classes d\'age
        age1 = input('Entrez le pourcentage de la classe [0-14] ans total, tapez None pour passer la question :')
        liste_info.append(age1)
        age1_1 = input('Entrez le pourcentage de la classe [0-14] ans masculin, tapez None pour passer la question :')
        liste_info.append(age1_1)
        age1_2 = input('Entrez le pourcentage de la classe [0-14] ans feminin, tapez None pour passer la question :')
        liste_info.append(age1_2)

        age2 = input('Entrez le pourcentage de la classe [0-14] ans total, tapez None pour passer la question :')
        liste_info.append(age2)
        age2_1 = input('Entrez le pourcentage de la classe [0-14] ans masculin, tapez None pour passer la question :')
        liste_info.append(age2_1)
        age2_2 = input('Entrez le pourcentage de la classe [0-14] ans feminin, tapez None pour passer la question :')
        liste_info.append(age2_2)

        age3 = input('Entrez le pourcentage de la classe [25-54] ans total, tapez None pour passer la question :')
        liste_info.append(age3)
        age3_1 = input('Entrez le pourcentage de la classe [25-54] ans masculin, tapez None pour passer la question :')
        liste_info.append(age3_1)
        age3_2 = input('Entrez le pourcentage de la classe [25-54] ans feminin, tapez None pour passer la question :')
        liste_info.append(age3_2)

        age4 = input('Entrez le pourcentage de la classe [55-64] ans total, tapez None pour passer la question :')
        liste_info.append(age4)
        age4_1 = input('Entrez le pourcentage de la classe [55-64] ans masculin, tapez None pour passer la question :')
        liste_info.append(age4_1)
        age4_2 = input('Entrez le pourcentage de la classe [55-64] ans feminin, tapez None pour passer la question :')
        liste_info.append(age4_2)

        age5 = input('Entrez le pourcentage de la classe [65 ans et plus] total, tapez None pour passer la question :')
        liste_info.append(age5)
        age5_1 = input('Entrez le pourcentage de la classe [65 ans et plus] masculin, tapez None pour passer la question :')
        liste_info.append(age5_1)
        age5_2 = input('Entrez le pourcentage de la classe [65 ans et plus] feminin, tapez None pour passer la question :')
        liste_info.append(age5_2)

        # Ajout de la suggestion dans la base de données
        with open("Suggestions.json") as json_file: 
            sugges =json.load(json_file)
        sugges.append(liste_info)
        with open("Suggestions.json", "w") as write_file:
            json.dump(sugges, write_file)

        print("Votre proposition a bien été enregistrée")
        input("Appuyez sur Entrer pour continuer")

        return(Ouvert(previous_menu))
# Classe géographe
class Geographe(Individu): 
    def __init__(self):
        self.connecte = False
        self.type = "Geographe"
    
    def connexion(self): 
        with open("DataTreatment/user.json") as json_file:
            users = json.load(json_file)

        lcomptes = fbd.account_list(users)
        lmdp = fbd.password_list(users)
        ltype = fbd.type_liste(users)

        pseudo = input("Veuillez entrer votre nom d'utilisateur : ")
        mdp = getpass.getpass("Veuillez entrer votre mot de passe : ")

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

    def ajout_pays(self,previous): 
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            input( "Appuyez sur Entrer pour continuer")
            return(Ouvert(previous))

        filename="DataTreatment/country.json"
        with open(filename) as json_file:
            data = json.load(json_file)

        nouveau_pays = True
        
        while True : 
            Nom = input("Entrer le nom du pays a ajouter : ") 
            #on suppose dans un premier temps que l'user rentre quelque chose 
            if Nom != 'none':
                break
        
        try : #tente de trouver le code du pays
            code = get_code(Nom)
            nouveau_pays = False 
            print("Le pays ",Nom," va être modifié")
        except: 
            print("Le pays entré n'existe pas, un nouveau pays va être crée")
        finally :
            # La fonction demande à l'utilisateur s'il souhaite ajouter des informations
            complementaire = input('Voulez vous ajouter des informations ? (Y/N)')
            liste_info = []
            # Si l'utilisateur accepte 
            if complementaire in ["Y","y"]: 
                superficie = input('Entrez la superficie du pays en km2 totale, tapez None pour passer la question :')
                liste_info.append(superficie)
                superficie2 = input('Entrez la superficie du pays en km2 métropolitaine, tapez None pour passer la question :')
                liste_info.append(superficie2)
                pop = input('Entrez la population du pays, tapez None pour passer la question :')
                liste_info.append(pop)
                crois = input('Entrez la croissance demographique du pays en pourcentage , tapez None pour passer la question :')
                liste_info.append(crois)
                inflation = input('Entrez l\'inflation du pays en pourcentage pour l\'année 2016, tapez None pour passer la question :')
                liste_info.append(inflation)
                inflation2 = input('Entrez l\'inflation du pays en pourcentage pour l\'année 2015, tapez None pour passer la question :')
                liste_info.append(inflation2)
                dette = input('Entrez la dette en dollars - unité incluse (trillion, billion...) - pour l\'année 2016, tapez None pour passer la question :')
                liste_info.append(dette)
                dette2 = input('Entrez la dette en dollars - unité incluse (trillion, billion...) - pour l\'année 2016, tapez None pour passer la question :')
                liste_info.append(dette2)
                chom = input('Entrez la taux de chomage du pays en pourcentage pour l\'année 2015, tapez None pour passer la question :')
                liste_info.append(chom)
                chom2 = input('Entrez la taux de chomage du pays en pourcentage pour l\'année 2016, tapez None pour passer la question :')
                liste_info.append(chom2)
                sante = input('Entrez le taux de depense en sante du pays en pourcentage pour l\'année 2014, tapez None pour passer la question :')
                liste_info.append(sante)
                edu = input('Entrez le taux de depense en education du pays en pourcentage pour l\'année 2013, tapez None pour passer la question :')
                liste_info.append(edu)
                army = input('Entrez le taux de depense militaire du pays en pourcentage pour 2014, tapez None pour passer la question :')
                liste_info.append(army)
                army2 = input('Entrez le taux de depense militaire du pays en pourcentage pour 2013, tapez None pour passer la question :')
                liste_info.append(army2)
                army3 = input('Entrez le taux de depense militaire du pays en pourcentage pour 2012, tapez None pour passer la question :')
                liste_info.append(army3)

                # Entree des 5 classes d\'age
                age1 = input('Entrez le pourcentage de la classe [0-14] ans total, tapez None pour passer la question :')
                liste_info.append(age1)
                age1_1 = input('Entrez le pourcentage de la classe [0-14] ans masculin, tapez None pour passer la question :')
                liste_info.append(age1_1)
                age1_2 = input('Entrez le pourcentage de la classe [0-14] ans feminin, tapez None pour passer la question :')
                liste_info.append(age1_2)

                age2 = input('Entrez le pourcentage de la classe [0-14] ans total, tapez None pour passer la question :')
                liste_info.append(age2)
                age2_1 = input('Entrez le pourcentage de la classe [0-14] ans masculin, tapez None pour passer la question :')
                liste_info.append(age2_1)
                age2_2 = input('Entrez le pourcentage de la classe [0-14] ans feminin, tapez None pour passer la question :')
                liste_info.append(age2_2)

                age3 = input('Entrez le pourcentage de la classe [25-54] ans total, tapez None pour passer la question :')
                liste_info.append(age3)
                age3_1 = input('Entrez le pourcentage de la classe [25-54] ans masculin, tapez None pour passer la question :')
                liste_info.append(age3_1)
                age3_2 = input('Entrez le pourcentage de la classe [25-54] ans feminin, tapez None pour passer la question :')
                liste_info.append(age3_2)

                age4 = input('Entrez le pourcentage de la classe [55-64] ans total, tapez None pour passer la question :')
                liste_info.append(age4)
                age4_1 = input('Entrez le pourcentage de la classe [55-64] ans masculin, tapez None pour passer la question :')
                liste_info.append(age4_1)
                age4_2 = input('Entrez le pourcentage de la classe [55-64] ans feminin, tapez None pour passer la question :')
                liste_info.append(age4_2)

                age5 = input('Entrez le pourcentage de la classe [65 ans et plus] total, tapez None pour passer la question :')
                liste_info.append(age5)
                age5_1 = input('Entrez le pourcentage de la classe [65 ans et plus] masculin, tapez None pour passer la question :')
                liste_info.append(age5_1)
                age5_2 = input('Entrez le pourcentage de la classe [65 ans et plus] feminin, tapez None pour passer la question :')
                liste_info.append(age5_2)

            # Creation de l'entree
            entree = fbd.pays_vide()
            entree['Government']['Country name']['conventional short form']['text'] = Nom
            print("Votre pays a bien ete cree")
            if len(liste_info) >0 : 
                if liste_info[0] not in ['None','none']: 
                    entree['Geography']['Area']['total']['text'] = str(liste_info[0])+"sq km; "+str(liste_info[1])+" sq km (metropolitan "+ Nom +")"
                if liste_info[1] not in ['None','none']: 
                    entree['People and Society']['Population']['text'] = liste_info[2]
                if liste_info[2] not in ['None','none']: 
                    entree['People and Society']['Population growth rate']['text'] = str(liste_info[3])+"% (2016 est.)"
                if liste_info[3] not in ['None','none']: 
                    entree['Economy']['Inflation rate (consumer prices)']['text'] = str(liste_info[4])+"% (2016 est.) ++ "+str(liste_info[5])+"% (2015 est.)"
                if liste_info[4] not in ['None','none']: 
                    entree['Economy']['Debt - external']['text'] = "$"+str(liste_info[6])+"% (31 March 2016 est.) ++ $"+str(liste_info[7])+"% (31 March 2015 est.)"
                if liste_info[5] not in ['None','none']: 
                    entree['Economy']['Unemployment rate']['text'] = str(liste_info[8])+"% (2016 est.) ++ "+str(liste_info[9])+"% (2015 est.)"
                if liste_info[6] not in ['None','none']: 
                    entree['People and Society']['Health expenditures']['text'] = str(liste_info[10])+ "% of GDP (2014)"
                if liste_info[7] not in ['None','none']: 
                    entree['People and Society']['Education expenditures']['text'] = str(liste_info[11])+ "% of GDP (2013)"
                if liste_info[8] not in ['None','none']: 
                    entree['Military and Security']['Military expenditures']['text'] = str(liste_info[12])+"% of GDP (2014) ++ "+str(liste_info[12])+"% of GDP (2013) ++ "+str(liste_info[13])+"% of GDP (2012)"
                if liste_info[9] not in ['None','none']: 
                    entree['People and Society']['Age structure']['0-14 years']['text'] = str(liste_info[14])+"% (male "+str(liste_info[15])+"% / female "+str(liste_info[16])+")"
                if liste_info[10] not in ['None','none']: 
                    entree['People and Society']['Age structure']['15-24 years']['text'] = str(liste_info[17])+"% (male "+str(liste_info[18])+"% / female "+str(liste_info[19])+")"
                if liste_info[11] not in ['None','none']: 
                    entree['People and Society']['Age structure']['25-54 years']['text'] = str(liste_info[10])+"% (male "+str(liste_info[21])+"% / female "+str(liste_info[22])+")"
                if liste_info[12] not in ['None','none']: 
                    entree['People and Society']['Age structure']['55-64 years']['text'] = str(liste_info[23])+"% (male "+str(liste_info[24])+"% / female "+str(liste_info[25])+")"
                if liste_info[13] not in ['None','none']: 
                    entree['People and Society']['Age structure']['65 years and over']['text'] = str(liste_info[26])+"% (male "+str(liste_info[27])+"% / female "+str(liste_info[28])+")"
                print('Vos informations complementaires ont bien ete enregistrees')
            with open("DataTreatment/country.json") as json_file: 
                data =json.load(json_file)
            if nouveau_pays : 
                data.append(entree)
            else :
                data[code]= entree 
            with open("DataTreatment/country.json", "w") as write_file:
                json.dump(data, write_file)

        print("Votre ajout a bien été enregistrée")

        return(Ouvert(previous))

    def gestion_suggestion(self,previous):
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            input( "Appuyez sur Entrer pour continuer")
            return(Ouvert(previous))

        with open("Suggestions.json") as json_file: 
            sugges =json.load(json_file)

        
        with open("DataTreatment/country.json") as json_file:
            data = json.load(json_file)

        n = len(sugges)
        while n > 0 :
            liste_info= sugges[0]
            nom_pays = liste_info.pop(0) # Recupere le nom du pays pour le placer correctement
            print("#####################################################")
            print("Voici la suggestion : ") 
            print("Nom du pays : ", nom_pays)
            print("Superficie du pays : ", str(liste_info[0])+"sq km; "+str(liste_info[1])+" sq km (metropolitan "+ nom_pays +")")
            print("Population du pays : ", liste_info[2])
            print("Croissance démographique du pays : ", str(liste_info[3])+"% (2016 est.)")
            print("Inflation du pays : ", str(liste_info[4])+"% (2016 est.) ++ "+str(liste_info[5])+"% (2015 est.)")
            print("Dette du pays : ", "$"+str(liste_info[6])+"% (31 March 2016 est.) ++ $"+str(liste_info[7])+"% (31 March 2015 est.)")
            print("Taux de chômage du pays : ", str(liste_info[8])+"% (2016 est.) ++ "+str(liste_info[9])+"% (2015 est.)")
            print("Depense santé du pays : ", str(liste_info[10])+ "% of GDP (2014)")
            print("Depense education du pays : ", str(liste_info[11])+ "% of GDP (2013)")
            print("Depense militaire du pays : ",str(liste_info[12])+"% of GDP (2014) ++ "+str(liste_info[12])+"% of GDP (2013) ++ "+str(liste_info[13])+"% of GDP (2012)")
            print("Taux [0 - 14] ans  : ", str(liste_info[14])+"% (male "+str(liste_info[15])+"% / female "+str(liste_info[16])+")")
            print("Taux [15 - 24] ans : ", str(liste_info[17])+"% (male "+str(liste_info[18])+"% / female "+str(liste_info[19])+")")
            print("Taux [25 - 54] ans : ", str(liste_info[10])+"% (male "+str(liste_info[21])+"% / female "+str(liste_info[22])+")")
            print("Taux [55 - 64] ans : ", str(liste_info[23])+"% (male "+str(liste_info[24])+"% / female "+str(liste_info[25])+")")
            print("Taux [65 ans et plus] ", sugges[0][14])
            print("#####################################################")
            while True : 
                res = input("Vous pouvez accepter (A) ou rejeter (R) cette suggestion : ")
                if res in ["A","a","R","r"]: 
                    break 
            
            if res in ["A","a"] : # Si l'admin accepte la suggestion 
                
                
                print ("Le pays ",nom_pays, "va être modifié :")
                nom_pays = fbd.get_code(nom_pays)
                # Test de présence du pays
                if len(liste_info) >0 : 
                    if liste_info[0] not in ['None','none']: 
                        data[nom_pays]['Geography']['Area']['total']['text'] = str(liste_info[0])+"sq km; "+str(liste_info[1])+" sq km (metropolitan "+ nom_pays +")"
                    if liste_info[1] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Population']['text'] = liste_info[2]
                    if liste_info[2] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Population growth rate']['text'] = str(liste_info[3])+"% (2016 est.)"
                    if liste_info[3] not in ['None','none']: 
                        data[nom_pays]['Economy']['Inflation rate (consumer prices)']['text'] = str(liste_info[4])+"% (2016 est.) ++ "+str(liste_info[5])+"% (2015 est.)"
                    if liste_info[4] not in ['None','none']: 
                        data[nom_pays]['Economy']['Debt - external']['text'] = "$"+str(liste_info[6])+"% (31 March 2016 est.) ++ $"+str(liste_info[7])+"% (31 March 2015 est.)"
                    if liste_info[5] not in ['None','none']: 
                        data[nom_pays]['Economy']['Unemployment rate']['text'] = str(liste_info[8])+"% (2016 est.) ++ "+str(liste_info[9])+"% (2015 est.)"
                    if liste_info[6] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Health expenditures']['text'] = str(liste_info[10])+ "% of GDP (2014)"
                    if liste_info[7] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Education expenditures']['text'] = str(liste_info[11])+ "% of GDP (2013)"
                    if liste_info[8] not in ['None','none']: 
                        data[nom_pays]['Military and Security']['Military expenditures']['text'] = str(liste_info[12])+"% of GDP (2014) ++ "+str(liste_info[12])+"% of GDP (2013) ++ "+str(liste_info[13])+"% of GDP (2012)"
                    if liste_info[9] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Age structure']['0-14 years']['text'] = str(liste_info[14])+"% (male "+str(liste_info[15])+"% / female "+str(liste_info[16])+")"
                    if liste_info[10] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Age structure']['15-24 years']['text'] = str(liste_info[17])+"% (male "+str(liste_info[18])+"% / female "+str(liste_info[19])+")"
                    if liste_info[11] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Age structure']['25-54 years']['text'] = str(liste_info[10])+"% (male "+str(liste_info[21])+"% / female "+str(liste_info[22])+")"
                    if liste_info[12] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Age structure']['55-64 years']['text'] = str(liste_info[23])+"% (male "+str(liste_info[24])+"% / female "+str(liste_info[25])+")"
                    if liste_info[13] not in ['None','none']: 
                        data[nom_pays]['People and Society']['Age structure']['65 years and over']['text'] = str(liste_info[26])+"% (male "+str(liste_info[27])+"% / female "+str(liste_info[28])+")"
                    print('Vos informations complementaires ont bien ete enregistrees : ')

            
            # Si la suggestion est refusée ou quand la modification a ete enregistree 
            del sugges[0]
            n= len(sugges) # On supprime le premier element de la liste de selection 
        
        print("La liste de suggestion est vide")

        with open("Suggestions.json", "w") as write_file:
            json.dump(sugges, write_file)
        input("Appuyez sur Entrer pour continuer ")

        return(Ouvert(previous))

# Classe Data Scientist

class DataScientist(Consultant): 
    def __init__(self):
        self.connecte = False
        self.type = "DataScientist"
    
    def connexion(self): 
        with open("DataTreatment/user.json") as json_file:
            users = json.load(json_file)

        lcomptes = fbd.account_list(users)
        lmdp = fbd.password_list(users)
        ltype = fbd.type_liste(users)

        pseudo = input("Veuillez entrer votre nom d'utilisateur : ")
        mdp = getpass.getpass("Veuillez entrer votre mot de passe : ")

        for i in range(len(lcomptes)): 
            if (self.type == ltype[i] and mdp == lmdp[i] and pseudo == lcomptes[i]): 
                self.connecte = True 
                print("Vous êtes connecté !")
                input("Appuyez sur Entrer pour continuer : ")
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

    def representationgraphique(self,previous_menu,critere):
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            input( "Appuyez sur Entrer pour continuer")
            return(Ouvert(previous_menu))
        
        filename="DataTreatment/country.json"
        with open(filename) as json_file:
            data = json.load(json_file)     
            
        tranche1=[]
        tranche2=[]
        tranche3=[]
        tranche4=[]
        tranche5=[]
        crit=[]
        pays=[]    

            

        
        #Erreurs
        if critere<2 or critere>10 :
            print('Critère inexistant')
            return(Ouvert(previous_menu))


        #Séparation des tranches d'âges
        for j in range (len(data)):

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
        
            if critere==1:
                    for i in range (len(data)):
                        crit.append(data[i]['Geography']['Area']['total']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==2:
                    for i in range (len(data)):
                        crit.append(data[i]['People and Society']['Population']['text'])
                        pays.append(data[i]['Government']['Country name']['conventional short form']['text'])        
                
            elif critere==3:
               for i in range (len(data)):
                   crit.append(data[i]['People and Society']['Population growth rate']['text'])
                   pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==4:
                for i in range (len(data)):
                    crit.append(data[i]['Economy']['Inflation rate (consumer prices)']['text'])
                    pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==5:
                for i in range (len(data)):
                    crit.append(data[i]['Economy']['Debt - external']['text'])
                    pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==6:
                for i in range (len(data)):
                    crit.append(data[i]['Economy']['Unemployment rate']['text'])
                    pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==7:
                for i in range (len(data)):
                    crit.append(data[i]['People and Society']['Health expenditures']['text'])
                    pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==8:
               for i in range (len(data)):
                   crit.append(data[i]['People and Society']['Education expenditures']['text'])
                   pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            elif critere==9:
               for i in range (len(data)):
                   crit.append(data[i]['Military and Security']['Military expenditures']['text']) 
                   pays.append(data[i]['Government']['Country name']['conventional short form']['text'])
            
            #Diagramme en barre du critère
            plt.bar(pays,crit)
            plt.title("Diagramme en barre du critère") 
            plt.show()
            
            #Boxplot des tranches d'âges
            plt.boxplot([TR1,TR2,TR3,TR4,TR5])
            plt.title("Boxplot par tranche d'âge du critère") 
            plt.show()
            
            input("Appuyez sur Entrer pour continuer")
            return(Ouvert(previous_menu))

# Classe administrateur
class Admin(Geographe, DataScientist):
    
    def __init__(self):
        self.connecte = False
        self.type = "Administrateur"
    
    def connexion(self): 
        with open("DataTreatment/user.json") as json_file:
            users = json.load(json_file)
        lcomptes = fbd.account_list(users)
        lmdp = fbd.password_list(users)
        ltype = fbd.type_liste(users)

        pseudo = input("Veuillez entrer votre nom d'utilisateur : ")
        mdp = getpass.getpass("Veuillez entrer votre mot de passe : ")

        for i in range(len(lcomptes)): 
            if (self.type == ltype[i] and mdp == lmdp[i] and pseudo == lcomptes[i]): 
                self.connecte = True 
                print("Vous êtes connecté !")
                input("Appuyez sur Entrer pour continuer : ")
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
        
    def suppression(self,previous_menu):
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            input( "Appuyez sur Entrer pour continuer ")
            return(Ouvert(previous_menu))
        elif not self.type == "Administrateur": 
            print ("Vous n'êtes pas Administrateur \n Accès refusé")
            input( "Appuyez sur Entrer pour continuer ")
            return(Ouvert(previous_menu))

        filename="DataTreatment/country.json"
        with open(filename) as json_file:
            data = json.load(json_file)

        nom_ou_code_pays = input("Entrez le nom ou le code du pays : ")

        try : 
            nom_ou_code_pays = int(nom_ou_code_pays)
        except : 
            nom_ou_code_pays = fbd.get_code(nom_ou_code_pays)

        del data[nom_ou_code_pays]
        with open("DataTreatment/country.json", "w") as write_file:
            json.dump(data, write_file)

        print("Votre suppression a bien été enregistrée")
        input("Appuyez sur Entrer pour continuer. ")
        return(Ouvert(previous_menu))



    def ajout_compte(self): 
        with open("DataTreatment/user.json") as json_file:
            users = json.load(json_file)

        new = {}
        while True : 
            type_user = input("Entrez le type d'utilisateur que vous souhaitez creer : (Geographe/DataScientist) ")
            if type_user in ["Geographe","DataScientist"] : #teste si c'est bien le bon type 
                break
        new['type'] = type_user
        new['ID'] = {}
        id_user = input("Entrez l'ID utilisateur que vous souhaitez creer : ")
        new['ID']['username'] = id_user
        mdp_user = input("Entrez le mot de passe utilisateur que vous souhaitez creer : ")
        mdp_confirmation = input("Confirmez votre mot de passe : ")
        while mdp_user != mdp_confirmation : 
            mdp_confirmation = input("Les deux mots de passe ne correspondent pas, veuiller reessayer : ")
        new['ID']['mdp'] = mdp_user
        
    
        print("L'utilisateur",id_user,"vient d'etre cree et va etre ajouter a la base")
        users.append(new)
        with open("DataTreatment/user.json", "w") as write_file:
            json.dump(users, write_file)


    def suppression_compte(self): 
        with open("DataTreatment/DataTreatment/user.json") as json_file:
            users = json.load(json_file)

        liste = fbd.account_list(users)
        print("Liste des comptes disponibles : ", liste)
        nom = input("Veuillez donner le nom du compte a supprimer : ")
        if nom in liste : 
            numero = liste.index(nom)
            del users[numero]
        else : 
            print("Aucun changement effectué")
        with open("DataTreatment/user.json", "w") as write_file:
            json.dump(users, write_file)

    def  gestion_comptes(self,previous_menu): 
        if not self.connecte : 
            print ("Vous n'êtes pas connecté \n Veuillez vous connecter")
            input("\n""Appuyez sur Entrer pour continuer ")
            return(Ouvert(previous_menu))
        print("#### Gestion des comptes ####")
        choix = input("Voulez vous ajouter ou supprimer un compte ? : (A/S) ")
        if choix in ["a", "A"]: 
            self.ajout_compte()
            return(Ouvert(previous_menu)) # à finir
        elif  choix in ["s", "S"]: 
            self.suppression_compte()
            return(Ouvert(previous_menu)) # à finir
        else :
            print("Aucun changement effectué")
            input("Appuyez sur Entrer pour continuer ")
            return(Ouvert(previous_menu))