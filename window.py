import tkinter as tk
import dataframe_manager as dm


def donothing():
    print("Doing nothing")


dfm = dm.DFManager("default")

root = tk.Tk()

# Root configuration
root.title("NHS Hours Tracker")
root.geometry("400x200")

# Home frame
home = tk.Frame(root, bg='red')
home.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.875)

open_button = tk.Button(home, text='Open an existing spreadsheet', command=dfm.open_excel)
open_button.place(relx=0, rely=0, relwidth=0.5, relheight=1.0)

new_button = tk.Button(home, text='Create a new spreadsheet', command=dfm.new_file)
new_button.place(relx=0.5, rely=0, relwidth=0.5, relheight=1.0)

# Create menu bar
menu_bar = tk.Menu(root)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=dfm.new_file)
file_menu.add_command(label="Open", command=dfm.open_excel)
file_menu.add_command(label="Save", command=dfm.save)
file_menu.add_command(label="Save as...", command=dfm.save_as)
file_menu.add_command(label="Close", command=donothing)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# Add file menu to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=donothing)

edit_menu.add_separator()

edit_menu.add_command(label="Cut", command=donothing)
edit_menu.add_command(label="Copy", command=donothing)
edit_menu.add_command(label="Paste", command=donothing)
edit_menu.add_command(label="Delete", command=donothing)
edit_menu.add_command(label="Select All", command=donothing)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", command=donothing)
help_menu.add_command(label="About...", command=donothing)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()


