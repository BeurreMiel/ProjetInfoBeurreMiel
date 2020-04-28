### Importation des donnees ### 
import json
filename="Country - Backup - FirstVer.json"
with open(filename) as json_file:
    data = json.load(json_file)
from FonctionBD import pays_vide


### Tentative de suppression des valeurs manquantes ####

def clean_table(data):
    n=len( data)
    L=[]
    for i in range(n):
        U=11*[0]
        bool=True
        try:
            U[0]= data[i]['Government']['Country name']['conventional short form']['text']
        except KeyError:
            bool=False
        try:
            U[1]= data[i]['Geography']['Area']['total']['text']
        except KeyError:
            bool=False
        try:
            U[2]= data[i]['People and Society']['Population']['text']
        except KeyError:
            bool=False
        try:
            U[3]= data[i]['People and Society']['Population growth rate']['text']
        except KeyError:
            bool=False
        try:
            U[4]= data[i]['Economy']['Inflation rate (consumer prices)']['text']
        except KeyError:
            bool=False
        try:
            U[5]= data[i]['Economy']['Debt - external']['text']
        except KeyError:
            bool=False
        try:
            U[6]= data[i]['Economy']['Unemployment rate']['text']
        except KeyError:
            bool=False
        try:
            U[7]= data[i]['People and Society']['Health expenditures']['text']
        except KeyError:
            bool=False
        try:
            U[8]= data[i]['People and Society']['Education expenditures']['text']
        except KeyError:
            bool=False
        try:
            U[9]= data[i]['Military and Security']['Military expenditures']['text']
        except KeyError:
            bool=False
        try:
            U[10]= data[i]['People and Society']['Age structure']
        except KeyError:
            bool=False
        if bool==True:
            L.append(U)  

    T = L

    index_NA = []
    for i in range(len(T)):
        S = 0
        for j in range(len(T[i])):
            if 'NA' in T[i][j]:
                S = 1
        if S == 1:
            index_NA.append(i)        

    liste_pays = []
    for i in range(len(index_NA)):
        liste_pays.append(T[index_NA[i]][0])

    for j in range(len(liste_pays)):
        index = -1
        for i in range(len(T)):
            if liste_pays[j] == T[i][0]:
                index = i
        if index > -1:
            T.pop(index)       
    

    data_clean = []
    for i in range(len(T)): 
        entree = pays_vide()
        entree['Government']['Country name']['conventional short form']['text'] = T[i][0]
        entree['Geography']['Area']['total']['text'] = T[i][1]
        entree['People and Society']['Population']['text'] = T[i][2]
        entree['People and Society']['Population growth rate']['text'] = T[i][3]
        entree['Economy']['Inflation rate (consumer prices)']['text'] = T[i][4]
        entree['Economy']['Debt - external']['text'] = T[i][5]
        entree['Economy']['Unemployment rate']['text'] = T[i][6]
        entree['People and Society']['Health expenditures']['text'] = T[i][7]
        entree['People and Society']['Education expenditures']['text'] = T[i][8]
        entree['Military and Security']['Military expenditures']['text'] = T[i][9]
        entree['People and Society']['Age structure'] = T[i][10]
        data_clean.append(entree)

    return(data_clean)

data_clean = clean_table(data) 

with open("country.json", "w") as write_file:
    json.dump(data_clean, write_file)




