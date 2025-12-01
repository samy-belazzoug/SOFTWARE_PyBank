CREATE TABLE IF NOT EXISTS Accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name VARCHAR(25),
    account_bank VARCHAR(25),
    account_type VARCHAR(25),
    account_date TEXT
);

CREATE TABLE IF NOT EXISTS Transactions(
    FOREIGN KEY (transaction_account) REFERENCES Accounts(account_id),
    FOREIGN KEY (transaction_category) REFERENCES Categories(category_id),
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_amount INTEGER,
    transaction_seller VARCHAR(25),
    transaction_date TEXT
);

CREATE TABLE IF NOT EXISTS Categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(25),
    category_color VARCHAR(25)
);