### Importation des donnees ### 
import json
filename="Country - Backup - FirstVer.json"
with open(filename) as json_file:
    data = json.load(json_file)
from FonctionBD import pays_vide


### Tentative de suppression des valeurs manquantes ####

def clean_table(data):
    n=len( data)
    data_clean_table=[]
    for i in range(n):
        Intermediate_list=11*[0]
        bool=True
        try:
            Intermediate_list[0]= data[i]['Government']['Country name']['conventional short form']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[1]= data[i]['Geography']['Area']['total']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[2]= data[i]['People and Society']['Population']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[3]= data[i]['People and Society']['Population growth rate']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[4]= data[i]['Economy']['Inflation rate (consumer prices)']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[5]= data[i]['Economy']['Debt - external']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[6]= data[i]['Economy']['Intermediate_listnemployment rate']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[7]= data[i]['People and Society']['Health expenditures']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[8]= data[i]['People and Society']['Education expenditures']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[9]= data[i]['Military and Security']['Military expenditures']['text']
        except KeyError:
            bool=False
        try:
            Intermediate_list[10]= data[i]['People and Society']['Age structure']
        except KeyError:
            bool=False
        if bool==True:
            data_clean_table.append(Intermediate_list)  

    index_NA = [] #indices des pays possédant des valeurs manquantes
    for i in range(len(data_clean_table)):
        S = 0
        for j in range(len(data_clean_table[i])):
            if 'NA' in data_clean_table[i][j]:
                S = 1
        if S == 1:
            index_NA.append(i)        

    liste_pays = []
    for i in range(len(index_NA)):
        liste_pays.append(data_clean_table[index_NA[i]][0])

    for j in range(len(liste_pays)):
        index = -1
        for i in range(len(data_clean_table)):
            if liste_pays[j] == data_clean_table[i][0]:
                index = i
        if index > -1:
            data_clean_table.pop(index)       
    

    data_clean_table = []
    for i in range(len(data_clean_table)): 
        entree = pays_vide()
        entree['Government']['Country name']['conventional short form']['text'] = data_clean_table[i][0]
        entree['Geography']['Area']['total']['text'] = data_clean_table[i][1]
        entree['People and Society']['Population']['text'] = data_clean_table[i][2]
        entree['People and Society']['Population growth rate']['text'] = data_clean_table[i][3]
        entree['Economy']['Inflation rate (consumer prices)']['text'] = data_clean_table[i][4]
        entree['Economy']['Debt - external']['text'] = data_clean_table[i][5]
        entree['Economy']['Unemployment rate']['text'] = data_clean_table[i][6]
        entree['People and Society']['Health expenditures']['text'] = data_clean_table[i][7]
        entree['People and Society']['Education expenditures']['text'] = data_clean_table[i][8]
        entree['Military and Security']['Military expenditures']['text'] = data_clean_table[i][9]
        entree['People and Society']['Age structure'] = data_clean_table[i][10]
        data_clean_table.append(entree)

    return(data_clean_table)

data_clean_table = clean_table(data) 

with open("country.json", "w") as write_file:
    json.dump(data_clean_table, write_file)




