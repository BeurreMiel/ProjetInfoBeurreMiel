class menu_ouvert: 
    def __init__(self,content): 
        # content est un dictonnaire contenant les actions possibles du menu actuel
        self.content = content 

    def run(self): 
        if len(self.content["path"]) != 0:
            chemin = self.content["path"][0]
            if len(self.contenu["path"]) > 2:
                for section in self.contenu["path"][2:]:
                    chemin += " -> {}".format(section)
            print("{} : {}\n".format(chemin, self.contenu["question"]))
        else : print("{}\n".format(self.contenu["question"]))
        
        # Options et actions possibles 
        options = self.content["options"]
        nb_options = len(options)
        actions = self.content["actions"]
        
        # Affichage des options
        for i, opt in enumerate(options):
            print("[{}] {}".format(i+1, opt))