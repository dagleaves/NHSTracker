import pandas as pd
from tkinter import filedialog


class DF:
    def __init__(self, name):
        self.df1 = pd.DataFrame
        self.df2 = pd.DataFrame
        self.df3 = pd.DataFrame
        self.df4 = pd.DataFrame
        self.dir = "/"
        self.file_name = name
        self.saved = False

    def save(self):
        with pd.ExcelWriter(self.dir + self.file_name) as writer:
            self.df1.to_excel(writer, sheet_name='Freshman')
            self.df2.to_excel(writer, sheet_name='Sophomore')
            self.df3.to_excel(writer, sheet_name='Junior')
            self.df4.to_excel(writer, sheet_name='Senior')
        self.saved = True

    def set_dir(self):
        self.dir = filedialog.askopenfilename(initialdir="/", title="Open Spreadsheet",
                                              filetypes=[("Excel Files", ".xls .xlsx")])
        dir_split = self.dir.split('/')
        self.file_name = dir_split[-1]
        print(self.dir)
        print(self.file_name)
