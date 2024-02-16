import sqlite3
import pandas as pd


# Se connecter à une base de données SQL vide
# SQLite stocke la BDD dans un simple fichier
filepath = "./Desktop/NSI/TP-3.2/jeu.db"
open(filepath, 'w').close() #crée un fichier vide
conn = sqlite3.connect(filepath)

# Déclaration du curseur c lié à la connection conn
c = conn.cursor()

# Créer une table
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (id INTEGER PRIMARY KEY, date text, trans text, symbol text, qty real, price real)''')

# Insérer une ligne de données
c.execute("INSERT INTO stocks (date, trans, symbol, qty, price) VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Sauvegarde des changements
conn.commit()


# Il est possible de cloturer la connection une fois les changements savegardés

#conn.close()

# Insérer plusieurs lignes
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (?,?,?,?,?)', purchases)
#t = ('IBM',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
c.execute('SELECT * FROM stocks')
print(c.fetchall()) # ou print(c.fetone()) pour afficher une ligne




# méthode SQL Query
df1 = pd.read_sql_query('SELECT * FROM stocks', conn,)
print("En utilisant la méthode read_sql_query \n", df1.head(), "\n")

#Méthode avec un booléen
requete = pd.read_sql_query("SELECT * FROM stocks", conn)
filtre = (requete["price"] >= 50) & (requete["symbol"] == 'IBM')
resultats_filtres = requete.loc[filtre]
print(resultats_filtres)
