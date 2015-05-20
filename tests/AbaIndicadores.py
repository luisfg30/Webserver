from tkinter import *


class AbaIndicadores(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        #spacing label
        Label(self, text="   ").grid(row=0, column=0)
    
        #labels and entry fields
        Label(self, text="Tempo médio de conexão:").grid(row=1, column=1)
        Label(self, text="Página mais acessada:").grid(row=2, column=1)
        Label(self, text="Média de Bytes:").grid(row=3, column=1)
 
       

        
   
     
        
        
     
