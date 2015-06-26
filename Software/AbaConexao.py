from tkinter import *
from tkinter import ttk
import Server

class AbaConexao(Frame):
    def __init__(self, master, server):
        Frame.__init__(self, master)
        self.my_server=server
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        Label(self, text="     ").grid(row=0, column=0)
    
        Label(self, text="IP da conexão").grid(row=1, columnspan=3)
        
        Label(self, text="Requisições realizadas").grid(row=2, column=4)
        
        Label(self, text="     ").grid(row=1, column=3)
        
        self.conDetails = Text(self, width=65, height=1)
        self.conDetails.grid(row=1, column=4)
        
        self.conListBox = Listbox(self, height=25)
        self.conListBox.grid(row=2, column=1, sticky=(N,S,W,E))
        self.conListBox.bind('<<ListboxSelect>>', self.showConection)
        self.current = self.conListBox.curselection()    
        
        sList = ttk.Scrollbar(self, orient=VERTICAL, command=self.conListBox.yview)
        sList.grid(row=2, column=2, sticky=(N,S))
        self.conListBox['yscrollcommand'] = sList.set
               
        self.updateList()
        
    def showConection(self, *args):
                    
        self.conDetails.delete(1.0, END)
        
        current = self.conListBox.curselection()[0]
        
        self.conDetails.insert(INSERT, "IP: "+self.my_server.listaConexoes[current].get_IP()+" - Porta: "+str(self.my_server.listaConexoes[current].get_porta())+" - Data: "+self.my_server.listaConexoes[current].get_data())
            
    def updateList(self):
    
        self.conListBox.delete(0, END)
        
        for i in range(len(self.my_server.listaConexoes)):
            self.conListBox.insert('end', self.my_server.listaConexoes[i].get_IP())
    
        self.showConection
        
    
    
