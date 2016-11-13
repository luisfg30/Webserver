from tkinter import *
import Tabela
import AcessoSGBD

class AbaBD(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.my_AcessoSGBD=AcessoSGBD.AcessoSGBD()
        
    def createWidgets(self):
        
       Label(self, text="    Consultar    ").grid(row=0, column=0)
        
       self.server = Button(self, text="Servers", command=self.queryServer)
       self.server.grid(row=0, column=1)
       
       self.conexoes = Button(self, text="Conexões", command=self.queryConexoes)
       self.conexoes.grid(row=0, column=3)
       
       self.conexoes = Button(self, text="Requisicoes", command=self.queryRequisicoes)
       self.conexoes.grid(row=0, column=5)
       
       self.conexoes = Button(self, text="Repostas", command=self.queryRespostas)
       self.conexoes.grid(row=0, column=7)
        
    def queryServer(self):
        
        columns=["ID","Porta","MaxConexoes", "Download", "Time Out", "      Data          ", "Pagina mais acessada", "Bytes enviados", "Bytes recebidos"]
        
        tabela=Tabela.Tabela(self,columns,750,400)
        tabela.grid(row=3, column=1, columnspan=10, sticky=(N,S,W,E))
        
        results = self.my_AcessoSGBD.queryServer()     
        
        for row in results:                
            tabela.insert_row(row)
        
    def queryConexoes(self):
    
        columns=["ID","ID_Server","   IP   ", "Porta", "      Data          ", "Bytes enviados", "Bytes recebidos"]

        tabela=Tabela.Tabela(self,columns,750,400)
        tabela.grid(row=3, column=1, columnspan=10, sticky=(N,S,W,E))
        
        results = self.my_AcessoSGBD.queryConexao()     
        
        for row in results:                
            tabela.insert_row(row)
            
    def queryRequisicoes(self):
    
        columns=["ID","ID_Conexao","Tipo", "Pagina", "Versão HTTP", "Hostname","      Data          "]

        tabela=Tabela.Tabela(self,columns,750,400)
        tabela.grid(row=3, column=1, columnspan=10, sticky=(N,S,W,E))
        
        results = self.my_AcessoSGBD.queryRequisicao()     
        
        for row in results:                
            tabela.insert_row(row)

    def queryRespostas(self):
    
        columns=["ID","ID_Requisicao","   Status   ", "    Server Version    ", "   Content Type   ", "Content Size","     Data      "]

        tabela=Tabela.Tabela(self,columns,750,400)
        tabela.grid(row=3, column=1, columnspan=10, sticky=(N,S,W,E))
        
        results = self.my_AcessoSGBD.queryResposta()     
        
        for row in results:                
            tabela.insert_row(row)