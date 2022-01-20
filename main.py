# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:01:48 2021

@author: M
"""

import tkinter as tk
import tkinter.font as font
import dos
import tres


class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Solucionador")
        self.configure(bg='grey') # Color de Fondo

        txt = tk.Frame(self,bg="grey")
        tk.Label(txt, text="Escoja el orden del sistema.", font=font.Font(size=10), bg="grey").pack(pady=(20,0))
        txt.grid(row=0, column=0, columnspan=2)
        boton = tk.Button(self, text="2x2", width=20, command=self.sistema2)
        boton.grid(row=1, column=0, padx=20, pady=30)
        boton = tk.Button(self, text="3x3", width=20, command=self.sistema3)
        boton.grid(row=1, column=1, padx=20, pady=30)
        about = tk.Frame(self, bg="CadetBlue1")
        tk.Label(about, text="Mateo L. - Weimar Jurado", font=font.Font(size=10), bg="CadetBlue1").pack(padx=100)
        about.grid(row=2, column=0, columnspan=2)

    def sistema3(self):
        tres.TresScreen(self.parent)

    def sistema2(self):
        dos.DosScreen(self.parent)

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    