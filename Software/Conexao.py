import datetime 

class Resposta(object):
    def __init__(self,header,content):
        self.header=header
        self.content=content
        
    def get_header(self):
        return self.header
     
    def get_content(self):
        return self.content

class Requisicao(object):
    def __init__(self,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data):
        self.tipo=tipo
        self.paginaAcessada=paginaAcessada
        self.versaoProtocoloHTTP=versaoProtocoloHTTP
        self.hostname=hostname
        self.data=data
        self.respostas=[]
    def nova_resposta(self,header,content):
        resp= Resposta(header,content)
        self.respostas.append(resp)
    
    def get_pagina(self):
        return self.paginaAcessada
        
    def get_resposta(self,index):
        return self.respostas[index]
        
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

    def nova_requisicao(self,bytes,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data):
        self.bytesRecebidos+=bytes
        self.tempoInativo=0
        req=Requisicao(tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data)
        self.requisicoesRecebidas.append(req)
        self.print_reqs()
        self.paginasAcessadas.append(paginaAcessada)
        
    def print_self(self):
        print("\t Data= "+self.data+"\n\t IP de origem= "+str(self.IP)+":"+str(self.porta)) 
    
    def print_reqs(self):
        print("\n\t REQUISICOES:\n")
        for i in range(len(self.requisicoesRecebidas)):
            print("\n\t["+str(i)+"] pagina: "+self.requisicoesRecebidas[i].get_pagina())
        
    def nova_resposta(self,bytes,reqIndex,header,content):
        self.bytesEnviados+=bytesEnviados
        self.requisicoesRecebidas[reqIndex].nova_resposta(header,content)
        
    def get_data(self):
        return self.data
    
    def get_porta(self):
        return self.porta
        
    def get_IP(self):
        return self.IP
        
    def get_download(self):
        return self.download