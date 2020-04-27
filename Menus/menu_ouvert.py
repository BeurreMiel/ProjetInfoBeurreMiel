class Ouvert: #Permet l'ouverture d'un menu
    def __init__(self,content): 
        # content est un dictonnaire contenant les actions possibles du menu actuel
        self.content = content 

    def run(self): 
        print("༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ ༼ つ ಥ_ಥ ༽つ")
        print("\n")
        
        if len(self.content["path"]) != 0:
            chemin = self.content["path"][0]
            if len(self.content["path"]) > 2:
                for section in self.content["path"][2:]:
                    chemin += " -> {}".format(section)
            print("{} : {}\n".format(chemin, self.content["question"]))
        else : print("{}\n".format(self.content["question"]))
        
        # Options et actions possibles 
        options = self.content["options"]
        nb_options = len(options)
        actions = self.content["actions"]
        
        # Affichage des options
        for i, opt in enumerate(options):
            print("[{}] {}".format(i+1, opt))

        print ("Que voulez vous faire ? ")

        while True : 
            choix = input("Choix : ")
            try : 
                choix = int(choix)
            except ValueError : 
                print("Le choix doit être un entier.")
                continue

            if choix < 1 or choix > nb_options : 
                print(" La valeur doit être comprise entre 1 et {}.".format(nb_options))
                continue 
            break
        return actions[choix-1](self.content)
