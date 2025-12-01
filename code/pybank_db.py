import sqlite3

with open("pybank.sql","r") as script_file:
    sql_script = script_file.read()

try:
    with sqlite3.connect("pybank.db") as connexion:
        print(f"Database opened successfully with {sqlite3.sqlite_version}.")
        
        #Activating foreign key feature
        connexion.execute('PRAGMA foreign_keys = ON;')

        cursor = connexion.cursor()
        
        #Executing SQLite script
        cursor.executescript(sql_script)
        connexion.commit()
        print("Script implemented successfully.")

        #Debugging
        test = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(test)
        response = cursor.fetchall()
        for r in response:
            print(r[0])

except sqlite3.OperationalError as error:
    print("Not able to open database : ",error)

finally:
    if connexion:
        cursor.close()
        connexion.close()
    print("Database closed successfully.")