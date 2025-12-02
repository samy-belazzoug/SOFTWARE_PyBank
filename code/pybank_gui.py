import tkinter as tk
from tkinter import font
from tkinter import ttk

"""------------------------------- W I N D O W -----------------------------"""


window = tk.Tk()
window.title("PyBank")
window.geometry("1430x860")

window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
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

label_date = tk.Label(
    master=window,text="Date",
    #font=arial,
    )

label_operation = tk.Label(
    master=window,text="Operation",
    #font=arial,
    )

label_losses = tk.Label(
    master=window,
    text="Losses",
    #font=arial
    )

label_gains = tk.Label(
    master=window,
    text="Gains",
    #font=arial
    )

"""----- E N T R I E S -------------------"""

entry_date = tk.Entry(
    master=window,
    #font=arial
    )

entry_operation = tk.Entry(
    master=window,
    #font=arial
    )

entry_losses = tk.Entry(
    master=window,
    #font=arial
    )
entry_gains = tk.Entry(
    master=window,
    #font=arial
    )

"""----- B U T T O N S -------------------"""

button_insert = tk.Button(
    master=window,
    text="Insert",
    #font=arial,
    foreground="green"
    )


button_update = tk.Button(
    master=window,
    text="Update",
    #font=arial,
    foreground="blue"
)


button_delete = tk.Button(
    master=window,
    text="Delete",
    #font=arial,
    foreground="red"
)

"""----- T R E E V I E W -------------------"""

tree = ttk.Treeview(master=window,columns=("Operation","Losses","Gains"))
vertical_scrollbar = ttk.Scrollbar(master=window,orient=tk.VERTICAL,command=tree.yview)
tree.configure(yscrollcommand=vertical_scrollbar.set)

#Columns names
tree.heading("#0",text="Date")
tree.heading("Operation",text="Operation")
tree.heading("Losses",text="Losses")
tree.heading("Gains",text="Gains")

#Parents
transaction = tree.insert("",tk.END,text="05 / 2023") 

#Sons
tree.insert(transaction,tk.END,text="03/05",values=("Auchan",-4.84,0))
tree.insert(transaction,tk.END,text="15/05",values=("Amazon",-18.83,0))
tree.insert(transaction,tk.END,text="15/05",values=("Virement",0,+150))




"""------------------------------- P A C K A G I N G -----------------------------"""

label_hello.grid(row=0,column=0,sticky=tk.NW)

label_operation.grid(row=1,column=0,sticky=tk.W)
entry_operation.grid(row=2,column=0,sticky=tk.W)
button_insert.grid(row=3,column=0,sticky=tk.W)

label_date.grid(row=1,column=1,sticky=tk.W)
entry_date.grid(row=2,column=1,sticky=tk.W)
button_update.grid(row=3,column=1,sticky=tk.W)

label_losses.grid(row=1,column=2,sticky=tk.W)
entry_losses.grid(row=2,column=2,sticky=tk.W)
button_delete.grid(row=3,column=2,sticky=tk.W)

label_gains.grid(row=1,column=3,sticky=tk.W)
entry_gains.grid(row=2,column=3,sticky=tk.W)

tree.grid(row=4,column=0,sticky=tk.W,columnspan=3)
#vertical_scrollbar.grid(row=4,column=1)

"""------------------------------- M A I N L O O P -----------------------------"""

window.mainloop()