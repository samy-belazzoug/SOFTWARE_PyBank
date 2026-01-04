import tkinter as tk
from tkinter import font
from tkinter import ttk
import pybank_db


"""------------------------------- W I N D O W -----------------------------"""


window = tk.Tk()
window.title("PyBank")
window.geometry("1420x860")

window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)


"""------------------------------- D A T A B A S E -----------------------------"""


pybank_db.init_database()
pybank_db.create_default_category()


"""----- T R A N S A C T I ON S -------------------"""


"""----- C A T E G O R I E S -------------------"""


categories = pybank_db.read_all_categories()
categories_list = []
for i in range(len(categories)):
    categories_list.append(categories[i][1])
print(categories_list)



"""------------------------------- F O N T S -----------------------------"""


#arial = tkinter.font.Font(family="Arial",size=18,weight="normal")


"""------------------------------- W I D G E T S -----------------------------"""


"""----- F R A M E S -------------------"""


frame_background = tk.Frame(master=window,background="black")


"""----- L A B E L S -------------------"""


label_hello = tk.Label(
    master=window,
    text="Welcome to Pybank!",
    #font=arial,
    foreground="white",
    background="purple",
    width=20,
    height=5
    )

label_id = tk.Label(
    master=window,
    text="ID",
    #font=arial
    )

label_amount = tk.Label(
    master=window,
    text="Amount",
    #font=arial
    )

label_operation = tk.Label(
    master=window,text="Operation",
    #font=arial,
    )

label_date = tk.Label(
    master=window,text="Date",
    #font=arial,
    )

label_category = tk.Label(
    master=window,
    text="Category",
    #font=arial
    )


"""----- E N T R I E S -------------------"""

entry_id = tk.Entry(
    master=window,
    #font=arial
    )

entry_amount = tk.Entry(
    master=window,
    #font=arial
    )

entry_operation = tk.Entry(
    master=window,
    #font=arial
    )

entry_date = tk.Entry(
    master=window,
    #font=arial
    )

entry_category = tk.Entry(
    master=window,
    #font=arial
    )


"""------------------------------- C O M B O B O X -----------------------------"""

combo_category = ttk.Combobox(
    master=window,
    values=categories_list
    )
combo_category.set("Category")


"""----- T R E E V I E W -------------------"""


tree = ttk.Treeview(master=window,columns=("Date","Operation","Losses","Gains"))
vertical_scrollbar = ttk.Scrollbar(master=window,orient=tk.VERTICAL,command=tree.yview)
tree.configure(yscrollcommand=vertical_scrollbar.set)

#Columns names
tree.heading("#0",text="id")
tree.heading("Date",text="Date")
tree.heading("Operation",text="Operation")
tree.heading("Losses",text="Amount")
tree.heading("Gains",text="Category")


"""------------------------------- F U N C T I O N S -----------------------------"""

def tree_read():
    """Display all the transactions"""
    for i in tree.get_children():
        tree.delete(i)
    
    transactions = pybank_db.read_all_transactions()
    transactions_id_list = []
    transactions_date_list = []
    transactions_operation_list = []
    transactions_amount_list = []
    transactions_category_list = []
    for i in range(len(transactions)):
        transactions_id_list.append(transactions[i][0])
        transactions_amount_list.append(transactions[i][1])
        transactions_operation_list.append(transactions[i][2])
        transactions_date_list.append(transactions[i][3])    
        transactions_category_list.append(categories[transactions[i][5]])
        tree.insert("",index='end',text=transactions_id_list[i], values=(transactions_date_list[i] , transactions_operation_list[i] , transactions_amount_list[i] , transactions_category_list[i][1]))
    transactions.clear()

def insert_button():
    pybank_db.create_transaction(entry_amount.get(),entry_operation.get(),entry_date.get(),1,combo_category.current())
    print(pybank_db.read_all_transactions())
    print(combo_category.current())
    tree_read()
def update_button():
    pybank_db.update_transaction(entry_id.get(),entry_amount.get(),entry_operation.get(),entry_date.get(),1,combo_category.current())
    print(pybank_db.read_all_transactions())
    print(combo_category.current())
    tree_read()
def delete_button():
    pybank_db.delete_transaction(entry_id.get())
    print(pybank_db.read_all_transactions())
    print(combo_category.current())
    tree_read()



"""----- B U T T O N S -------------------"""


button_insert = tk.Button(
    master=window,
    text="Insert",
    #font=arial,
    foreground="green",
    command=insert_button
    )

button_update = tk.Button(
    master=window,
    text="Update",
    #font=arial,
    foreground="blue",
    command=update_button
)

button_delete = tk.Button(
    master=window,
    text="Delete",
    #font=arial,
    foreground="red",
    command=delete_button
)


"""------------------------------- P A C K A G I N G -----------------------------"""


label_hello.grid(row=0,column=0,sticky=tk.NW)

label_id.grid(row=1,column=0,sticky=tk.W)
entry_id.grid(row=2,column=0,sticky=tk.W)

label_date.grid(row=1,column=1,sticky=tk.W)
entry_date.grid(row=2,column=1,sticky=tk.W)

label_operation.grid(row=1,column=2,sticky=tk.W)
entry_operation.grid(row=2,column=2,sticky=tk.W)

label_amount.grid(row=1,column=3,sticky=tk.W)
entry_amount.grid(row=2,column=3,sticky=tk.W)

label_category.grid(row=1,column=4,sticky=tk.W)
combo_category.grid(row=2,column=4,sticky=tk.W)


button_insert.grid(row=3,column=0,sticky=tk.W)
button_update.grid(row=3,column=1,sticky=tk.W)
button_delete.grid(row=3,column=2,sticky=tk.W)

tree.grid(row=4,column=0,sticky=tk.W,columnspan=3)
#vertical_scrollbar.grid(row=4,column=1)


"""------------------------------- M A I N L O O P -----------------------------"""
tree_read()
window.mainloop()