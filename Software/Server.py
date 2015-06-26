import Conexao
import http.server
import socketserver
import threading

class Server(object):

    def __init__(self,maxConexoes,porta,timeOut,download):
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        self.listaConexoes=[]  
        #print apenas para mostrar que recebeu os parametros, depois a construtora ja inicia o servidor
        print("\nPARAMETROS SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))  
        
        self.test_method()
        self.start_server()

    def test_method(self):
    
         for i in range(0, 10):
            c=Conexao.Conexao(8000,"192.168.1.%d" % i,True)
            self.listaConexoes.append(c)
            
         print("\n Lista de conexoes:")
         for i in range(len(self.listaConexoes)):
            print("\n " +self.listaConexoes[i].get_IP())  
            
    def restart_server(self):
        
            if len(self.listaConexoes)==0:
                print("\n Nenhuma conexao para salvar")
            else:
                for i in range(len(self.listaConexoes)):
                    print("\n SalvarConexao na classe SGBD para a conexao: "+self.listaConexoes[i].get_IP())
            self.listaConexoes.clear()
            #desse modo fica varios servers em paralelo O.0, tem que fechar o anterior
            self.start_server()
            
    def set_parametros(self,maxConexoes,porta,timeOut,download):   
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        print("\n PARAMETROS SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))
        
    def start_server(self):
        self.mt= mainThread(self.maxConexoes,self.porta,self.timeOut,self.download)

class mainThread(threading.Thread):
    def __init__(self,maxConexoes,porta,timeOut,download):
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        threading.Thread.__init__(self)
        self.start()
        
    def run(self):
        self.Handler = http.server.SimpleHTTPRequestHandler

        self.httpd = socketserver.TCPServer(("", self.porta), self.Handler)

        print("serving at port", self.porta)
        self.httpd.serve_forever()