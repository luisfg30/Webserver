import datetime 

class Resposta(object):

    def __init__(self,status,server_version,data,contentType,contentSize):
        self.status=status
        self.server_version=server_version
        self.data=data
        self.contentType=contentType
        self.contentSize=contentSize
            
    def get_status(self):
        return self.status
    
    def get_server_version(self):
        return self.server_version
        
    def get_data(self):
        return self.data
        
    def get_contentType(self):
        return self.contentType
    
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
     
    def get_tipo(self):
        return self.tipo
    
    def get_protocolo(self):
        return self.versaoProtocoloHTTP
    
    def get_pagina(self):
        return self.paginaAcessada
    
    def get_data(self):
        return self.data
        
    def get_hostname(self):
        return self.hostname
    
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
        #self.print_reqs()
        self.bytesEnviados+=resposta.get_contentSize()
        self.paginasAcessadas.append(paginaAcessada)
        
    def print_self(self):
        print("\t Data= "+self.data+"\n\t IP de origem= "+str(self.IP)+":"+str(self.porta)) 
        self.print_reqs()
    
    def print_reqs(self):
        print("\n\t\t REQUISICOES:\n")
        for i in range(len(self.requisicoesRecebidas)):
            print("\n\t\t["+str(i)+"] pagina: "+self.requisicoesRecebidas[i].get_pagina())
            #print("\n\t\t  Resposta:\n"+str(self.requisicoesRecebidas[i].get_resposta().get_header()))
            
    def get_bytesRecebidos(self):
        return self.bytesRecebidos
    
    def get_bytesEnviados(self):
        return self.bytesEnviados
        
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