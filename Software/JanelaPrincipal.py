from tkinter import *
import AbaConfig 
import AbaConexao
import AbaIndicadores
import AbaBD

class JanelaPrincipal(Frame):


    def __init__(self, master):
        super(JanelaPrincipal, self).__init__()

        self.master = master
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
        ####################
        self.curtab = None
        self.tabs = {}
        frame1= AbaBD.AbaBD()
        frame2=AbaConfig.AbaConfig()
        frame3=AbaConexao.AbaConexao()
        frame4=AbaIndicadores.AbaIndicadores()
        self.addTab("Conexões","#9999FF", "#4444FF",frame3)
        self.addTab("Indicadores","#FF9999", "#FF4444",frame4)
        self.addTab("Coonsulta BD","#99FF99", "#44FF44",frame1)
        self.addTab("Configurações","#FFFF99", "#FFFF44",frame2)
        ####################

        self.pack(fill=BOTH, expand=1, padx=5, pady=5)

    def addTab(self, name, color, activeColor,internal_frame):
        tabslen = len(self.tabs)
        if tabslen < 10:
            tab = {}
            btn = Button(self, text=name, command=lambda: self.raiseTab(tabslen), width=25, background=color, activebackground=activeColor)
            btn.grid(row=0, column=tabslen, sticky=W+E)

            
            #internal_frame= Abaconfig.AbaConfig()
            internal_frame.grid(row=1, column=0, columnspan=4, rowspan=2, sticky=W+E+N+S, in_=self)

            tab['id']=tabslen
            tab['btn']=btn
            tab['txtbx']=internal_frame
            self.tabs[tabslen] = tab
            self.raiseTab(tabslen)
    
    def changeColor(self,button):
        pass
    def raiseTab(self, tabid):
        #print("\nTab id: "+str(tabid))
        #print("prevtab: "+str(self.curtab))
        if self.curtab!= None and self.curtab != tabid and len(self.tabs)>1:
            self.tabs[tabid]['txtbx'].lift(self)
            self.tabs[self.curtab]['txtbx'].lower(self)
        self.curtab = tabid
        #print("curtab: "+str(self.curtab))
        
    




