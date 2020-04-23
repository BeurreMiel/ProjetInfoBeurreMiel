### Importation des donnees ### 
import json
filename="country.json"
with open(filename) as json_file:
    data = json.load(json_file)

### Importation de la base utilsateur ###

# La base utilisateur a été cree manuellement hors code et sauvegardee sous le format json
with open("user.json") as json_file:
    users = json.load(json_file)

with open("Suggestions.json") as json_file: 
    sugges =json.load(json_file)