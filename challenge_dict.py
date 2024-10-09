# Comptage de Fréquences
words = ["rabii", "rabii", "yassin", "imade", "yassin", "rabii"]

frequency_dict={

}
def compter_les_noms(liste,dct):
    for i in liste:
        dct[i] = dct.get(i,0)+1
    return dct

frequency_dict = compter_les_noms(words,frequency_dict)
print(frequency_dict)



#Challenge : Mise à Jour de Dictionnaires
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}
def update_dict(dic_updated,dicts2,dicts3):
    dic_updated.update(dicts2)
    dic_updated.update(dicts3)
    return dic_updated

dic_updated = update_dict(dict1,dict2,dict3)
print(dic_updated)





# Conversion de Deux Listes en Dictionnaire


key = ["rabii","yassin","imade"]
value = [22,22,20]

def Create_Dict(ky,vl):
    
    new_dict=dict(zip(ky,vl))
    return new_dict

my_dict=Create_Dict(key,value)
print(my_dict)


#Tri d'un Dictionnaire par Valeur
import random
import string

# Générer un dictionnaire avec des clés aléatoires (lettres) et des valeurs aléatoires (nombres)
random_dict = {random.choice(string.ascii_lowercase): random.randint(1, 100) for _ in range(10)}
print(random_dict)

def dict_pairs(dicts):
    liste_pair_nTrier=[

    ]
    liste_key=[

    ]
    liste_par_Trier = [

    ]

    for key , value in dicts.items():
        if value % 2 == 0:
            liste_pair_nTrier.append(value)
            liste_key.append(key)
    
    for i in range(len(liste_pair_nTrier)):
        max_v = max(liste_pair_nTrier)
        liste_par_Trier.append(max_v)
        liste_pair_nTrier.remove(max_v)

    return Create_Dict(liste_key,liste_par_Trier)


print(dict_pairs(random_dict))

        

# Suppression d'Éléments Basée sur une Condition
def delete_pair_nm(dicts):
    list_key = [

    ]
    for key ,  value in dicts.items():
        if value % 2 == 0:
            list_key.append(key)
            
    for i in list_key:
        del dicts[f"{i}"]

    return dicts


new_dict=delete_pair_nm(random_dict)
print(new_dict)



