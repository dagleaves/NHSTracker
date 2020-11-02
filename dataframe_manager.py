import pandas as pd
import tkinter as tk


class DFManager:
    def __init__(self, name):
        self.df1 = pd.DataFrame
        self.df2 = pd.DataFrame
        self.df3 = pd.DataFrame
        self.df4 = pd.DataFrame
        self.dir = "/"
        self.file_name = name
        self.saved = False

    def get_file_name(self):
        return self.file_name

    def get_saved(self):
        return self.saved

    def open_excel(self):
        opened = self.set_dir()
        try:
            self.df1 = pd.read_excel(opened, 'Freshman')
            self.df2 = pd.read_excel(opened, 'Sophomore')
            self.df3 = pd.read_excel(opened, 'Junior')
            self.df4 = pd.read_excel(opened, 'Senior')
        except:
            print(tk.messagebox.askyesno(title='Invalid Spreadsheet',
                                         message='Error: Invalid spreadsheet format detected'))
            # TODO: Check pandas dataframe error code


    def save(self):
        with pd.ExcelWriter(self.dir + self.file_name) as writer:
            self.df1.to_excel(writer, sheet_name='Freshman')
            self.df2.to_excel(writer, sheet_name='Sophomore')
            self.df3.to_excel(writer, sheet_name='Junior')
            self.df4.to_excel(writer, sheet_name='Senior')
        self.saved = True

    def set_dir(self):
        self.dir = tk.filedialog.askopenfilename(initialdir="/", title="Open Spreadsheet",
                                                 filetypes=[("Excel Files", ".xls .xlsx")])
        dir_split = self.dir.split('/')
        self.file_name = dir_split[-1]
        return self.dir

