import tkinter as tk
import Server

class JanelaInicial(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        master.geometry("400x200")
        master.title("Janela Inicial")
        
    def createWidgets(self):
        #labels and entry fields
        tk.Label(self, text="Máximo de Conexões:").grid(row=0)
        tk.Label(self, text="Porta:").grid(row=1)
        tk.Label(self, text="Time Out(segundos):").grid(row=2)
 
        #default values
        self.v_eMaxC=500
        self.v_ePorta=8000
        self.v_eTime=300
        self.v_download=tk.StringVar()
        
        vcmd1 = self.register(self.validate_MaxC)  
        vcmd2 = self.register(self.validate_Porta) 
        vcmd3 = self.register(self.validate_Time) 
        
        self.eMaxC = tk.Entry(self,validate='focus', validatecommand=(vcmd1, '%P'))
        self.eMaxC.insert(0,str(self.v_eMaxC))
        self.ePorta = tk.Entry(self,validate='focus', validatecommand=(vcmd2, '%P'))
        self.ePorta.insert(0,str(self.v_ePorta))
        self.eTime = tk.Entry(self,validate='focus', validatecommand=(vcmd3, '%P'))
        self.eTime.insert(0,str(self.v_eTime))
        self.cDownload=tk.Checkbutton(self,text="Habilitar Download",variable=self.v_download,onvalue="True",offvalue="False")
        self.cDownload.var=self.v_download
        
        self.eMaxC.grid(row=0, column=1)
        self.ePorta.grid(row=1, column=1)
        self.eTime.grid(row=2, column=1)
        self.cDownload.grid(row=3, column=0)
        
        #buttons
        self.ok = tk.Button(self)
        self.ok["text"] = "Iniciar servidor"
        self.ok["command"] = self.start_server
        self.ok.grid(row=4)

        self.QUIT = tk.Button(self, text="SAIR", fg="red",
                                            command=window.destroy)
        self.QUIT.grid(row=4,column=1)
        

    def validate_MaxC(self, P):
        try:
                v=int(P)
                if v<1 or v>self.v_eMaxC:
                    v=self.v_eMaxC
                    self.eMaxC.delete(0,tk.END)
                    self.eMaxC.insert(0,str(self.v_eMaxC))
                return True
        except:
            self.eMaxC.delete(0,tk.END)
            self.eMaxC.insert(0,str(self.v_eMaxC))
            return False
     
    def validate_Porta(self,P):
            try:
                    v=int(P)
                    if v<1 or v>self.v_ePorta:
                        v=self.v_ePorta
                        self.ePorta.delete(0,tk.END)
                        self.ePorta.insert(0,str(self.v_ePorta))
                    return True
            except:
                self.ePorta.delete(0,tk.END)
                self.ePorta.insert(0,str(self.v_ePorta))
                return False
 
    def validate_Time(self,P):
        try:
                v=int(P)
                if v<1 or v>self.v_eTime:
                    v=self.v_eTime
                    self.eTime.delete(0,tk.END)
                    self.eTime.insert(0,str(self.v_eTime))
                return True
        except:
            self.eTime.delete(0,tk.END)
            self.eTime.insert(0,str(self.v_eTime))
            return False
            
    def start_server(self):
        self.validate_MaxC(self.eMaxC.get())
        self.validate_Porta(self.ePorta.get())
        self.validate_Time(self.eTime.get())
        my_server= Server.Server(int(self.eMaxC.get()),int(self.ePorta.get()),int(self.eTime.get()),self.v_download.get())   

window = tk.Tk()
app = JanelaInicial(master=window)
app.mainloop()