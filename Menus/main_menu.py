from pyfiglet import Figlet
from Menus.menu_ouvert import Ouvert
from FonctionBD import clear

class Main_menu: 
    def __init__(self): 
        pass
    
    def Bienvenue(self):
        clear()
        welcome = Figlet(font='big')
        print(welcome.renderText('Bienvenue'))
        input("Appuyez sur Entrer pour lancer l'application : ")

    def Banner(self): 
        print("༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ")
        print("\n")

    def Au_revoir(self): 
        print("\n")
        print("༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ")
        print("\n")
        bye = Figlet(font='big')
        print(bye.renderText('Beurre Miel'))

    def new_menu(self, previous_menu):
        vue_actuelle = Ouvert(previous_menu)
        while vue_actuelle:
            vue_actuelle = vue_actuelle.run()
        return vue_actuelle