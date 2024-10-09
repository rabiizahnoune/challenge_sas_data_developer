import pandas as pd 
import numpy as np
dicts = {
    "A":[1,np.nan,48,3],
    "B":[1,np.nan,48,np.nan]
}
df =pd.DataFrame(dicts)
new_data = df.fillna(df.mean())
print(new_data)


#Filtrage de Données

data = {
    'TransactionID': [1, 2, 3, 4, 5, 6],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Montant': [500, 1500, 2500, 800, 1200, 400],
    'Type': ['Débit', 'Crédit', 'Crédit', 'Débit', 'Crédit', 'Débit']
}

df1=pd.DataFrame(data)

new_df1=df1[df1["Montant"]>1000]
print(new_df1)

#Agrégation de Données
data1 = {
    'VenteID': [1, 2, 3, 4, 5, 6, 7],
    'Region': ['Nord', 'Sud', 'Est', 'Ouest', 'Nord', 'Est', 'Sud'],
    'Montant': [200, 300, 150, 400, 250, 100, 350]
}


df2 = pd.DataFrame(data1)
total_ventes_par_regions = df2.groupby("Region")["Montant"].sum().reset_index()
print(total_ventes_par_regions)




#Fusion de Données
clients_data = {
    'customer_id': [1, 2, 3, 4],
    'nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com']
}

commandes_data = {
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 2, 3, 1],
    'montant': [250, 150, 200, 300, 400]
}

df_clients = pd.DataFrame(clients_data)
df_commandes = pd.DataFrame(commandes_data)

df_fusionne = pd.merge(df_clients,df_commandes,on="customer_id",how="inner")
print(df_fusionne)