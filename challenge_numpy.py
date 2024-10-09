import numpy as np

#Analyse de Températures
temperatures = np.array([22.5, 24.0, 19.8, 21.0, 23.5, 25.2, 20.1, 18.6, 22.0, 24.3])

print(np.mean(temperatures))

print(np.median(temperatures))

print(np.std(temperatures))

# Normalisation de Données
def normaliser(data):
    data_normaliser = (data-np.mean(data)/np.std(data))

    return data_normaliser

print(normaliser(temperatures))
print(np.mean(temperatures))

print(np.median(temperatures))

print(np.std(temperatures))

#Comparaison de Tableaux
arry_1 = np.array([1,2,3,4,5,6,7,8])
arry_2 = np.array([1,10,3,4,9,6,7,0])

def comp_arr( arr1 , arr2 ):
    index = np.where(arr1 != arr2)
    valeur_different_arr1 = arr1[index]
    valeur_different_arr2 = arr2[index]
    return index , valeur_different_arr1 , valeur_different_arr2

index,valeur_different_arr1,valeur_different_arr2 = comp_arr(arry_1,arry_2)
print(index)
print(valeur_different_arr1)
print(valeur_different_arr2)


#Opérations Matricielles#

def operation_arry(arr1,arr2):
    multuplication = np.dot(arr1,arr2)
    transposer_arr1 = arr1.T
    transposer_arr2 = arr2.T
    inverse_arr1 = np.linalg.inv(arr1)
    inverse_arr2 = np.linalg.inv(arr2)
    return multuplication,transposer_arr1,transposer_arr2,inverse_arr1,inverse_arr2




#Sélection Basée sur Conditions

def select_pair_nbr(arr):
    index = np.where(arr % 2 == 0)
    array_pair=arr[index]
    return array_pair

print(select_pair_nbr(np.array([1,2,3,4,5,6,7,8,9,10,11,12])))

