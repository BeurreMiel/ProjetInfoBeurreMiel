from Menus.menu_ouvert import Ouvert
from Acteurs import Individu
from Acteurs import Consultant
from Acteurs import Geographe
from Acteurs import DataScientist
from Acteurs import Admin

def connexion(content): 
    menu_act = content

    if menu_act["individu"].connexion() : #Vérifie si l'acteur peut se connecter et est connecté  
        # On retire à l'utilisateur la possibilité de se co
        del menu_act["options"][0] 
        del menu_act["actions"][0]
    
    return(Ouvert(menu_act))

def indices_actions(ind,indice_taches):
    menu_act = {}
    menu_act["individu"] = ind
    menu_act["question"] = menu[1]["question"]
    menu_act["options"] = [menu[1]["options"][i] for i in indice_taches]
    menu_act["actions"] = [menu[1]["actions"][i] for i in indice_taches]
    menu_act["path"] = []
    return(Ouvert(menu_act))

menu = [
    # Menu de selection du type d'utilisateur 
    { 
        "question" : "Selectionner votre type utilisateur",
        "options" : ["Consultant", "Géographe", "DataScientist", "Administrateur", "Quitter l'application"],
        "actions" : [
            (lambda content :indices_actions(Consultant(),[1,4,8,9])),
            (lambda content :indices_actions(Geographe(),[0,1,5,6,8,9])),
            (lambda content :indices_actions(DataScientist(),[0,1,2,3,4,8,9])),
            (lambda content :indices_actions(Admin(),[0,1,2,3,5,6,7,8,9])),
            Individu().quitter],
        "individu": Individu(),
        "path": []
    },
    # Menu de selection de l'action

    {
        "question" : "Que voulez vous faire ? ",
        "options" : ["Connexion", #0
        "Affichage de données pays", #1
        "Représentation graphique", #2
        "Résumés statistiques", #3
        "Proposition suggestion", #4
        "Gestion des pays", #5
        "Gestion des suggestions", #6
        "Gestion des comptes", #7
        "Retour au menu précédent", #8
        "Quitter l'application"],#9
        "actions" : [
            connexion,
            (lambda content :content["individu"].affichage(content)),
            (lambda content :content["individu"].representationgraphique(content)),
            (lambda content :content["individu"].resume(content)), # à faire 
            (lambda content :content["individu"].ajout_suggestion(content)),
            (lambda content :content["individu"].ajout_pays(content)),
            (lambda content :content["individu"].gestion_suggestion(content)),
            (lambda content :content["individu"].gestion_comptes(content)),
            (lambda content : Ouvert(menu[0])),
            Individu().quitter,
            ],
        "individu": Individu(),
        "path": []
    }
]

