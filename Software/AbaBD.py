from tkinter import *
import Tabela

class AbaBD(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
    
       list2=["Data","Página","Tipo de Resuisição"]
       
       self.tabela=Tabela.Tabela(self,list2,700,400)
       self.tabela.pack(side="top", fill="x")
      
       list=["abc","def","ghi"]
       for i in range(50):
            self.tabela.insert_row(list)

       

        
   
     
        
        
     
