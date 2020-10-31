import tkinter as tk
import dataframe_manager as dm

def donothing():
    print("Doing nothing")


dfm = dm.DF("default")

root = tk.Tk()

# Create menu bar
menu_bar = tk.Menu(root)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=donothing)
file_menu.add_command(label="Open", command=dfm.set_dir)
file_menu.add_command(label="Save", command=donothing)
file_menu.add_command(label="Save as...", command=donothing)
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


