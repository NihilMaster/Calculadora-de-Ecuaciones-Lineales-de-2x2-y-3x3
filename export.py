# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 08:53:17 2021

@author: M
"""

import tkinter as tk
import os
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from datetime import datetime

class Exp(tk.Toplevel):
    def __init__(self, parent, s, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Exportar")
        self.var = []
        self.s = s
        self.final = Paragraph
        
        try:
            os.mkdir('Exportado')
        except OSError:
            print("Directorio existente.")

        tk.Button(self, text="PDF", command=self.bPDF).pack()
        #tk.Button(self, text="CSV", command=self.bCSV).pack()
        #tk.Button(self, text="XLXS", command=self.bXLXS).pack()
        tk.Button(self, text="Cancelar", command=self.destroy).pack()
        
    def bPDF(self):
        spdf = self.s
        
        spdf = spdf.replace("Método de Gauss", "<b>Método de Gauss</b>")
        spdf = spdf.replace("Método de Gauss-Jordan", "<b>Método de Gauss-Jordan</b>")
        spdf = spdf.replace("Regla de Cramer", "<b>Regla de Cramer</b>")
        spdf = spdf.replace("│", "|")
        spdf = spdf.replace("⌈", "_")
        spdf = spdf.replace("⌉", "_")
        spdf = spdf.replace("⌊", "_")
        spdf = spdf.replace("⌋", "_")
        spdf = spdf.replace("∙", "×")
        spdf = spdf.replace("⁻", "-")
        spdf = spdf.replace("ᵗ", "^t")
        spdf = spdf.replace("₁", "<sub>1</sub>")
        spdf = spdf.replace("₂", "<sub>2</sub>")
        spdf = spdf.replace("₃", "<sub>2</sub>")
        
        sclean = Paragraph(
            spdf.replace("\n", "<br />"),
            ParagraphStyle(
                "ps1",
                fontName="Times-Roman",
                fontSize=11
            )
        )
        self.final = sclean
        self.accion(1)
        
    def bCSV(self): self.accion(2)
    def bXLXS(self): self.accion(3)
        
    def accion(self, tipo):
        if tipo==0:
            messagebox.showinfo(message="Seleccione una opción.", title="Alerta")            
        elif tipo==1:
            now = datetime.now()
            doc = SimpleDocTemplate(
                "Exportado/Resumen"+str(now.microsecond)+".pdf",
                pagesize=A4
            )
            doc.build([self.final])
            self.destroy()
            
        elif tipo==2:
            print("2")
            
        elif tipo==3:
            print("3")
            