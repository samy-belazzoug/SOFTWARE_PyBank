import sqlite3
import json

def init_database(db_path="pybank.db"):
    """Initialize the database with tables from SQL script"""
    try:
        with open("pybank.sql", "r") as script_file:
            sql_script = script_file.read()
        
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.executescript(sql_script)
            connexion.commit()
            print("Database initialized successfully.")
            return True
    except Exception as error:
        print(f"Error initializing database: {error}")
        return False


# ==================== ACCOUNTS CRUD ====================


def create_account(name, bank, account_type, date, db_path="pybank.db"):
    """Create a new account"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute(
                "INSERT INTO Accounts (account_name, account_bank, account_type, account_date) VALUES (?, ?, ?, ?)",
                (name, bank, account_type, date)
            )
            connexion.commit()
            print(f"Account '{name}' created successfully.")
            return cursor.lastrowid
    except Exception as error:
        print(f"Error creating account: {error}")
        return None


def read_account(account_id, db_path="pybank.db"):
    """Read a single account by ID"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE account_id = ?", (account_id,))
            result = cursor.fetchone()
            if result is None:
                print(f"Account with ID {account_id} not found.")
                return None
            return list(result)
    except Exception as error:
        print(f"Error reading account: {error}")
        return None


def read_all_accounts(db_path="pybank.db"):
    """Read all accounts"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("SELECT * FROM Accounts")
            results = cursor.fetchall()
            return [list(row) for row in results]
    except Exception as error:
        print(f"Error reading all accounts: {error}")
        return []


def update_account(account_id, name, bank, account_type, date, db_path="pybank.db"):
    """Update an existing account"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute(
                "UPDATE Accounts SET account_name = ?, account_bank = ?, account_type = ?, account_date = ? WHERE account_id = ?",
                (name, bank, account_type, date, account_id)
            )
            connexion.commit()
            if cursor.rowcount == 0:
                print(f"Account with ID {account_id} not found.")
                return False
            print(f"Account {account_id} updated successfully.")
            return True
    except Exception as error:
        print(f"Error updating account: {error}")
        return False


def delete_account(account_id, db_path="pybank.db"):
    """Delete an account"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Accounts WHERE account_id = ?", (account_id,))
            connexion.commit()
            if cursor.rowcount == 0:
                print(f"Account with ID {account_id} not found.")
                return False
            print(f"Account {account_id} deleted successfully.")
            return True
    except Exception as error:
        print(f"Error deleting account: {error}")
        return False


# ==================== CATEGORIES CRUD ====================


def create_category(name, color, db_path="pybank.db")->str:
    """Create a new category"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute(
                "INSERT INTO Categories (category_name, category_color) VALUES (?, ?)",
                (name, color)
            )
            connexion.commit()
            print(f"Category '{name}' created successfully.")
            return cursor.lastrowid
    except Exception as error:
        print(f"Error creating category: {error}")
        return None


def read_category(category_id, db_path="pybank.db"):
    """Read a single category by ID"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("SELECT * FROM Categories WHERE category_id = ?", (category_id,))
            result = cursor.fetchone()
            if result is None:
                print(f"Category with ID {category_id} not found.")
                return None
            return list(result)
    except Exception as error:
        print(f"Error reading category: {error}")
        return None


def read_all_categories(db_path="pybank.db"):
    """Read all categories"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("SELECT * FROM Categories")
            results = cursor.fetchall()
            return [list(row) for row in results]
    except Exception as error:
        print(f"Error reading all categories: {error}")
        return []


def update_category(category_id, name, color, db_path="pybank.db"):
    """Update an existing category"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute(
                "UPDATE Categories SET category_name = ?, category_color = ? WHERE category_id = ?",
                (name, color, category_id)
            )
            connexion.commit()
            if cursor.rowcount == 0:
                print(f"Category with ID {category_id} not found.")
                return False
            print(f"Category {category_id} updated successfully.")
            return True
    except Exception as error:
        print(f"Error updating category: {error}")
        return False


def delete_category(category_id, db_path="pybank.db"):
    """Delete a category"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Categories WHERE category_id = ?", (category_id,))
            connexion.commit()
            if cursor.rowcount == 0:
                print(f"Category with ID {category_id} not found.")
                return False
            print(f"Category {category_id} deleted successfully.")
            return True
    except Exception as error:
        print(f"Error deleting category: {error}")
        return False


# ==================== TRANSACTIONS CRUD ====================


def create_transaction(amount, description, date, account_id, category_id, db_path="pybank.db"):
    """Create a new transaction"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute(
                "INSERT INTO Transactions (transaction_amount, transaction_seller, transaction_date, transaction_account, transaction_category) VALUES (?, ?, ?, ?, ?)",
                (amount, description, date, account_id, category_id)
            )
            connexion.commit()
            print(f"Transaction created successfully.")
            return cursor.lastrowid
    except Exception as error:
        print(f"Error creating transaction: {error}")
        return None


def read_transaction(transaction_id, db_path="pybank.db"):
    """Read a single transaction by ID"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("SELECT * FROM Transactions WHERE transaction_id = ?", (transaction_id,))
            result = cursor.fetchone()
            if result is None:
                print(f"Transaction with ID {transaction_id} not found.")
                return None
            return list(result)
    except Exception as error:
        print(f"Error reading transaction: {error}")
        return None


def read_all_transactions(db_path="pybank.db"):
    """Read all transactions"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("SELECT * FROM Transactions")
            results = cursor.fetchall()
            return [list(row) for row in results]
    except Exception as error:
        print(f"Error reading all transactions: {error}")
        return []


def update_transaction(transaction_id, amount, description, date, account_id, category_id, db_path="pybank.db"):
    """Update an existing transaction"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute(
                "UPDATE Transactions SET transaction_amount = ?, transaction_seller = ?, transaction_date = ?, transaction_account = ?, transaction_category = ? WHERE transaction_id = ?",
                (amount, description, date, account_id, category_id, transaction_id)
            )
            connexion.commit()
            if cursor.rowcount == 0:
                print(f"Transaction with ID {transaction_id} not found.")
                return False
            print(f"Transaction {transaction_id} updated successfully.")
            return True
    except Exception as error:
        print(f"Error updating transaction: {error}")
        return False


def delete_transaction(transaction_id, db_path="pybank.db"):
    """Delete a transaction"""
    try:
        with sqlite3.connect(db_path) as connexion:
            connexion.execute('PRAGMA foreign_keys = ON;')
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Transactions WHERE transaction_id = ?", (transaction_id,))
            connexion.commit()
            if cursor.rowcount == 0:
                print(f"Transaction with ID {transaction_id} not found.")
                return False
            print(f"Transaction {transaction_id} deleted successfully.")
            return True
    except Exception as error:
        print(f"Error deleting transaction: {error}")
        return False
    

def create_default_category():    
    with open('settings.json', 'r') as file:
        settings = json.load(file)
    if settings['category_created'] == 0:
        create_account("By default","Bank","Type","00/00/0000")
        create_category(" ","000000")
        create_category("Transport","000000")
        create_category("Alimentation","000000")
        create_category("Divertissement","000000")
        create_category("ArgentPoche","000000")
        create_category("CommandeLigne","000000")
        create_category("Restaurant","000000")
        create_category("Don","000000")
        create_category("Informatique","000000")
        create_category("Courses","000000")
        create_category("AutoEcole","000000")
        create_category("FranceTravail","000000")
        create_category("Sports","000000")
        create_category("JeuxVideos","000000")
        create_category("Vetements","000000")
        create_category("Banque","000000")
        create_category("Autre","000000")
        create_category("Ecole","000000")
        
        #Set category_created to 1 in json
        settings['category_created'] = 1
        
        #Save JSON data
        with open('settings.json', 'w') as file:
            json.dump(settings, file, indent=4)
    else:
        print("Categories already created.")
        read_all_categories()


if __name__ == "__main__":
    init_database()
    account_id = create_account("Courant quelqu'un","HSBC","Courant","03/11/2020")
    # Créer une catégorie
    category_id = create_category("Alimentation", "#FF5733")

    # Créer une transaction
    create_transaction(50, "Courses Carrefour", "2024-01-15", 1, 1)
    accounts = read_all_accounts()
    transaction = read_all_transactions()
    print(accounts)
    print(transaction)