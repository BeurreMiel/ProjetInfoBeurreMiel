from Menus.menu_ouvert import Ouvert
from Acteurs import Individu
from Acteurs import Consultant
from Acteurs import Geographe
from Acteurs import DataScientist
from Acteurs import Admin

def connexion(previous_menu): 
    menu_act = previous_menu

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

def menu_graph(previous_menu): 
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Selectionnez le critère"
    menu_act["options"] = ["Superficie", #2
        "Population", #3
        "Croissance démographique", #4
        "Inflation", #5
        "Dette", #6
        "Taux de chômage", #7
        "Taux de dépenses en santé", #8
        "Taux de dépenses en éducation", #9
        "Taux de dépenses militaires", #10
        "Retour au menu précédent", 
        "Quitter l'application"]
    menu_act["actions"] = [
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,2)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,3)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,4)), # 
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,5)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,6)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,7)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,8)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,9)),
            (lambda previous_menu :previous_menu["individu"].representationgraphique(previous_menu,10)),
            (lambda previous_menu : Ouvert(menu[0])),
            Individu().quitter]
    menu_act["path"] = []
    
    return(Ouvert(menu_act))

def menu_resume(previous_menu): 
    menu_act = {}
    menu_act["individu"] = menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Selectionnez le critère"
    menu_act["options"] = ["Superficie", #2
        "Population", #3
        "Croissance démographique", #4
        "Inflation", #5
        "Dette", #6
        "Taux de chômage", #7
        "Taux de dépenses en santé", #8
        "Taux de dépenses en éducation", #9
        "Taux de dépenses militaires", #10
        "Retour au menu précédent", 
        "Quitter l'application"]
    menu_act["actions"] = [
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,2)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,3)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,4)), # 
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,5)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,6)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,7)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,8)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,9)),
            (lambda previous_menu :previous_menu["individu"].resume(previous_menu,10)),
            (lambda previous_menu : Ouvert(menu[0])),
            Individu().quitter]
    menu_act["path"] = []
    
    return(Ouvert(menu_act))


menu = [
    # Menu de selection du type d'utilisateur 
    { 
        "question" : "Selectionner votre type utilisateur",
        "options" : ["Consultant", "Géographe", "DataScientist", "Administrateur", "Quitter l'application"],
        "actions" : [
            (lambda previous_menu :indices_actions(Consultant(),[1,4,8,9])),
            (lambda previous_menu :indices_actions(Geographe(),[0,1,5,6,8,9])),
            (lambda previous_menu :indices_actions(DataScientist(),[0,1,2,3,4,8,9])),
            (lambda previous_menu :indices_actions(Admin(),[0,1,2,3,5,6,7,8,9])),
            Individu().quitter],
        "individu": Individu(),
        "path": []
    },

    # Menu de selection de l'action

    {
        "question" : "Que voulez vous faire ? ",
        "options" : ["Connexion", #0
        "Affichage de données pays", #1
        "Représentation graphique", #2 Data
        "Résumés statistiques", #3 Data
        "Proposition suggestion", #4
        "Gestion des pays", #5
        "Gestion des suggestions", #6
        "Gestion des comptes", #7
        "Retour au menu précédent", #8
        "Quitter l'application"],#9
        "actions" : [connexion,
            (lambda previous_menu :previous_menu["individu"].affichage(previous_menu)),
            menu_graph,
            menu_resume, # à faire 
            (lambda previous_menu :previous_menu["individu"].ajout_suggestion(previous_menu)),
            (lambda previous_menu :previous_menu["individu"].ajout_pays(previous_menu)),
            (lambda previous_menu :previous_menu["individu"].gestion_suggestion(previous_menu)),
            (lambda previous_menu :previous_menu["individu"].gestion_comptes(previous_menu)),
            (lambda previous_menu : Ouvert(menu[0])),
            Individu().quitter],
        "individu": Individu(),
        "path": []
    }]