from tkinter import *


class AbaIndicadores(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.bytesEnviados=StringVar()
        self.bytesRecebidos=StringVar()
        self.pagina=StringVar()
        self.bytesEnviados.set('Média de Bytes Enviados: '+'0')
        self.bytesRecebidos.set('Média de Bytes Recebidos:'+'0')
        self.pagina.set('Página mais acessada:')
        self.createWidgets()
        
    def createWidgets(self):
    
        #labels 
        Label(self, textvariable=self.bytesRecebidos,background="white").pack(side=TOP,padx=100,fill=X)
        Label(self, textvariable=self.bytesEnviados,background="white").pack(side=TOP,padx=100,fill=X)
        Label(self, textvariable=self.pagina,background="white").pack(side=TOP,padx=100,fill=X)

    def atualizaCampos(self,bytesRec,bytesEnv,pagina,acessos):
        self.bytesRecebidos.set('Média de Bytes Recebidos:'+str(bytesRec))
        self.bytesEnviados.set('Média de Bytes Enviados: '+str(bytesEnv))
        self.pagina.set('Página mais acessada:'+pagina+'   Nº de acessos: '+str(acessos))
        self.update_idletasks()
   
     
        
        
     
