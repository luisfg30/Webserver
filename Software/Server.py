import Conexao

class Server(object):

    def __init__(self,maxConexoes,porta,timeOut,download):
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        self.listaConexoes=[]  
       
        #print apenas para mostrar que recebeu os parametros, depois a construtora ja inicia o servidor
        print("\nSTART SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))  
        
        self.test_method()

    def test_method(self):
         c=Conexao.Conexao(8080,"192.168.1.1",True)
         self.listaConexoes.append(c)
         print("\n Lista de conexoes:")
         for i in range(len(self.listaConexoes)):
            print("\n " +self.listaConexoes[i].get_IP())  