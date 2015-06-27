import mysql.connector
import datetime

class AcessoSGBD(object):

    def __init__(self):
    
        self.date=datetime.datetime.now()
        self.date=str(self.date)
        
        self.cnx = mysql.connector.connect(user='root', password='peixeboi',
                                           host='127.0.0.1',
                                           database='webserver')
        
        
        
    def insertServer(self,maxConexoes,porta,download,timeOut):
    
        cursor = self.cnx.cursor()

        cursor.execute("SELECT MAX(idServer) FROM Server")
        
        id = cursor.fetchone()[0]
        
        if(id == None):
            id = 0
        else:
            id += 1
        
        cursor.execute("INSERT INTO `webserver`.`server`(`idServer`,`porta`,`maxConexoes`,`download`,`timeOut`,`data`) VALUES(%d, %d, %d, %s, %d,'%s');" % (id, porta, maxConexoes, download, timeOut, self.date))
        
        self.cnx.commit()
        
        cursor.close