from tkinter import *
import tkinter.font as TkFont
from tkinter import ttk
from tkinter.ttk import Treeview
import random
import sqlite3
from sqlite3 import Error

class DatabasePy:
    def __init__(self):
        self.root = Tk()
        self.root.title('PyDatabase')
        self.root.geometry("900x600")
        self.root.config(bg="#657153")
        self.firstWindow()
        self.root.mainloop()

    def firstWindow(self):
        self.Frame = Frame(self.root,bg="#657153",width=400, height=520)
        self.Frame.pack(expand=YES)

        self.subFrame = Frame(self.Frame,borderwidth=3,relief='solid', bg="#657153")
        self.subFrame.pack(pady = 20) 
        
        self.Label3 = Label(self.subFrame,bg="#657153", text ='PyDatabase',font=("Serif", 35))
        self.Label3.pack(padx = 10, pady = 10)

        self.subLabel3 = Label(self.subFrame,bg="#657153", text ='Le gestionnaire SQL',font=("Serif", 25))
        self.subLabel3.pack(padx = 10, pady = 10)

        self.B = Button(self.Frame, text ="Démarrer le gestionnaire !", highlightthickness=4, bg="#7CAE7A",font=("Courrier", 19), command=self.menu)
        self.B.pack(pady = 30)

    def menu(self):
        self.Frame.destroy()

        self.Frame2 = Frame(self.root,borderwidth=3,relief='solid', bg="#657153",width=250, height=600)
        self.Frame2.pack_propagate(False)
        self.Frame2.pack(side=RIGHT, expand=YES, fill=BOTH)

        self.Frame3 = Frame(self.root,borderwidth=3,relief='solid',bg="#657153",width=600, height=600)
        self.Frame3.pack_propagate(False)
        self.Frame3.pack(side=LEFT,expand=YES,fill=BOTH)

        self.Label = Label(self.Frame2,bg="#657153", text ='Veuillez choisir une option:',font=("Serif", 15))
        self.Label.pack(padx = 10, pady = 10)

        self.B = Button(self.Frame2, text ="Créer une table", highlightthickness=4, bg="#7CAE7A",font=("Courrier", 15))
        self.B.pack(pady = 15)

        self.B2 = Button(self.Frame2, text ="Créer un élément", highlightthickness=4, bg="#7CAE7A",font=("Courrier", 15))
        self.B2.pack(pady = 15)

        self.B3 = Button(self.Frame2, text ="Modifier un élément", highlightthickness=4, bg="#7CAE7A",font=("Courrier", 15))
        self.B3.pack(pady = 15)

        self.B4 = Button(self.Frame2, text ="Suprimer un élément", highlightthickness=4, bg="#7CAE7A",font=("Courrier", 15))
        self.B4.pack(pady = 15)

        self.B5 = Button(self.Frame2, text ="Suprimer une table", highlightthickness=4, bg="#7CAE7A",font=("Courrier", 15))
        self.B5.pack(pady = 15)

        self.tableau = Treeview(self.Frame3, columns=('nom', 'type', 'schema'))
        self.tableau.heading('nom', text='Nom')
        self.tableau.heading('type', text='Type')
        self.tableau.heading('schema', text='Schéma')
        self.tableau['show'] = 'headings'
        self.tableau.pack(side=LEFT,fill=BOTH, expand=True)

        folder1= self.tableau.insert("", 1, "", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
    



d = DatabasePy()   