# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:04:21 2021

@author: M
"""
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as font
from tkinter import messagebox
import ecua as ec
import corre as crr
import export as exp

class DosScreen(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Sistema de 2x2")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        self.configure(background='#8fd8d8')
        self.inn = []; self.rescorr = [] 
        self.valy1 = []; self.valy2 = []
        self.valx = range(-10, 10)    
        self.checkIN  = False
        self.checkSOL = False

        self.contenido = tk.Frame(self, bg="#8fd8d8")
        self.result = tk.Label(self.contenido, bg="#8fd8d8", font=font.Font(size=15), text='Ecuación', padx=30, pady=5, width=50)
        self.result.grid(row=0,column=0,columnspan=2)    
        
        freso = tk.Frame(self.contenido)
        self.resp = tk.Text(freso, bg="#d1eeee", height=20, width=35) # anchor="nw"
        self.resp.grid(row=0,column=0)
        self.sresp = "Resultado..."
        self.resp.insert(tk.INSERT, self.sresp)
        scroll = tk.Scrollbar(freso, orient='vertical', command=self.resp.yview)
        scroll.grid(row=0,column=1, sticky="ns")
        self.resp['yscrollcommand'] = scroll.set
        freso.grid(row=1,column=0, padx=(3,1), pady=4)
        
        relleno = tk.Frame(self.contenido, height=300, width=300)
        relleno.grid(row=1,column=1, padx=(2,1), pady=4)
        
        self.contenido.grid(row=0, column=0)
        
        tombos = tk.Frame(self, bg="#8fd8d8")
        ecuacion = tk.Button(tombos, bg="#528b8b", fg="white", text="Ecuación", command=self.setEc)
        ecuacion.grid(row=0,column=0, padx=20, pady=10)
        calcular = tk.Button(tombos, bg="#528b8b", fg="white", text="Calcular", command=self.matplotCanvas)
        calcular.grid(row=1,column=0, padx=20, pady=10)
        
        export = tk.Button(tombos, bg="#66cccc", text="Exportar", command=self.setExp)
        export.grid(row=2,column=0, padx=20, pady=10)
        corrob = tk.Button(tombos, bg="#66cccc", text="Corroborar", command=self.corroborar)
        corrob.grid(row=3,column=0, padx=20, pady=10)
        volver = tk.Button(tombos, bg="black", fg="white", text="Volver", command=self.volver)
        volver.grid(row=4,column=0, columnspan=2, padx=20, pady=10)
        
        tombos.grid(row=0,column=1)
        
        
        self.parent.withdraw()

    def volver(self):
        self.parent.deiconify()
        self.destroy()
        
    def setEc(self):
        a = SetEc(self.parent)
        self.valy1.clear()
        self.valy2.clear()
        self.result.configure(text=str(a[0])+"X₁ + "+str(a[1])+"X₂ = "+str(a[2])+"\n"+str(a[3])+"X₁ + "+str(a[4])+"X₂ = "+str(a[5]))
        for i in self.valx:
            try:self.valy1.append(((a[2]-a[0]*i)/a[1]))
            except:self.valy1.append(0)
            try:self.valy2.append(((a[5]-a[3]*i)/a[4]))
            except:self.valy2.append(0)
        self.inn = a 
        self.checkIN  = True
        self.checkSOL = False         
        
    def setExp(self):
        if self.checkSOL:            
            Expr(self.parent, ("Sistema 2x2\n\n\n\n" + self.resp.get('1.0', 'end-1c')))
        else:
            messagebox.showinfo(message="La exportación se debe hacer después\nde que se haya resuelto algún problema.", title="Alerta")
            
    def corroborar(self):
        if self.checkSOL:
            Corro(self.parent, self.rescorr, self.inn)
        else:
            messagebox.showinfo(message="La corroboración se debe hacer después\nde que se haya resuelto algún problema.", title="Alerta")
        
    def matplotCanvas(self):
        if self.checkIN:
            m = Figure(figsize=(3,3), dpi=100)
            yy = range(-15, 20)
            yx = [0 for i in yy]
            xx = range(-10, 15)
            xy = [0 for i in xx]
            x = m.add_subplot(1, 1, 1)
            x.plot(xx, xy, color="#000000")
            x.plot(yx,yy, color="#000000")
            x.plot(self.valx, self.valy1)
            x.plot(self.valx, self.valy2)
            x.grid(True)
            x.set_xlim([-10, 10])
            x.set_ylim([-10, 10])
    
            canvas = FigureCanvasTkAgg(m, self.contenido)
            canvas.get_tk_widget().grid(row=1, column=2)
            canvas._tkcanvas.grid(row=1, column=1, padx=2)
            
            self.resol()
        else:
            messagebox.showinfo(message="La solución y graficación se debe hacer después\nde que se haya ingresado un sistema de ecuaciones.", title="Alerta")            
        
    def resol(self):
        a_i = [float(x) for x in self.inn]
        s = "Método de Gauss\n\n\n"
        
        mat_i = [[a_i[0],a_i[1],a_i[2]],[a_i[3],a_i[4],a_i[5]]]
        aux = [x*1 for x in mat_i]
        
        if (aux[0][1] == 0 and aux[1][1] == 0 or 
            aux[0][0] == 0 and aux[1][0] == 0 and aux[0][1] == 0 and aux[1][1] == 0 or 
            aux[0][0] == 0 and aux[1][0] == 0):
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
        s = s + self.printMaz(aux)
        
        if aux[0][0]==0:
            s = s + "F₂ <=> F₁\n\n"
            for i in [0, 1, 2]:
                mat_i[1][i] = aux[0][i]
                mat_i[0][i] = aux[1][i]
        else:
            s = s + "F₂ = F₂ - ( "+format(aux[1][0],'.2f')+"/"+format(aux[0][0],'.2f')+" ) ∙ F₁\n\n"
            for i in [0, 1, 2]:
                mat_i[1][i] = aux[1][i] - (aux[1][0]/aux[0][0]) * aux[0][i]
        
        s = s + "Matriz escalonada:\n"
        s = s + self.printMaz(mat_i)
        
        s = s + "Solución del sistema:\n"
        s = s + "Si:        "+format(mat_i[1][1],'.2f')+"X₂ = "+format(mat_i[1][2],'.2f')+"\n"
        if mat_i[1][2]/mat_i[1][1] == 0:
            s = s + "Entonces:  X₂ = "+format(abs(mat_i[1][2]/mat_i[1][1]),'.2f')+"\n"
        else:
            s = s + "Entonces:  X₂ = "+format(mat_i[1][2]/mat_i[1][1],'.2f')+"\n"
        if (mat_i[0][2]-(mat_i[0][1]*(mat_i[1][2]/mat_i[1][1])))/mat_i[0][0] == 0:
            s = s + "Por ende:  X₁ = "+format(abs((mat_i[0][2]-(mat_i[0][1]*(mat_i[1][2]/mat_i[1][1])))/mat_i[0][0]),'.2f')+"\n\n\n"
        else:
            s = s + "Por ende:  X₁ = "+format((mat_i[0][2]-(mat_i[0][1]*(mat_i[1][2]/mat_i[1][1])))/mat_i[0][0],'.2f')+"\n\n\n"
        
        
        s = s + "Método de Gauss-Jordan\n\n\n"
        
        mat_i = [[a_i[0],a_i[1],a_i[2]],[a_i[3],a_i[4],a_i[5]]]
        
        s = s + "Matriz inicial:\n"
        s = s + self.printMaz(mat_i)
        
        #1
        s = s + "Primera iteración:\n"  
        aux = [x*1 for x in mat_i]
        if aux[0][0]==0:
            s = s + "F₂ <=> F₁\n\n"
            for i in [0, 1, 2]:
                mat_i[1][i] = aux[0][i]
                mat_i[0][i] = aux[1][i]
        else:
            s = s + "F₁ = F₁ / "+format(aux[0][0],'.2f')+"\n"
            for i in [0, 1, 2]:
                mat_i[0][i] = aux[0][i]/aux[0][0]      
        s = s + self.printMaz(mat_i)
        
        #2
        s = s + "Segunda iteración:\n"        
        aux = [x*1 for x in mat_i]        
        if aux[1][0]==0:
            s = s + "F₁ = F₁ / "+format(aux[0][0],'.2f')+"\n"
            for i in [0, 1, 2]:
                mat_i[0][i] = aux[0][i]/aux[0][0]
        else:
            s = s + "F₂ = F₂ - "+format(aux[1][0],'.2f')+" ∙ F₁\n"
            for i in [0, 1, 2]:
                mat_i[1][i] = aux[1][i] - aux[1][0]*aux[0][i]
        s = s + self.printMaz(mat_i)
        
        #3
        s = s + "Tercera iteración:\n"        
        aux = [x*1 for x in mat_i]
        if aux[1][0]==0:
            s = s + "F₁ = F₁ / "+format(aux[1][1],'.2f')+"\n"
            for i in [0, 1, 2]:
                mat_i[1][i] = aux[1][i]/aux[1][1]
        else:
            s = s + "F₂ = F₂ /"+format(aux[1][1],'.2f')+"\n"
            for i in [0, 1, 2]:
                mat_i[1][i] = aux[1][i]/aux[1][1]
        s = s + self.printMaz(mat_i)
        
        #4
        aux = [x*1 for x in mat_i]        
        for i in [0, 1, 2]:
            mat_i[0][i] = aux[0][i] - aux[0][1]*aux[1][i]
        s = s + "Cuarta iteración:\n"        
        s = s + "F₁ = F₁ - ("+format(aux[0][1],'.2f')+") ∙ F₂\n"
        s = s + self.printMaz(mat_i)
        
        if mat_i[0][2]==0:
            s = s + "Solución del sistema:\n    X₁ = "+format(abs(mat_i[0][2]),'.2f')+"\n"
        else:
            s = s + "Solución del sistema:\n    X₁ = "+format(mat_i[0][2],'.2f')+"\n"
        if mat_i[1][2]==0:
            s = s + "X₂ = "+format(abs(mat_i[1][2]),'.2f') + "\n\n\n"
        else:
            s = s + "X₂ = "+format(mat_i[1][2],'.2f') + "\n\n\n"
        self.rescorr.append(mat_i[0][2])
        self.rescorr.append(mat_i[1][2])
        
        #Δ
        s = s + "Regla de Cramer\n\n\nΔ "
        mat_i = [[a_i[0],a_i[1],a_i[2]],[a_i[3],a_i[4],a_i[5]]]
        aux = [x*1 for x in mat_i]

        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),"│")  
        s = s + "= " + format(aux[0][0]*aux[1][1]-aux[1][0]*aux[0][1],'.2f') + "\n\nΔ₁"
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[i][2],'.2f'),format(aux[i][1],'.2f'),"│")  
        s = s + "= " + format(aux[0][2]*aux[1][1]-aux[1][2]*aux[0][1],'.2f') + "\n\nΔ₂"
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][2],'.2f'),"│")  
        s = s + "= " + format(aux[0][0]*aux[1][2]-aux[1][0]*aux[0][2],'.2f') + "\n\n"
        
        s = s + "Solución del sistema\n"
        s = s + "X₁ = Δ₁/Δ = "+format(((aux[0][2]*aux[1][1]-aux[1][2]*aux[0][1])/(aux[0][0]*aux[1][1]-aux[1][0]*aux[0][1])),'.2f') + "\n"
        s = s + "X₂ = Δ₂/Δ = "+format(((aux[0][0]*aux[1][2]-aux[1][0]*aux[0][2])/(aux[0][0]*aux[1][1]-aux[1][0]*aux[0][1])),'.2f') + "\n\n\n"
        
        s = s + "Método de la matriz inversa\n\n\nA ="
        mat_i = [[a_i[0],a_i[1],a_i[2]],[a_i[3],a_i[4],a_i[5]]]
        aux = [x*1 for x in mat_i]
        
        s = s + "\n" + '{:15}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),"│")  
        s = s + "\n" + '{:15}{:1}'.format("⌊","⌋") + "\n\nB ="
        s = s + "\n" + '{:9}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:3}'.format("│",format(aux[i][2],'.2f'),"│")  
        s = s + "\n" + '{:9}{:1}'.format("⌊","⌋") + "\n\nHallar matriz inversa:\n|A| ="
        
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),"│")  
        s = s + "= " + format(aux[0][0]*aux[1][1]-aux[1][0]*aux[0][1],'.2f') + "\n\nAdj(A) ="
        
        aux[0][0] =   mat_i[1][1]
        aux[1][0] = -(mat_i[0][1])
        aux[0][1] =   mat_i[1][0]
        aux[1][1] = -(mat_i[0][0])
        s = s + "\n" + '{:15}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),"│")  
        s = s + "\n" + '{:15}{:1}'.format("⌊","⌋") + "\n\nAdj(A)ᵗ ="
        
        s = s + "\n" + '{:15}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format(aux[0][i],'.2f'),format(aux[1][i],'.2f'),"│")
        s = s + "\n" + '{:15}{:1}'.format("⌊","⌋") + "\n\n"
            
        det = aux[0][0]*aux[1][1]-aux[1][0]*aux[0][1]            
        s = s + "\nDado que: A⁻¹ = 1/|A| ∙ (Adj(A))ᵗ\nSe tiene:\nA⁻¹ ="
        s = s + "\n" + '{:15}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}'.format("│",format((aux[0][i])*(1/det),'.2f'),format((aux[1][i])*(1/det),'.2f'),"│")
        s = s + "\n" + '{:15}{:1}'.format("⌊","⌋") + "\n\n"
        
        s = s + "Por consiguiente se calcula:\nX = A⁻¹ ∙ B"
        s = s + "\n" + '{:15}{:3}{:9}{:1}'.format("⌈","⌉","⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:3}{:3}{:6}{:3}'.format("│",format((aux[0][i])*(1/det),'.2f'),format((aux[1][i])*(1/det),'.2f'),"│","│",format(mat_i[i][2],'.2f'),"│")
        s = s + "\n" + '{:15}{:3}{:9}{:1}'.format("⌊","⌋","⌊","⌋") + "\n\nX ="
        
        inv = []
        s = s + "\n" + '{:9}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            mfinal = 0
            for j in [0, 1]:    
                mfinal = mfinal + ((aux[j][i])*(1/det))*mat_i[j][2]
            s = s + "\n" +'{:3}{:6}{:3}'.format("│",format(mfinal,'.2f'),"│")
            inv.append(mfinal)
        s = s + "\n" + '{:9}{:1}'.format("⌊","⌋") + "\n\n"
        
        s = s + "Solución del sistema\n"
        if inv[0]==0:
            s = s + "X₁ = "+format(abs(inv[0]),'.2f') + "\n"
        else:
            s = s + "X₁ = "+format(-inv[0],'.2f') + "\n"
        if inv[1]==0:
            s = s + "X₂ = "+format(abs(inv[1]),'.2f') + "\n\n\n"
        else:
            s = s + "X₂ = "+format(inv[1],'.2f') + "\n\n\n"
        
        self.resp.delete("1.0","end")
        self.resp.insert(1.0, s)
        self.checkSOL = True
        
    def printMaz(self, aux):
        s = ""
        s = s + '{:21}{:1}'.format("⌈","⌉")
        for i in [0, 1]:
            s = s + "\n" +'{:3}{:6}{:6}{:6}{:3}'.format("│",format(aux[i][0],'.2f'),format(aux[i][1],'.2f'),format(aux[i][2],'.2f'),"│")  
        s = s + "\n" + '{:21}{:1}'.format("⌊","⌋") + "\n\n"
        return s
        
def SetEc(p):
    strvar = ec.Ecua(p,True)
    return strvar.getVar()
    
def Corro(p, r, i):
    crr.Corroborar(p, r, i, True)  
    
def Expr(p, s):
    exp.Exp(p, s)      