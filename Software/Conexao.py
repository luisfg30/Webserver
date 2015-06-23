import datetime 
class Conexao(object):

    def __init__(self,porta,IP,download):
        date=datetime.datetime.now()
        self.data=str(date)
        self.porta=porta
        self.IP=IP
        self.download=download
        #print apenas para mostrar que recebeu os parametros
        print("\nCONEXAO CRIADA\n Data:"+self.data+"\n Porta"+str(self.porta)+"\n IP:"+str(self.IP)+"\n Enable Download:"+str(self.download))    

    def get_data(self):
        return data
    
    def get_porta(self):
        return self.porta
        
    def get_IP(self):
        return self.IP
        
    def get_download(self):
        return self.download