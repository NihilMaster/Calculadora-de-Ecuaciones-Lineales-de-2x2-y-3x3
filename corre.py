# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 02:19:37 2021

@author: M
"""

import tkinter as tk

class Corroborar(tk.Toplevel):
    def __init__(self, parent, resp, inp, typ, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Corroborar datos")
        r = [format(x,'.1f') for x in resp]
        i = [format(x,'.1f') for x in inp]
        # X₁    X₂    X₃
        tittle = tk.Frame(self)
        res = tk.Label(tittle, justify="center", text="Corroboración de resultados")
        res.pack()
        tittle.grid(row=0, column=0, columnspan=14)
        
        if(not typ):
            ley = tk.Frame(self)
            tk.Label(ley, justify="center", text="X₁").grid(row=1, column=0, padx=50, pady=5)
            tk.Label(ley, justify="center", text="X₂").grid(row=1, column=1, padx=(100,50), pady=5)
            tk.Label(ley, justify="center", text="X₃").grid(row=1, column=2, padx=(100,15), pady=5)
            respawn = tk.Frame(self)
            tk.Label(respawn, justify="center", text="Calculado").grid(row=1, column=3, padx=(45,5), pady=5)
            tk.Label(respawn, justify="center", text="Esperado").grid(row=1, column=4, padx=(15,0), pady=5)
            ley.grid(row=1, column=0, columnspan=10)
            respawn.grid(row=1, column=10, columnspan=14)
            
            x1 = format((inp[0]*resp[0]+inp[1]*resp[1]+inp[2]*resp[2]), '.1f')
            tk.Label(self, justify="center", text=i[0]).grid(row=2, column=0, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=2, column=1, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[0]).grid(row=2, column=2, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=2, column=3, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[1]).grid(row=2, column=4, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=2, column=5, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[1]).grid(row=2, column=6, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=2, column=7, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[2]).grid(row=2, column=8, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=2, column=9, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[2]).grid(row=2, column=10, padx=0, pady=5)
            tk.Label(self, justify="center", text="=").grid(row=2, column=11, padx=3, pady=5)
            tk.Label(self, justify="center", text=x1).grid(row=2, column=12, padx=20, pady=5)
            tk.Label(self, justify="center", text="|").grid(row=2, column=13, padx=5, pady=5)
            tk.Label(self, justify="center", text=i[3]).grid(row=2, column=14, padx=20, pady=5)
            
            x2 = format((inp[4]*resp[0]+inp[5]*resp[1]+inp[6]*resp[2]), '.1f')
            tk.Label(self, justify="center", text=i[4]).grid(row=3, column=0, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=3, column=1, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[0]).grid(row=3, column=2, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=3, column=3, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[5]).grid(row=3, column=4, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=3, column=5, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[1]).grid(row=3, column=6, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=3, column=7, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[6]).grid(row=3, column=8, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=3, column=9, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[2]).grid(row=3, column=10, padx=0, pady=5)
            tk.Label(self, justify="center", text="=").grid(row=3, column=11, padx=3, pady=5)
            tk.Label(self, justify="center", text=x2).grid(row=3, column=12, padx=20, pady=5)
            tk.Label(self, justify="center", text="|").grid(row=3, column=13, padx=5, pady=5)
            tk.Label(self, justify="center", text=i[7]).grid(row=3, column=14, padx=20, pady=5)
            
            x3 = format((inp[8]*resp[0]+inp[9]*resp[1]+inp[10]*resp[2]), '.1f')
            tk.Label(self, justify="center", text=i[8]).grid(row=4, column=0, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=4, column=1, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[0]).grid(row=4, column=2, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=4, column=3, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[9]).grid(row=4, column=4, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=4, column=5, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[1]).grid(row=4, column=6, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=4, column=7, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[10]).grid(row=4, column=8, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=4, column=9, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[2]).grid(row=4, column=10, padx=0, pady=5)
            tk.Label(self, justify="center", text="=").grid(row=4, column=11, padx=3, pady=5)
            tk.Label(self, justify="center", text=x3).grid(row=4, column=12, padx=20, pady=5)
            tk.Label(self, justify="center", text="|").grid(row=4, column=13, padx=5, pady=5)
            tk.Label(self, justify="center", text=i[11]).grid(row=4, column=14, padx=20, pady=5)
        else:
            ley = tk.Frame(self)
            tk.Label(ley, justify="center", text="X₁").grid(row=1, column=0, padx=35, pady=5)
            tk.Label(ley, justify="center", text="X₂").grid(row=1, column=1, padx=(50,25), pady=5)
            respawn = tk.Frame(self)
            tk.Label(respawn, justify="center", text="Calculado").grid(row=1, column=3, padx=(25,5), pady=5)
            tk.Label(respawn, justify="center", text="Esperado").grid(row=1, column=4, padx=(15,0), pady=5)
            ley.grid(row=1, column=0, columnspan=7)
            respawn.grid(row=1, column=7, columnspan=10)
            
            x1 = format((inp[0]*resp[0]+inp[1]*resp[1]), '.1f')
            tk.Label(self, justify="center", text=i[0]).grid(row=2, column=0, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=2, column=1, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[0]).grid(row=2, column=2, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=2, column=3, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[1]).grid(row=2, column=4, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=2, column=5, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[1]).grid(row=2, column=6, padx=0, pady=5)
            tk.Label(self, justify="center", text="=").grid(row=2, column=7, padx=3, pady=5)
            tk.Label(self, justify="center", text=x1).grid(row=2, column=8, padx=20, pady=5)
            tk.Label(self, justify="center", text="|").grid(row=2, column=9, padx=5, pady=5)
            tk.Label(self, justify="center", text=i[2]).grid(row=2, column=10, padx=20, pady=5)
            
            x2 = format((inp[3]*resp[0]+inp[4]*resp[1]), '.1f')
            tk.Label(self, justify="center", text=i[3]).grid(row=3, column=0, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=3, column=1, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[0]).grid(row=3, column=2, padx=0, pady=5)
            tk.Label(self, justify="center", text="+").grid(row=3, column=3, padx=3, pady=5)
            tk.Label(self, justify="center", text=i[4]).grid(row=3, column=4, padx=0, pady=5)
            tk.Label(self, justify="center", text="∙").grid(row=3, column=5, padx=0, pady=5)
            tk.Label(self, justify="center", text=r[1]).grid(row=3, column=6, padx=0, pady=5)
            tk.Label(self, justify="center", text="=").grid(row=3, column=7, padx=3, pady=5)
            tk.Label(self, justify="center", text=x2).grid(row=3, column=8, padx=20, pady=5)
            tk.Label(self, justify="center", text="|").grid(row=3, column=9, padx=5, pady=5)
            tk.Label(self, justify="center", text=i[5]).grid(row=3, column=10, padx=20, pady=5)

        butt = tk.Frame(self)
        tk.Button(butt, text="Volver", command=self.destroy).pack()
        butt.grid(row=5, column=0, columnspan=14)