from tkinter import *
from tkinter import ttk
import Server
from random import randint

class AbaConexao(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        Label(self, text="     ").grid(row=0, column=0)
    
        Label(self, text="IP da conexão").grid(row=1, columnspan=3)
        
        Label(self, text="Requisições realizadas").grid(row=1, column=4)
        
        Label(self, text="               ").grid(row=1, column=3)
        
        self.conInfo = Text(self, width=60)
        self.conInfo.grid(row=2, column=4, sticky=(S+N+E+W))
        
        sInfo = ttk.Scrollbar(self, orient=VERTICAL, command=self.conInfo.yview)
        sInfo.grid(column=5, row=2, sticky=(N,S))
        self.conInfo['yscrollcommand'] = sInfo.set
        
        self.conListBox = Listbox(self, height=25)
        self.conListBox.grid(row=2, column=1, sticky=(N,S,W,E))
        self.conListBox.bind('<<ListboxSelect>>', self.showConection)
        self.current = self.conListBox.curselection()        
        
        sList = ttk.Scrollbar(self, orient=VERTICAL, command=self.conListBox.yview)
        sList.grid(row=2, column=2, sticky=(N,S))
        self.conListBox['yscrollcommand'] = sList.set
        
        for i in range(1,100):
            self.conListBox.insert('end', '192.168.100.%03d' % i)
        
        
    def showConection(self, *args):
        
        print(self.conListBox.curselection()[0])
            
        self.conInfo.delete(1.0, END)
        
        quantReq = randint(1,10)
        
        for x in range(1, quantReq):
            self.conInfo.insert(INSERT, "Requisicao %d\n\nData: %d:%d\nHora: %d:%d:%d\nBytes Enviados: %d\n\n\n" % (x, randint(0,23), randint(0,59), randint(1,30), randint(1,12), randint(2014,2015), randint(0,99999)))
    
    
    
    
    #def insertConection(self, C)


'''window = Tk()
window.geometry("400x200")
window.title("Aba Conexao")
app = AbaConexao(master=window)
app.mainloop()'''