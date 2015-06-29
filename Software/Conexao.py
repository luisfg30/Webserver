import datetime 

class Resposta(object):
    def __init__(self,header,contentSize):
        self.header=header
        self.contentSize=contentSize
        
    def get_header(self):
        return self.header
     
    def get_contentSize(self):
        return self.contentSize

class Requisicao(object):
    def __init__(self,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data,resp):
        self.tipo=tipo
        self.paginaAcessada=paginaAcessada
        self.versaoProtocoloHTTP=versaoProtocoloHTTP
        self.hostname=hostname
        self.data=data
        self.resposta=resp
    
    def get_pagina(self):
        return self.paginaAcessada
        
    def get_resposta(self):
        return self.resposta
        
class Conexao(object):

    def __init__(self,IP,porta,data):
        self.data=data
        self.porta=porta
        self.IP=IP
        self.bytesEnviados=0
        self.bytesRecebidos=0
        self.tempoInativo=0
        self.requisicoesRecebidas=[]
        self.paginasAcessadas=[]          

    def nova_requisicao(self,bytes,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data,resposta):
        self.bytesRecebidos+=bytes
        self.tempoInativo=0
        req=Requisicao(tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data,resposta)
        self.requisicoesRecebidas.append(req)
        self.print_reqs()
        self.paginasAcessadas.append(paginaAcessada)
        
    def print_self(self):
        print("\t Data= "+self.data+"\n\t IP de origem= "+str(self.IP)+":"+str(self.porta)) 
        self.print_reqs()
    
    def print_reqs(self):
        print("\n\t\t REQUISICOES:\n")
        for i in range(len(self.requisicoesRecebidas)):
            print("\n\t\t["+str(i)+"] pagina: "+self.requisicoesRecebidas[i].get_pagina())
            #print("\n\t\t  Resposta:\n"+str(self.requisicoesRecebidas[i].get_resposta().get_header()))
        
    def nova_resposta(self,bytes,reqIndex,header,content):
        self.bytesEnviados+=bytesEnviados
        self.requisicoesRecebidas[reqIndex].nova_resposta(header,content)
    
    def get_requisicoes(self):
        return self.requisicoesRecebidas
     
    def get_data(self):
        return self.data
    
    def get_porta(self):
        return self.porta
        
    def get_IP(self):
        return self.IP
        
    def get_download(self):
        return self.download