import Conexao
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPParser(BaseHTTPRequestHandler):

    def do_GET(self):
        print("\nServer recebeu do browser: \n"+self.requestline+"\n"+str(self.headers))
        
        if self.path=="/": #homepage
            fpath="pages/index.html"   
        else:
            fpath="pages/"+self.path[1:] #apenas para guardar as paginas em pastas separadas
        print("\n PATH:"+self.path+ "--FPTAH:"+fpath)
        
        if fpath.endswith(".html"):
                mimetype='text/html'    
        elif fpath.endswith(".jpg"):
                mimetype='image/jpg'
                
        elif fpath.endswith(".gif"):
                mimetype='image/gif'
                
        elif fpath.endswith(".js"):
                mimetype='application/javascript'
                
        elif fpath.endswith(".css"):
                mimetype='text/css'
        else:
                mimetype='application/octet-stream' #unnkow type
                
        content=bytes(0)        
        try:		
				#Open the static file requested and send it
                f = open(fpath,"rb") 
                content=f.read()
                #print("\n CONTENT: \n"+content)
                f.close()
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.send_header('Content-Length:',len(content))
                self.end_headers()
                self.wfile.write(content)
                #self.wfile.write(bytes(content,"utf-8"))
                status=" 200 OK\n"
            
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
            status=" 404 Not Found\n"    
            
        respHeader=self.request_version+status+"Server: "+self.server_version+" "+self.sys_version+"\n"+self.date_time_string(None)+"\nContent-type: "+mimetype+"\nContent-Length:"+str(len(content))
        r=Conexao.Resposta(respHeader,len(content))    
        
        print("\n CLOSE CONNECTION: "+str(self.close_connection))
        #self.close_connection       
        
        print("\n SERVER RESPONDEU: \n"+respHeader)
        
        print("\n IP QUE VAI PARA A FUNCAO:"+self.client_address[0]+str(type(self.client_address[0])))
        index=self.server.servidor.procura_conexao(self.client_address[0])
        print("\nINDEX: "+str(index))
        if index == -1: # conexao ainda nao existe
            c=Conexao.Conexao(self.client_address[0],self.client_address[1],self.date_time_string(None))
            c.nova_requisicao(len(str(self.headers)),self.command,self.path,self.request_version,self.server.servidor.get_hostname,self.date_time_string(None),r)
            
            self.server.servidor.get_lista().append(c)
        else: #conexao ja existe
           self.server.servidor.nova_requisicao(index,len(str(self.headers)),self.command,self.path,self.request_version,self.server.servidor.get_hostname,self.date_time_string(None),r)
        
        self.server.servidor.print_conexoes()    
        
     
class customServer(HTTPServer):
        def __init__(self,servidor,server_address,parser):
            super(customServer,self).__init__(server_address,parser)
            self.servidor=servidor
            
class Server(object):

    def __init__(self,maxConexoes,IP,porta,timeOut,download):
        self.hostname=IP
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        self.listaConexoes=[]  
        #print apenas para mostrar que recebeu os parametros, depois a construtora ja inicia o servidor
        print("\nPARAMETROS SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))  
        
        self.start_server()
        
    def procura_conexao(self,IP):
        if len(self.listaConexoes)==0: #lista vazia
            return -1
        else:    
            for i in range(len(self.listaConexoes)):
                if self.listaConexoes[i].get_IP()==IP :
                    return i# retorna o indice da conexao
                else:
                    return -1 #retorna -1 se a conexao nao existe
    
    def print_conexoes(self):
        print("\n CONEXOES: ")
        for i in range(len(self.listaConexoes)):
            print("\n ["+str(i)+"] ")
            self.listaConexoes[i].print_self()
    
    def get_porta(self):
        return self.porta
        
    def get_maxConexoes(self):
        return self.maxConexoes
        
    def get_download(self): 
        return self.download
        
    def get_timeOut(self):
        return self.timeOut
        
    def get_hostname(self):
        return self.hostname
        
    def get_conexao(self,index):
        return self.listaConexoes[index]
    
    def get_lista(self):
        return self.listaConexoes
        
    def nova_conexao(self,IP,porta,data):
        c=Conexao.Conexao(IP,porta,data)
        self.listaConexoes.append(c)
        
    def nova_requisicao(self,index,bytes,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data,resposta):
        self.listaConexoes[index].nova_requisicao(bytes,tipo,paginaAcessada,versaoProtocoloHTTP,hostname,data,resposta)
        
    def restart_server(self):
        
            if len(self.listaConexoes)==0:
                print("\n Nenhuma conexao para salvar")
            else:
                for i in range(len(self.listaConexoes)):
                    print("\n SalvarConexao na classe SGBD para a conexao: "+self.listaConexoes[i].get_IP())
            self.listaConexoes.clear()
            #desse modo fica varios servers em paralelo O.0, tem que fechar o anterior
            self.start_server()
    def set_parametros(self,maxConexoes,ip,porta,timeOut,download):  
        self.hostname=ip
        self.maxConexoes=maxConexoes
        self.porta=porta
        self.timeOut=timeOut
        self.download=download
        print("\n PARAMETROS SERVER\n Max Conexoes:"+str(self.maxConexoes)+"\n Porta:"+str(self.porta)+"\n Time Out:"+str(self.timeOut)+"\n Enable Download:"+str(self.download))
    def start_server(self):
        self.mt= mainThread(self,self.maxConexoes,self.porta,self.timeOut,self.download)

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