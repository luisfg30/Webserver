
class Server(object):

    def __init__(self,maxConexoes,porta,timeOut,download):
    
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        #print apenas para mostrar que recebeu os parametros, depois a construtora ja inicia o servidor
        print("\nSTART SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))    


        
        
#my_server= Server(10,20,30,True)        