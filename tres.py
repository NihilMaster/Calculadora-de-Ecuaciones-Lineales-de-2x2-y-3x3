# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:01:38 2021

@author: M
"""

import tkinter as tk
import tkinter.font as font
import matplotlib.pyplot as plt
from tkinter import messagebox
import ecua as ec
import corre as crr
import export as exp

class TresScreen(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Sistema de 3x3")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        self.configure(background='#772554')
        self.inn = []; self.rescorr = []
        self.valz1 = []; self.valz2 = []; self.valz3 = []
        self.valx = range(-10, 10); self.valy = range(-10, 10)
        self.valxM = []; self.valyM = []
        self.checkIN  = False
        self.checkSOL = False
        
        self.contenido = tk.Frame(self, bg="#772554")
        self.result = tk.Label(self.contenido, bg="#772554", font=font.Font(size=15), fg="#ffd6d6", text='Ecuación', padx=5, pady=5, width=50)
        self.result.grid(row=1,column=0,columnspan=2)
        
        freso = tk.Frame(self.contenido)
        self.resp = tk.Text(freso, bg="#a32f58", fg="#ffd6d6", height=20, width=60) # anchor="nw"
        self.resp.grid(row=0,column=0)
        self.sresp = "Resultado..."
        self.resp.insert(tk.INSERT, self.sresp)
        scroll = tk.Scrollbar(freso, orient='vertical', bg="#a32f58", command=self.resp.yview)
        scroll.grid(row=0,column=1, sticky="ns")
        self.resp['yscrollcommand'] = scroll.set
        freso.grid(row=2,column=0, columnspan=2, padx=3, pady=4)
        
        self.contenido.grid(row=0, column=0)
        
        tombos = tk.Frame(self, bg="#772554")
        ecuacion = tk.Button(tombos, bg="#e54361", text="Ecuación", command=self.setEc)
        ecuacion.grid(row=0,column=0, padx=(5,20), pady=(5,10))
        calcular = tk.Button(tombos, bg="#e54361", text="Calcular", command=self.resol)
        calcular.grid(row=1,column=0, padx=(5,20), pady=10)
        self.grafic = tk.Button(tombos, bg="#ffbe7f", text="Graficar", command=self.matplotCanvas)
        self.grafic.grid(row=2,column=0, columnspan=2, padx=(5,20), pady=10)
        export = tk.Button(tombos, bg="#ff7976", text="Exportar", command=self.setExp)
        export.grid(row=3,column=0, padx=(5,20), pady=10)
        corrob = tk.Button(tombos, bg="#ff7976", text="Corroborar", command=self.corroborar)
        corrob.grid(row=4,column=0, padx=(5,20), pady=10)
        volver = tk.Button(tombos, bg="black", fg="white", text="Volver", command=self.volver)
        volver.grid(row=5,column=0, columnspan=2, padx=(5,20), pady=10)
        
        tombos.grid(row=0,column=1)
        
        self.parent.withdraw()

    def volver(self):
        self.parent.deiconify()
        self.destroy()
        
    def setEc(self):
        a = SetEc(self.parent)
        self.valz1.clear()
        self.valz2.clear()
        self.valxM.clear()
        self.valyM.clear()
        self.result.configure(text=str(a[0])+"X₁ + "+str(a[1])+"X₂ = "+str(a[2])+"X₃ = "+str(a[3])+
                              "\n"+str(a[4])+"X₁ + "+str(a[5])+"X₂ = "+str(a[6])+"X₃ = "+str(a[7])+
                              "\n"+str(a[8])+"X₁ + "+str(a[9])+"X₂ = "+str(a[10])+"X₃ = "+str(a[11]))
        
        if a[2]==0 or a[6]==0 or a[10]==0:
            self.grafic.configure(state="disabled")
        else:
            self.grafic.configure(state="normal")
            for i in self.valx:
                for j in self.valy:
                    self.valz1.append(((a[3]-a[0]*i-a[1]*j)/a[2]))
                    self.valz2.append(((a[7]-a[4]*i-a[5]*j)/a[6]))
                    self.valz3.append(((a[11]-a[8]*i-a[9]*j)/a[10]))
                    self.valxM.append(i)
                    self.valyM.append(j)
        self.inn = a 
        self.checkIN  = True
        self.checkSOL = False
        
    def setExp(self):
        if self.checkSOL:            
            Expr(self.parent, ("Sistema 3x3\n\n\n\n" + self.resp.get('1.0', 'end-1c')))
        else:
            messagebox.showinfo(message="La exportación se debe hacer después\nde que se haya resuelto algún problema.", title="Alerta")
    
    def corroborar(self):
        if self.checkSOL:
            Corro(self.parent, self.rescorr, self.inn)
        else:
            messagebox.showinfo(message="La corroboración se debe hacer después\nde que se haya resuelto algún problema.", title="Alerta")
        
    def matplotCanvas(self):
        if self.checkSOL:
            ax = plt.figure("Representación gráfica").add_subplot(projection='3d')
            x = [format(x,'.1f') for x in self.inn]
            ax.plot_trisurf(self.valxM, self.valyM, self.valz1, linewidth=0.2, antialiased=True, color="black")
            ax.plot_trisurf(self.valxM, self.valyM, self.valz2, linewidth=0.2, antialiased=True, color="#4AFAB1")
            ax.plot_trisurf(self.valxM, self.valyM, self.valz3, linewidth=0.2, antialiased=True, color="#543FFB")
            
            Ecuacion1 = (x[0]+ "X₁ + " + x[1]+ "X₂ + " + x[2] + "X₃ = " + x[3])
            Ecuacion2 = (x[4]+ "X₁ + " + x[5]+ "X₂ + " + x[6] + "X₃ = " + x[7])
            Ecuacion3 = (x[8]+ "X₁ + " + x[9]+ "X₂ + " + x[10] + "X₃ = " + x[11])
            
            ax.text2D(-0.30, 1.05, Ecuacion1, color="black", fontweight="heavy", transform=ax.transAxes)
            ax.text2D(-0.30, 1.0, Ecuacion2, color="#4AFAB1", fontweight="heavy", transform=ax.transAxes)
            ax.text2D(-0.30, 0.95, Ecuacion3, color="#543FFB", fontweight="heavy", transform=ax.transAxes)
                        
            plt.show()
        else:
            messagebox.showinfo(message="La graficación se debe hacer después\nde que se haya resuelto algún problema.", title="Alerta")
    
    def resol(self):
        if not self.checkIN:
            messagebox.showinfo(message="La solución y graficación se debe hacer después\nde que se haya ingresado un sistema de ecuaciones.", title="Alerta")            
            return 0;

        a_i = [float(x) for x in self.inn]
        s = "Método de Gauss\n\n\n"
        
        mat_i = [[a_i[0],a_i[1],a_i[2],a_i[3]],[a_i[4],a_i[5],a_i[6],a_i[7]],[a_i[8],a_i[9],a_i[10],a_i[11]]]
        aux = [x*1 for x in mat_i]
        
        if (aux[0][0] == 0 and aux[1][0] == 0 and aux[2][0] == 0 or
            aux[0][1] == 0 and aux[1][1] == 0 and aux[2][1] == 0 or 
            aux[0][2] == 0 and aux[1][2] == 0 and aux[2][2] == 0 or
            aux[0][0] == 0 and aux[1][0] == 0 and aux[0][1] == 0 and aux[1][1] == 0 or 
            aux[0][0] == 0 and aux[2][0] == 0 and aux[0][2] == 0 and aux[2][2] == 0 or 
            aux[1][1] == 0 and aux[2][1] == 0 and aux[1][2] == 0 and aux[2][2] == 0):
            s = "Método de Gauss\n\n"
            s = s + "El sistema no tiene solución\n\n\n\n"
            s = s + "Método de Gauss-Jordan\n\n"
            s = s + "El sistema no tiene solución\n\n\n\n"
            s = s + "Regla de Cramer\n\n"
            s = s + "El número de ecuaciones\ndebe ser igual al\nnúmero de incógnitas.\n\n\n\n"
            s = s + "Método de la matriz inversa\n\n"
            s = s + "El número de ecuaciones\ndebe ser igual al\nnúmero de incógnitas."
            self.resp.delete("1.0","end")
            self.resp.insert(1.0, s)
            self.checkSOL = True
            return
            
        s = s + "Matriz inicial:\n"
        s = s + self.printMaz(mat_i)
        
        s = s + "Matriz escalonada.\n"
        
        #1
        s = s + "Primer iteración:\n"
        aux = [x*1 for x in mat_i]
        if aux[0][0] == 0 and aux[1][0] == 0:
            s = s + "F₃ <=> F₁\n\n"
            for i in [0, 1, 2, 3]:
                mat_i[2][i] = aux[0][i]
                mat_i[0][i] = aux[2][i]
        elif aux[0][0] == 0:
            s = s + "F₂ <=> F₁\n\n"
            for i in [0, 1, 2, 3]:
                mat_i[1][i] = aux[0][i]
                mat_i[0][i] = aux[1][i]
        else:
            s = s + "F₂ = F₂ - ( "+format(aux[1][0],'.2f')+"/"+format(aux[0][0],'.2f')+" ) ∙ F₁\n"
            for i in [0, 1, 2, 3]:
                mat_i[1][i] = aux[1][i] - (aux[1][0]/aux[0][0]) * aux[0][i]
        s = s + self.printMaz(mat_i)
                
        #2
        aux = [x*1 for x in mat_i]
        for i in [0, 1, 2, 3]:
            mat_i[2][i] = aux[2][i] - (aux[2][0]/aux[0][0]) * aux[0][i]
        s = s + "Segunda iteración:\n"
        s = s + "F₃ = F₃ - ( "+format(aux[2][0],'.2f')+"/"+format(aux[0][0],'.2f')+" ) ∙ F₁\n"
        s = s + self.printMaz(mat_i)
        
        #3
        s = s + "Tercera iteración:\n"
        aux = [x*1 for x in mat_i]
        if aux[1][1] == 0:
            s = s + "F₃ <=> F₂\n\n"            
            for i in [0, 1, 2, 3]:
                mat_i[2][i] = aux[1][i]
                mat_i[1][i] = aux[2][i]
        else:
            s = s + "F₃ = F₃ - ( "+format(aux[2][1],'.2f')+"/"+format(aux[1][1],'.2f')+" ) ∙ F₂\n"
            for i in [0, 1, 2, 3]:
                mat_i[2][i] = aux[2][i] - (aux[2][1]/aux[1][1]) * aux[1][i]
        s = s + self.printMaz(mat_i)

        s = s + "Solución del sistema:\n"
        s = s + "Si:        "+format(mat_i[2][2],'.2f')+"X₃ = "+format(mat_i[2][3],'.2f')+"\n"
        s = s + "Entonces:  X₃ = "+format(mat_i[2][3]/mat_i[2][2],'.2f')+"\n"
        s = s + "Por ende:  X₂ = "+format((mat_i[1][3]-(mat_i[1][2]*(mat_i[2][3]/mat_i[2][2])))/mat_i[1][1],'.2f')+"\n"
        s = s + "Al final:  X₁ = "+format((mat_i[0][3] - (mat_i[0][2]*(mat_i[2][3]/mat_i[2][2])) - (mat_i[0][1]*(mat_i[1][3]-(mat_i[1][2]*(mat_i[2][3]/mat_i[2][2])))/mat_i[1][1]))/mat_i[0][0],'.2f')+"\n\n\n"
        

        s = s + "Método de Gauss-Jordan\n\n\n"
        
        mat_i = [[a_i[0],a_i[1],a_i[2],a_i[3]],[a_i[4],a_i[5],a_i[6],a_i[7]],[a_i[8],a_i[9],a_i[10],a_i[11]]]
        
        s = s + "Matriz inicial:\n"
        s = s + self.printMaz(mat_i)
        
        #1
        s = s + "Primer iteración:\n"
        aux = [x*1 for x in mat_i]
        if aux[0][0] == 0 and aux[1][0] == 0:
            s = s + "F₃ <=> F₁\n\n"
            for i in [0, 1, 2, 3]:
                mat_i[2][i] = aux[0][i]
                mat_i[0][i] = aux[2][i]
        elif aux[0][0] == 0:
            s = s + "F₂ <=> F₁\n\n"
            for i in [0, 1, 2, 3]:
                mat_i[1][i] = aux[0][i]
                mat_i[0][i] = aux[1][i]            
        else:
            s = s + "F₁ = F₁ / "+format(aux[0][0],'.2f')+"\n"
            for i in [0, 1, 2, 3]:
                mat_i[0][i] = aux[0][i]/aux[0][0]
        s = s + self.printMaz(mat_i)
        
        #2
        s = s + "Segunda iteración:\n"
        aux = [x*1 for x in mat_i]
        if aux[1][0] == 0:
            s = s + "F₁ = F₁ / "+format(aux[0][0],'.2f')+"\n"
            for i in [0, 1, 2, 3]:
                mat_i[0][i] = aux[0][i]/aux[0][0]
        else:
            s = s + "F₂ = F₂ - ( "+format(aux[0][0],'.2f')+" ∙ F₁ )\n"
            for i in [0, 1, 2, 3]:
                mat_i[1][i] = aux[1][i]-(aux[1][0]*aux[0][i])  
        s = s + self.printMaz(mat_i)
        
        #3
        aux = [x*1 for x in mat_i]
        for i in [0, 1, 2, 3]:
            mat_i[2][i] = aux[2][i]-(aux[2][0]*aux[0][i])   
        s = s + "Tercer iteración:\n"
        s = s + "F₃ = F₃ - ( "+format(aux[2][0],'.2f')+" ∙ F₁ )\n"
        s = s + self.printMaz(mat_i)
        
        #4
        s = s + "Cuarta iteración:\n"
        aux = [x*1 for x in mat_i]
        if aux[1][1] == 0:
            s = s + "F₃ <=> F₂\n\n"            
            for i in [0, 1, 2, 3]:
                mat_i[2][i] = aux[1][i]
                mat_i[1][i] = aux[2][i]
        else:
            s = s + "F₂ = F₂ / "+format(aux[1][1],'.2f')+"\n"
            for i in [0, 1, 2, 3]:
                mat_i[1][i] = aux[1][i]/aux[1][1]
        s = s + self.printMaz(mat_i)
        
        #5
        s = s + "Quinta iteración:\n"
        aux = [x*1 for x in mat_i]
        if aux[2][1] == 0:
            s = s + "F₂ = F₂ / "+format(aux[1][1],'.2f')+"\n"
            for i in [0, 1, 2, 3]:
                mat_i[1][i] = aux[1][i]/aux[1][1]
        else:
            s = s + "F₃ = F₃ - ( "+format(aux[2][1],'.2f')+" ∙ F₂ )\n"
            for i in [0, 1, 2, 3]:
                mat_i[2][i] = aux[2][i]-(aux[2][1]*aux[1][i])
        s = s + self.printMaz(mat_i)
        
        #6
        aux = [x*1 for x in mat_i]
        for i in [0, 1, 2, 3]:
            mat_i[2][i] = aux[2][i]/aux[2][2]
        s = s + "Sexta iteración:\n"
        s = s + "F₃ = F₃ / "+format(aux[2][2],'.2f')+"\n"
        s = s + self.printMaz(mat_i)
        
        #7
        aux = [x*1 for x in mat_i]
        for i in [0, 1, 2, 3]:
            mat_i[1][i] = aux[1][i]-(aux[1][2]*aux[2][i])
        s = s + "Séptima iteración:\n"
        s = s + "F₂ = F₂ - ( "+format(aux[1][2],'.2f')+" ∙ F₃ )\n"
        s = s + self.printMaz(mat_i)
        
        #8
        aux = [x*1 for x in mat_i]
        for i in [0, 1, 2, 3]:
            mat_i[0][i] = aux[0][i]-(aux[0][2]*aux[2][i])   
        s = s + "Octava iteración:\n"
        s = s + "F₁ = F₁ - ( "+format(aux[0][2],'.2f')+" ∙ F₃ )\n"
        s = s + self.printMaz(mat_i)
        
        #9
        aux = [x*1 for x in mat_i]
        for i in [0, 1, 2, 3]:
            mat_i[0][i] = aux[0][i]-(aux[0][1]*aux[1][i])
        s = s + "Novena iteración:\n"
        s = s + "F₁ = F₁ - ( "+format(aux[0][1],'.2f')+" ∙ F₂ )\n"
        s = s + self.printMaz(mat_i)
        
        s = s + "Solución del sistema:\n    X₁ = "+format(mat_i[0][3],'.2f')+"\n    X₂ = "+format(mat_i[1][3],'.2f')+"\n    X₃ = "+format(mat_i[2][3],'.2f') + "\n\n\n"
        self.rescorr.append(mat_i[0][3])
        self.rescorr.append(mat_i[1][3])
        self.rescorr.append(mat_i[2][3])
        
        #Δ
        s = s + "Regla de Cramer\n\n\nΔ "
        mat_i = [[a_i[0],a_i[1],a_i[2],a_i[3]],[a_i[4],a_i[5],a_i[6],a_i[7]],[a_i[8],a_i[9],a_i[10],a_i[11]]]
        aux = [x*1 for x in mat_i]
        ra = []
        aS = 0; aI = 0
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),format(aux[i][2],'.2f'),"│")  
        aS = aux[0][0]*aux[1][1]*aux[2][2] + aux[0][1]*aux[1][2]*aux[2][0] + aux[0][2]*aux[1][0]*aux[2][1]
        aI = aux[0][2]*aux[1][1]*aux[2][0] + aux[0][0]*aux[1][2]*aux[2][1] + aux[0][1]*aux[1][0]*aux[2][2]
        ra.append(aS-aI)
        s = s + "= " + format(aS-aI,'.2f') + "\n\nΔ₁"
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][3],'.2f'),format(aux[i][1],'.2f'),format(aux[i][2], '.2f'),"│")
        aS = aux[0][3]*aux[1][1]*aux[2][2] + aux[0][1]*aux[1][2]*aux[2][3] + aux[1][3]*aux[2][1]*aux[0][2]
        aI = aux[0][2]*aux[1][1]*aux[2][3] + aux[0][3]*aux[1][2]*aux[2][1] + aux[0][1]*aux[1][3]*aux[2][2]
        ra.append(aS-aI)
        s = s + "= " + format(aS-aI,'.2f') + "\n\nΔ₂"
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][2],'.2f'),format(aux[i][2], '.2f'),"│")  
        aS = aux[0][0]*aux[1][3]*aux[2][2] + aux[0][3]*aux[1][2]*aux[2][0] + aux[0][2]*aux[2][3]*aux[1][0]
        aI = aux[0][2]*aux[1][3]*aux[2][0] + aux[0][0]*aux[1][2]*aux[2][3] + aux[1][0]*aux[0][3]*aux[2][2]
        ra.append(aS-aI)
        s = s + "= " + format(aS-aI,'.2f') + "\n\nΔ₃"
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][2],'.2f'),format(aux[i][2], '.2f'),"│")  
        aS = aux[0][0]*aux[1][1]*aux[2][3] + aux[0][1]*aux[1][3]*aux[2][0] + aux[0][3]*aux[1][0]*aux[2][1]
        aI = aux[0][3]*aux[1][1]*aux[2][0] + aux[0][0]*aux[1][3]*aux[2][1] + aux[0][1]*aux[2][3]*aux[1][0]
        ra.append(aS-aI)
        s = s + "= " + format(aS-aI,'.2f') + "\n\n"
        
        s = s + "Solución del sistema\n"
        s = s + "X₁ = Δ₁/Δ = "+format(ra[1]/ra[0],'.2f') + "\n"
        s = s + "X₂ = Δ₂/Δ = "+format(ra[2]/ra[0],'.2f') + "\n"
        s = s + "X₃ = Δ₃/Δ = "+format(ra[3]/ra[0],'.2f') + "\n\n\n"
        
        s = s + "Método de la matriz inversa\n\n\nA ="
        mat_i = [[a_i[0],a_i[1],a_i[2],a_i[3]],[a_i[4],a_i[5],a_i[6],a_i[7]],[a_i[8],a_i[9],a_i[10],a_i[11]]]
        aux = [x*1 for x in mat_i]
        
        s = s + "\n" + '{:24}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1]),format(aux[i][2],'.2f'),"│")
        s = s + "\n" + '{:24}{:1}'.format("⌊","⌋") + "\n\nB ="
        s = s + "\n" + '{:9}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:6}{:3}'.format("│",format(aux[i][2],'.2f'),"│")  
        s = s + "\n" + '{:9}{:1}'.format("⌊","⌋") + "\n\nHallar matriz inversa:\n|A| ="
        
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),format(aux[i][2],'.2f'),"│")  
        aS = aux[0][0]*aux[1][1]*aux[2][2] + aux[0][1]*aux[1][2]*aux[2][0] + aux[0][2]*aux[1][0]*aux[2][1]
        aI = aux[0][2]*aux[1][1]*aux[2][0] + aux[0][0]*aux[1][2]*aux[2][1] + aux[0][1]*aux[1][0]*aux[2][2]
        det = aS-aI
        s = s + "= " + format(det,'.2f') + "\n\nAdj(A) ="

        aux[0][0] =  mat_i[1][1]*mat_i[2][2]-mat_i[1][2]*mat_i[2][1]
        aux[1][0] = (mat_i[0][1]*mat_i[2][2]-mat_i[0][2]*mat_i[2][1])*-1
        aux[2][0] =  mat_i[0][1]*mat_i[1][2]-mat_i[0][2]*mat_i[1][1]
        aux[0][1] = (mat_i[1][0]*mat_i[2][2]-mat_i[1][2]*mat_i[2][0])*-1
        aux[1][1] =  mat_i[0][0]*mat_i[2][2]-mat_i[0][2]*mat_i[2][0]
        aux[2][1] = (mat_i[0][0]*mat_i[1][2]-mat_i[0][2]*mat_i[1][0])*-1
        aux[0][2] =  mat_i[1][0]*mat_i[2][1]-mat_i[1][1]*mat_i[2][0]
        aux[1][2] = (mat_i[0][0]*mat_i[2][1]-mat_i[0][1]*mat_i[2][0])*-1
        aux[2][2] =  mat_i[0][0]*mat_i[1][1]-mat_i[0][1]*mat_i[1][0]

        s = s + "\n" + '{:24}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),format(aux[i][2],'.2f'),"│")  
        s = s + "\n" + '{:24}{:1}'.format("⌊","⌋") + "\n\nAdj(A)ᵗ ="
        
        s = s + "\n" + '{:24}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format(aux[0][i],'.2f'),format(aux[1][i],'.2f'),format(aux[2][i],'.2f'),"│")
        s = s + "\n" + '{:24}{:1}'.format("⌊","⌋") + "\n\n"
            
        s = s + "\nDado que: A⁻¹ = 1/|A| ∙ (Adj(A))ᵗ\nSe tiene:\nA⁻¹ ="
        s = s + "\n" + '{:24}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}'.format("│",format((aux[0][i])*(1/det),'.2f'),format((aux[1][i])*(1/det),'.2f'),format((aux[2][i])*(1/det),'.2f'),"│")
        s = s + "\n" + '{:24}{:1}'.format("⌊","⌋") + "\n\n"
        
        s = s + "Por consiguiente se calcula:\nX = A⁻¹ ∙ B"
        s = s + "\n" + '{:24}{:3}{:9}{:1}'.format("⌈","⌉","⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:3}{:3}{:6}{:3}'.format("│",format((aux[0][i])*(1/det),'.2f'),format((aux[1][i])*(1/det),'.2f'),format((aux[2][i])*(1/det),'.2f'),"│","│",format(mat_i[i][3],'.2f'),"│")
        s = s + "\n" + '{:24}{:3}{:9}{:1}'.format("⌊","⌋","⌊","⌋") + "\n\nX ="
        
        inv = []
        s = s + "\n" + '{:9}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            mfinal = 0
            for j in [0, 1, 2]:    
                mfinal = mfinal + ((aux[j][i])*(1/det))*mat_i[j][3]
            s = s + "\n" +'{:3}{:6}{:3}'.format("│",format(mfinal,'.2f'),"│")
            inv.append(mfinal)
        s = s + "\n" + '{:9}{:1}'.format("⌊","⌋") + "\n\n"
        
        s = s + "Solución del sistema\n"
        s = s + "X₁ = "+format(inv[0],'.2f') + "\n"
        s = s + "X₂ = "+format(inv[1],'.2f') + "\n"
        s = s + "X₃ = "+format(inv[2],'.2f') + "\n\n\n"
        
        self.resp.delete("1.0","end")
        self.resp.insert(1.0, s)
        self.checkSOL = True
        
    def printMaz(self, aux):
        s = ""
        s = s + '{:31}{:1}'.format("⌈","⌉")
        for i in [0, 1, 2]:
            s = s + "\n" +'{:3}{:7}{:7}{:7}{:7}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),format(aux[i][2],'.2f'),format(aux[i][3],'.2f'),"│")  
        s = s + "\n" + '{:31}{:1}'.format("⌊","⌋") + "\n\n"
        return s
        
def SetEc(p):
    strvar = ec.Ecua(p,False)
    return strvar.getVar()

def Corro(p, r, i):
    crr.Corroborar(p, r, i, False)
    
def Expr(p, s):
    exp.Exp(p, s)  