import sqlite3
import time
conn = sqlite3.connect("base.db")

def create_database(database):
    cursor = database.cursor()
    while True:
        db_name = input("Nom de la base de donnée: ")
        requests = """CREATE TABLE IF NOT EXISTS {}(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name_matiere TEXT,
        name_prof TEXT,
        moyenne NUMBER)""".format(db_name)
        cursor.execute(requests)
        database.commit()
        wantcontinue = input("Veux-tu créer un autre table SQL ? (Oui/Non)")
        if wantcontinue == "Non":
            break
        else:
            continue
    
def remove_element_table(database):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM SQLITE_MASTER WHERE type='table';")
    everything = cursor.fetchall()
    total = int(len(everything))
    tables = []
    for rows in everything:
        tables.append(rows[2])
        number = int(len(tables))-1
        print(number,")", rows[2])
    choice_table = input("Dans quelle table ajouter ?")
    add = str(tables[int(choice_table)])
    cursor.execute("SELECT * FROM {}".format(add))
    each_element = cursor.fetchall()
    for rows in each_element:
        print("ID: ", rows[0], "/ Matière: ", rows[1], "/ Prof: ", rows[2])
    choice_element = int(input("Quel élément suprimer en tapant son ID ?"))
    cursor.execute("DELETE FROM {} WHERE id = {}".format(add, int(choice_element)))
    database.commit()

def add_element_tables(database):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM SQLITE_MASTER WHERE type='table';")
    everything = cursor.fetchall()
    total = int(len(everything))
    tables = []
    for rows in everything:
        tables.append(rows[2])
        number = int(len(tables))-1
        print(number,")", rows[2])
    choice_table = input("Dans quelle table ajouter ?")
    add = str(tables[int(choice_table)])
    add_name_matiere = input("Nom de la matière: ")
    add_name_prof = input("Nom du prof: ")
    add_moyenne = input("Moyenne dans cette matière: ")
    cursor.execute("""INSERT INTO {}(name_matiere, name_prof, moyenne) VALUES(?,?,?)""".format(add), (add_name_matiere, add_name_prof, add_moyenne))
    database.commit()

def erase_tables(database):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM SQLITE_MASTER WHERE type='table';")
    everything = cursor.fetchall()
    total = int(len(everything))
    tables = []
    for rows in everything:
        tables.append(rows[2])
        number = int(len(tables))-1
        print(number,")", rows[2])
    choice = input("Quelle table suprimer ?")
    erase = str(tables[int(choice)])
    cursor.execute("""DROP TABLE {}""".format(erase))
    database.commit()

def modify_elements(database):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM SQLITE_MASTER WHERE type='table';")
    everything = cursor.fetchall()
    total = int(len(everything))
    tables = []
    for rows in everything:
        tables.append(rows[2])
        number = int(len(tables))-1
        print(number,")", rows[2])
    choice_table = input("Dans quelle table ajouter ?")
    add = str(tables[int(choice_table)])
    cursor.execute("SELECT * FROM {}".format(add))
    each_element = cursor.fetchall()
    for rows in each_element:
        print("ID: ", rows[0], "/ Matière: ", rows[1], "/ Prof: ", rows[2], "/ Moyenne: ", rows)
    choice_element = int(input("Quel élément modifier en tapant son ID ?"))
    new_name_matiere = input("Nouveau nom de la matière: ")
    new_name_prof = input("Nouveau nom du prof: ")
    new_moyenne = input("Nouvelle moyenne: ")
    cursor.execute("UPDATE {} SET name_matiere = ?, name_prof = ?, moyenne = ? WHERE id = ?".format(add), (new_name_matiere, new_name_prof, new_moyenne, choice_element))
    database.commit()



print("Bienvenue sur mon gestionnaire SQL")
time.sleep(1.5)
while True:
    print("Voici les options de l'app:")
    time.sleep(1)
    print("1)Créer une base de donnée")
    time.sleep(1)
    print("2)Ajouter un élément dans une table")
    time.sleep(1)
    print("3)Modifier un élément")
    time.sleep(1)
    print("4)Suprimer un élément")
    time.sleep(1)
    print("5)Suprimer une table")
    time.sleep(1)
    choose = input("Veuillez choisir une option en tapant le chiffre lui correspondant:")
    if choose == "1":
        create_database(conn)
    elif choose == "2":
        add_element_tables(conn)
    elif choose == "3":
        modify_elements(conn)
    elif choose == "4":
        remove_element_table(conn)
    elif choose == "5":
        erase_tables(conn)
    else:
        print("Ce choix n'existe ou vous avez tapé n'importe quoi")