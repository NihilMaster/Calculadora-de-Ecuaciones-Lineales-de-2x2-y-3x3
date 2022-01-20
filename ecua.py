# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:09:18 2021

@author: M
"""
import tkinter as tk

class Ecua(tk.Toplevel):
    def __init__(self, parent, dif, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.dif = dif
        self.title("Ecuación")
        self.var = []
        
        dig = (self.register(self.callback))
        self.svx1 = tk.StringVar(self)
        x1 = tk.Entry(self, justify="center", textvariable=self.svx1, width=5, validate='all', validatecommand=(dig, '%P'))
        x1.grid(row=0,column=0, pady=(2,0), padx=(5,0))
        x_1 = tk.Label(self, text="X₁ +")
        x_1.grid(row=0,column=1, padx=(0,10), pady=(2,0))
        self.svx2 = tk.StringVar(self)
        x2 = tk.Entry(self, justify="center", textvariable=self.svx2, width=5, validate='all', validatecommand=(dig, '%P'))
        x2.grid(row=0,column=2, pady=(2,0))
        x_2 = tk.Label(self, text="X₂ +")
        x_2.grid(row=0,column=3, padx=(0,10), pady=(2,0))
        self.svx3 = tk.StringVar(self)        
        self.x3 = tk.Entry(self, justify="center", textvariable=self.svx3, width=5, validate='all', validatecommand=(dig, '%P'))
        self.x3.grid(row=0,column=4, pady=(2,0))
        x_3 = tk.Label(self, text="X₃")
        x_3.grid(row=0,column=5, padx=(0,10), pady=(2,0))
        x_eq1 = tk.Label(self, text="=")
        x_eq1.grid(row=0,column=6, padx=(0,10), pady=(2,0))
        self.svxe1 = tk.StringVar(self)
        xeq1 = tk.Entry(self, justify="center", textvariable=self.svxe1, width=5, validate='all', validatecommand=(dig, '%P'))
        xeq1.grid(row=0,column=7, pady=(2,0), padx=(0,5))
        
        self.svx4 = tk.StringVar(self)
        x4 = tk.Entry(self, justify="center", textvariable=self.svx4, width=5, validate='all', validatecommand=(dig, '%P'))
        x4.grid(row=1,column=0, padx=(5,0))
        x_4 = tk.Label(self, text="X₁ +")
        x_4.grid(row=1,column=1, padx=(0,10))
        self.svx5 = tk.StringVar(self)
        x5 = tk.Entry(self, justify="center", textvariable=self.svx5, width=5, validate='all', validatecommand=(dig, '%P'))
        x5.grid(row=1,column=2)
        x_5 = tk.Label(self, text="X₂ +")
        x_5.grid(row=1,column=3, padx=(0,10))
        self.svx6 = tk.StringVar(self)
        self.x6 = tk.Entry(self, justify="center", textvariable=self.svx6, width=5, validate='all', validatecommand=(dig, '%P'))
        self.x6.grid(row=1,column=4)
        x_6 = tk.Label(self, text="X₃")
        x_6.grid(row=1,column=5, padx=(0,10))
        x_eq2 = tk.Label(self, text="=")
        x_eq2.grid(row=1,column=6, padx=(0,10))
        self.svxe2 = tk.StringVar(self)
        xeq2 = tk.Entry(self, justify="center", textvariable=self.svxe2, width=5, validate='all', validatecommand=(dig, '%P'))
        xeq2.grid(row=1,column=7, padx=(0,5))
        
        self.svx7 = tk.StringVar(self)
        self.x7 = tk.Entry(self, justify="center", textvariable=self.svx7, width=5, validate='all', validatecommand=(dig, '%P'))
        self.x7.grid(row=2,column=0, padx=(5,0))
        x_7 = tk.Label(self, text="X₁ +")
        x_7.grid(row=2,column=1, padx=(0,10))
        self.svx8 = tk.StringVar(self)
        self.x8 = tk.Entry(self, justify="center", textvariable=self.svx8, width=5, validate='all', validatecommand=(dig, '%P'))
        self.x8.grid(row=2,column=2)
        x_8 = tk.Label(self, text="X₂ +")
        x_8.grid(row=2,column=3, padx=(0,10))
        self.svx9 = tk.StringVar(self)
        self.x9 = tk.Entry(self, justify="center", textvariable=self.svx9, width=5, validate='all', validatecommand=(dig, '%P'))
        self.x9.grid(row=2,column=4)
        x_9 = tk.Label(self, text="X₃")
        x_9.grid(row=2,column=5, padx=(0,10))
        x_eq3 = tk.Label(self, text="=")
        x_eq3.grid(row=2,column=6, padx=(0,10))
        self.svxe3 = tk.StringVar(self)
        self.xeq3 = tk.Entry(self, justify="center", textvariable=self.svxe3, width=5, validate='all', validatecommand=(dig, '%P'))
        self.xeq3.grid(row=2,column=7, padx=(0,5))
        
        if(self.dif):
            self.x3.configure(state="disabled")
            x_2.configure(text="X₂")
            x_3.configure(fg="gray84")
            self.x6.configure(state="disabled")
            x_5.configure(text="X₂")
            x_6.configure(fg="gray84")
            self.x7.configure(state="disabled")
            x_8.configure(text="X₂")
            x_7.configure(fg="gray84")
            self.x8.configure(state="disabled")
            x_8.configure(fg="gray84")
            self.x9.configure(state="disabled")
            x_9.configure(fg="gray84")
            x_eq3.configure(fg="gray84")
            self.xeq3.configure(state="disabled")
        
        envia = tk.Button(self, bg="LightSalmon2", text="Limpiar", command=self.clsX)
        envia.grid(row=4,column=0, columnspan=4, pady=(2,2))
        
        envia = tk.Button(self, bg="PeachPuff2", text="Enviar", command=self.prestroy)
        envia.grid(row=4,column=4, columnspan=4, pady=(2,2))
                
        ######################################################################
        self.svx1.set("3")
        self.svx2.set("2")
        self.svx3.set("2")
        self.svxe1.set("4")
        self.svx4.set("2")
        self.svx5.set("2")
        self.svx6.set("5")
        self.svxe2.set("1")
        self.svx7.set("1")
        self.svx8.set("9")
        self.svx9.set("4")
        self.svxe3.set("6")
        ######################################################################
        
        self.wait_window()
        
    def clsX(self):
        self.svx1.set("")
        self.svx2.set("")
        self.svx3.set("")
        self.svxe1.set("")
        self.svx4.set("")
        self.svx5.set("")
        self.svx6.set("")
        self.svxe2.set("")
        self.svx7.set("")
        self.svx8.set("")
        self.svx9.set("")
        self.svxe3.set("")
        
    def prestroy(self):
        self.var.append(float(self.svx1.get()))
        self.var.append(float(self.svx2.get()))
        if not self.dif: self.var.append(float(self.svx3.get()))
        self.var.append(float(self.svxe1.get()))
        self.var.append(float(self.svx4.get()))
        self.var.append(float(self.svx5.get()))
        if not self.dif: self.var.append(float(self.svx6.get()))
        self.var.append(float(self.svxe2.get()))
        if not self.dif: 
            self.var.append(float(self.svx7.get()))
            self.var.append(float(self.svx8.get()))
            self.var.append(float(self.svx9.get()))
            self.var.append(float(self.svxe3.get()))

        self.destroy()      
        
    def getVar(self):
        return self.var
  
    def callback(self, P):
        list1=[]
        list1[:0]=P
        if str.isdigit(P) or P == "" or self.dat(P):            
            return True
        else:
            return False
        
    def dat(self, P):
        list1=[]
        list1[:0]=P
        count1=0
        count2=0
        for i in list1:
            if i=="-": count1 = count1+1
            if i==".": count2 = count2+1
        if list1[0] == ".": return False #No empieza con punto
        if list1[0] == "-" and list1[1] == ".": return False #No tiene el punto después del menos
        if count1>1 or count2>1: return False #No tiene más de un punto o menos
        else: return True