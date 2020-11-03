import pandas as pd
from tkinter import filedialog, messagebox
import tkinter as tk
import xlrd


class DFManager:
    df1 = None
    df2 = None
    df3 = None
    df4 = None
    dir = None
    # file_name = None
    saved = None

    def __init__(self, name):
        self.df1 = pd.DataFrame(columns=['Names', 'Total Hours', 'History -->'])
        self.df2 = pd.DataFrame(columns=['Names', 'Total Hours', 'History -->'])
        self.df3 = pd.DataFrame(columns=['Names', 'Total Hours', 'History -->'])
        self.df4 = pd.DataFrame(columns=['Names', 'Total Hours', 'History -->'])
        self.dir = "/"
        # self.file_name = name
        self.saved = False

    # def get_file_name(self):
    #     return self.file_name

    def get_saved(self):
        return self.saved

    def set_dir(self):
        self.dir = filedialog.askopenfilename(title="Open Spreadsheet", filetypes=[("Excel Files", ".xls .xlsx")])
        # dir_split = self.dir.split('/')
        # self.file_name = dir_split[-1]
        return self.dir

    def new_file(self):
        self.df1.columns = ['Names', 'Total Hours', 'History -->']
        self.df2.columns = ['Names', 'Total Hours', 'History -->']
        self.df3.columns = ['Names', 'Total Hours', 'History -->']
        self.df4.columns = ['Names', 'Total Hours', 'History -->']

    def open_excel(self):
        opened = self.set_dir()
        try:
            self.df1 = pd.read_excel(opened, 'Freshman')
            self.df2 = pd.read_excel(opened, 'Sophomore')
            self.df3 = pd.read_excel(opened, 'Junior')
            self.df4 = pd.read_excel(opened, 'Senior')
        except ValueError:
            create_new = messagebox.askyesno(title='Invalid Spreadsheet',
                                             message='Error: Invalid spreadsheet format detected\n'
                                                     'Would you like to create a new spreadsheet?')
            if create_new:
                self.new_file()

        except xlrd.biffh.XLRDError:
            create_new = messagebox.askyesno(title='Invalid Spreadsheet',
                                             message='Error: Invalid spreadsheet format detected.\n'
                                                     'Would you like to create a new spreadsheet?')
            if create_new:
                self.new_file()

    def save(self):
        with pd.ExcelWriter(self.dir) as writer:
            self.df1.to_excel(writer, sheet_name='Freshman', index=False)
            self.df2.to_excel(writer, sheet_name='Sophomore', index=False)
            self.df3.to_excel(writer, sheet_name='Junior', index=False)
            self.df4.to_excel(writer, sheet_name='Senior', index=False)
        self.saved = True

    def save_as(self):
        self.dir = filedialog.asksaveasfilename(title="Save Spreadsheet", defaultextension='.xlsx',
                                                      filetypes=[("Excel Files", ".xls .xlsx")])
        self.save()

