from tkinter import *


class AbaIndicadores(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
    
        #labels 
        Label(self, text="Uso da Rede",background="blue").pack(side=LEFT,padx=100,fill=Y)
        Label(self, text="Uso de Memória",background="green").pack(side=LEFT,padx=100,fill=X)

       

        
   
     
        
        
     
