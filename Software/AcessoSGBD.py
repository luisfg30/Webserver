import mysql.connector
import datetime

class AcessoSGBD(object):

    def __init__(self):
    
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        self.cnx = mysql.connector.connect(user='root', password='peixeboi',
                                           host='127.0.0.1',
                                           database='webserver')

                                           
    def insertServer(self,server):
    
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        porta = server.get_porta()
        maxConexoes = server.get_maxConexoes()
        download = server.get_download()
        timeOut = server.get_timeOut()
        
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idServer) FROM Server")
        
        id = cursor.fetchone()[0]
        
        if(id == None):
            id = 0
        else:
            id += 1
        
        cursor.execute("INSERT INTO `webserver`.`server`(`idServer`,`porta`,`maxConexoes`,`download`,`timeOut`,`data`) VALUES(%d, %d, %d, %s, %d,'%s');" % (id, porta, maxConexoes, download, timeOut, self.date))
        
        self.cnx.commit()
        
        cursor.close()
        
    def queryServer(self):
        
        cursor = self.cnx.cursor()
        
        cursor.execute("SELECT S.idServer, S.data, I.pagMaisAcessada, I.bytesEnviados, I.bytesRecebidos, S.porta, S.maxConexoes, S.download, S.timeOut FROM server S LEFT OUTER JOIN indicadores I on S.idServer = I.idServer ORDER BY S.idServer")
        
        results = cursor.fetchall()
        
        self.cnx.commit()
        
        cursor.close()
        
        return results
        
    def insertConexao(self, conexao):
        
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        IP = conexao.get_IP()
        porta = conexao.get_porta()
        bytesEnviados = conexao.get_bytesEnviados()
        bytesRecebidos = conexao.get_bytesRecebidos()
        
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idServer) FROM Server")
        
        idServer = cursor.fetchone()[0]
        
        cursor.execute("SELECT MAX(idConexao) FROM conexao")
        
        idConexao = cursor.fetchone()[0]
        
        if(idConexao == None):
            idConexao = 0
        else:
            idConexao += 1
               
        cursor.execute("INSERT INTO `webserver`.`conexao`(`idConexao`,`idServer`,`IP`,`porta`,`data`,`bytesEnviados`,`bytesRecebidos`)VALUES (%d, %d, '%s', %d, '%s', %d, %d);" % (idConexao,idServer,IP,porta,self.date,bytesEnviados,bytesRecebidos))
        
        self.cnx.commit()
        
        cursor.close()
        
    def queryConexao(self):
        
        cursor = self.cnx.cursor()
        
        cursor.execute("SELECT * FROM conexao")
        
        results = cursor.fetchall()
        
        self.cnx.commit()
        
        cursor.close()
                
        return results
      
    def insertRequisicao(self, requisicao):
        
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        tipo = requisicao.get_tipo()
        pagina = requisicao.get_pagina()
        versaoHTTP = requisicao.get_protocolo()
        hostname = requisicao.get_hostname()
        
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idConexao) FROM conexao")
        
        idConexao = cursor.fetchone()[0]
        
        cursor.execute("SELECT MAX(idRequisicao) FROM requisicao")
        
        idRequisicao = cursor.fetchone()[0]
        
        if(idRequisicao == None):
            idRequisicao = 0
        else:
            idRequisicao += 1
               
        cursor.execute("INSERT INTO `webserver`.`requisicao`(`idRequisicao`,`idConexao`,`tipo`,`pagina`,`versaoHTTP`,`hostname`, `data`)VALUES (%d, %d, '%s', '%s', '%s', '%s', '%s');" % (idRequisicao,idConexao,tipo,pagina,versaoHTTP,hostname,self.date))
        
        self.cnx.commit()
        
        cursor.close()
        
    def queryRequisicao(self):
        
        cursor = self.cnx.cursor()
        
        cursor.execute("SELECT * FROM requisicao")
        
        results = cursor.fetchall()
        
        self.cnx.commit()
        
        cursor.close()
                
        return results

        
    
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idServer) FROM Server")
        
        id = cursor.fetchone()[0]
        
        if(id == None):
            id = 0
        else:
            id += 1
        
        cursor.execute("INSERT INTO `webserver`.`server`(`idServer`,`porta`,`maxConexoes`,`download`,`timeOut`,`data`) VALUES(%d, %d, %d, %s, %d,'%s');" % (id, porta, maxConexoes, download, timeOut, self.date))
        
        self.cnx.commit()
        
        cursor.close()
    
    def insertResposta(self, resposta):
        
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        status = resposta.get_status()
        serverVersion = resposta.get_server_version()
        contentType = resposta.get_contentType()
        contentSize = resposta.get_contentSize()
        
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idRequisicao) FROM requisicao")
        
        idRequisicao = cursor.fetchone()[0]
        
        cursor.execute("SELECT MAX(idResposta) FROM resposta")
        
        idResposta = cursor.fetchone()[0]
        
        if(idResposta == None):
            idResposta = 0
        else:
            idResposta += 1
               
        cursor.execute("INSERT INTO `webserver`.`resposta`(`idResposta`,`idRequisicao`,`status`,`serverVersion`,`contentType`,`contentSize`, `data`)VALUES (%d, %d, '%s', '%s', '%s', %d, '%s');" % (idResposta,idRequisicao,status,serverVersion,contentType,contentSize,self.date))
        
        self.cnx.commit()
        
        cursor.close()
        
    def queryResposta(self):
        
        cursor = self.cnx.cursor()
        
        cursor.execute("SELECT * FROM resposta")
        
        results = cursor.fetchall()
        
        self.cnx.commit()
        
        cursor.close()
                
        return results
    
    def insertIndicadores(self, indicadores):
        
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        bytesEnviados = indicadores.get_bytesEnviados()
        bytesRecebidos = indicadores.get_bytesRecebidos()
        pagMaisAcessada = indicadores.get_pagMaisAcessada()
        
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idServer) FROM server")
        
        idServer = cursor.fetchone()[0]
        
        cursor.execute("SELECT MAX(idIndicadores) FROM indicadores")
        
        idIndicadores = cursor.fetchone()[0]
        
        if(idIndicadores == None):
            idIndicadores = 0
        else:
            idIndicadores += 1
               
        cursor.execute("INSERT INTO `webserver`.`indicadores`(`idIndicadores`,`idServer`,`pagMaisAcessada`,`bytesEnviados`,`bytesRecebidos`)VALUES (%d, %d, '%s', %f, %f);" % (idIndicadores,idServer,pagMaisAcessada,bytesEnviados,bytesRecebidos))
        
        self.cnx.commit()
        
        cursor.close()
