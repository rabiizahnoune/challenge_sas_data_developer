import os 
chemin_repertoire = r"C:\Users\Youcode\Desktop\project2\challenge_fichier"
liste_contenue = [

]

for fichier in os.listdir(chemin_repertoire):
    if fichier.endswith(".txt"):
        chemin_fichier = os.path.join(chemin_repertoire,fichier)


        with open(chemin_fichier,"r",encoding='utf-8') as f :
            contenu = f.read()
            with open('ali.txt','w') as r:
                  r.write(contenu)
            
            
chemin_repertoire =  r"C:\Users\Youcode\Desktop\project2\challenge_fichier" 

nom_fichier = 'config.yaml'


chemin_fichier = os.path.join(chemin_repertoire, nom_fichier)


if os.path.exists(chemin_fichier):

    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()
        print("Contenu de", nom_fichier, ":\n", contenu)
else:
    print(nom_fichier, "n'existe pas dans le répertoire", chemin_repertoire)
    





#Challenge : Copie Sélective de Fichiers
import shutil
repertoire_distination = r'C:\Users\Youcode\Desktop\project2\repertoire_distination'

for fichier in os.listdir(chemin_repertoire):
    if fichier.endswith('.txt'):
        chemin_fichier=os.path.join(chemin_repertoire,fichier)
        shutil.copy(chemin_fichier,repertoire_distination)

def create_repetoire(repertoire,list_sous_repetoire):
    os.mkdir(repertoire)
    for i in list_sous_repetoire:
        chemin_repertoire=os.path.join(repertoire,i)
        os.mkdir(chemin_repertoire)


create_repetoire("hello_guys",["imad","yassin"])