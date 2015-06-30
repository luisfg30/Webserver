import Conexao
import threading
import time
import AcessoSGBD
from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPParser(BaseHTTPRequestHandler):

    def do_GET(self):
        print("\nServer recebeu do browser: \n"+self.requestline+"\n"+str(self.headers))
        index=self.server.servidor.procura_conexao(self.client_address[0],self.client_address[1],self.date_time_string(None))
        print("\nINDEX: "+str(index))
        if index == -1: # conexao ainda nao existe
            self.server.servidor.nova_conexao(self.client_address[0],self.client_address[1],self.date_time_string(None))
            self.server.servidor.nova_requisicao(len(self.server.servidor.get_lista())-1,len(str(self.headers)),self.command,self.path,self.request_version,self.server.servidor.get_hostname,self.date_time_string(None))
        else: #conexao ja existe
           self.server.servidor.nova_requisicao(index,len(str(self.headers)),self.command,self.path,self.request_version,self.server.servidor.get_hostname,self.date_time_string(None))
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        self.server.servidor.print_conexoes()
     
class customServer(HTTPServer):
        def __init__(self,servidor,server_address,parser):
            super(customServer,self).__init__(server_address,parser)
            self.servidor=servidor
            
class Server(object):

    def __init__(self,maxConexoes,porta,timeOut,download):
        self.hostname="192.168.1.6"
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        self.listaConexoes=[]

        self.my_AcessoSGBD=AcessoSGBD.AcessoSGBD()
        
        #print apenas para mostrar que recebeu os parametros, depois a construtora ja inicia o servidor
        print("\nPARAMETROS SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))  
        
        self.start_server()
        self.save_server()
        
    def procura_conexao(self,IP,porta,data):
        if len(self.listaConexoes)==0: #lista vazia
            return -1
        else:    
            for i in range(len(self.listaConexoes)):
                if self.listaConexoes[i].get_IP()==IP :
                    return i# retorna o indice da conexao
        
        return -1 #retorna -1 se a conexao nao existe
    
    def print_conexoes(self):
        print("\n CONEXOES: ")
        for i in range(len(self.listaConexoes)):
            print("\n ["+str(i)+"] ")
            self.listaConexoes[i].print_self()
    
    def get_porta(self):
        return self.porta
    
    def get_hostname(self):
        return self.hostname
    def get_conexao(self,index):
        return self.listaConexoes[index]
    
    def get_lista(self):
        return self.listaConexoes
        
    def nova_conexao(self,IP,porta,data):
        c=Conexao.Conexao(IP,porta,data)
        self.listaConexoes.append(c)
        
    def nova_requisicao(self,index,bytes,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data):
        self.listaConexoes[index].nova_requisicao(bytes,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data)
        
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
        self.mt= mainThread(self,self.maxConexoes,self.porta,self.timeOut,self.download)
    
    def save_server(self):
        self.my_AcessoSGBD.insertServer(self.porta,self.maxConexoes,self.download,self.timeOut)
    
class mainThread(threading.Thread):
    def __init__(self,servidor,maxConexoes,porta,timeOut,download):
        self.servidor=servidor
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        threading.Thread.__init__(self)
        self.start()
        
    def run(self):
        server_address=(self.servidor.hostname, self.porta)
        myServer = customServer(self.servidor,server_address, HTTPParser)
        print(time.asctime(), "Server Starts - %s:%s" % (self.servidor.hostname, self.porta))
        myServer.serve_forever()