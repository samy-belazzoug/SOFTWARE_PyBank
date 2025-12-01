import tkinter as tk

"""------------------------------- W I N D O W -----------------------------"""


window = tk.Tk()


"""------------------------------- W I D G E T S -----------------------------"""


"""----- L A B E L S -------------------"""

label_hello = tk.Label(
    text="Welcome to Pybank!",
    foreground="white",
    background="purple",
    width=20,
    height=5
    )

label_name = tk.Label(text="Name")
label_date = tk.Label(text="Date")
label_amount = tk.Label(text="Amount")
label_description = tk.Label(text="Description")

"""----- E N T R I E S -------------------"""

entry_name = tk.Entry()
entry_date = tk.Entry()
entry_amount = tk.Entry()
entry_description = tk.Entry()

"""----- B U T T O N S -------------------"""

button_insert = tk.Button(
    text="Insert",
    foreground="green"
    )


button_update = tk.Button(
    text="Update",
    foreground="blue"
)


button_delete = tk.Button(
    text="Delete",
    foreground="red"
)


"""------------------------------- P A C K A G I N G -----------------------------"""


label_hello.pack() #Add hello Label to the window

label_name.pack()
entry_name.pack()
label_date.pack()
entry_date.pack()
label_amount.pack()
entry_amount.pack()
label_description.pack()
entry_description.pack()

button_insert.pack()
button_update.pack()
button_delete.pack()


"""------------------------------- M A I N L O O P -----------------------------"""

window.mainloop()