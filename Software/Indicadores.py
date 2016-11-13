import Server
import Conexao

class Indicadores(object):
    def __init__(self,server):
        self.my_server=server
        self.bytesEnviados=0
        self.bytesRecebidos=0
        self.listaConexoes=self.my_server.get_lista()
        self.listaPaginas=[]
        a=[" ",0]
        self.maiorAcesso=0
        self.listaPaginas.append(a)
        self.indexPag=0
        
    def get_bytesEnviados(self):
        return self.bytesEnviados
        
    def get_bytesRecebidos(self):
        return self.bytesRecebidos
        
    def add_pagina(self,pagina):
        existe=0
        for i in range (len(self.listaPaginas)):
            if self.listaPaginas[i][0]==pagina:
                self.listaPaginas[i][1]+=1  #caso a pagina ja exista na lista, apenas soma um acesso
                existe=1
            else:
                exitse=0
        if existe==0:        
            self.listaPaginas.append([pagina,1]) #caso percorra a lista e a pagina nao exista, adiciona ela com um acesso    
                
    def get_pagMaisAcessada(self):
        for i in range (len(self.listaPaginas)):
            if self.listaPaginas[i][1]>self.maiorAcesso:
                self.indexPag=i
                self.maiorAcesso=self.listaPaginas[i][1]
        return  self.listaPaginas[self.indexPag][0]   #retorna o valor indicado pelo indice 
    
    def atualizaValores(self):
        somaEnv=0
        somaRec=0
        for i in range (len(self.listaConexoes)):
            somaRec+=self.listaConexoes[i].get_bytesRecebidos()
            somaEnv+=self.listaConexoes[i].get_bytesEnviados()
        
        try:
            self.bytesRecebidos=somaRec/len(self.listaConexoes)
        except ZeroDivisionError:
            self.bytesRecebidos=0
            
        try:
            self.bytesEnviados=somaEnv/ len(self.listaConexoes)
        except ZeroDivisionError:
            self.bytesEnviados=0
        
        self.my_server.get_JanelaPrincipal().get_abaIndicadores().atualizaCampos(self.bytesRecebidos,self.bytesEnviados,self.get_pagMaisAcessada(),self.maiorAcesso)    
        #print("\nLISTA DE PAGINAS\n")
        #print(self.listaPaginas)
        