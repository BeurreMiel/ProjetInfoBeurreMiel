from Data import data
from Data import users
import FonctionBD as fbd

fbd.ajout_compte(users)

print("Le dernier compte ajoute est", users[-1])

print("La nouvelle liste des comptes est", users)