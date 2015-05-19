from tkinter import *
class Tabs(Frame):


    def __init__(self, parent):
        super(Tabs, self).__init__()

        self.parent = parent
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
        ####################
        self.curtab = None
        self.tabs = {}
        self.addTab("Conexões","#9999FF", "#4444FF")
        self.addTab("Indicadores","#FF9999", "#FF4444")
        self.addTab("Coonsulta BD","#99FF99", "#44FF44")
        self.addTab("Configurações","#FFFF99", "#FFFF44")
        ####################

        self.pack(fill=BOTH, expand=1, padx=5, pady=5)

    def addTab(self, name, color, activeColor):
        tabslen = len(self.tabs)
        if tabslen < 10:
            tab = {}
            btn = Button(self, text=name, command=lambda: self.raiseTab(tabslen), width=25, background=color, activebackground=activeColor)
            btn.grid(row=0, column=tabslen, sticky=W+E)

            textbox = Text(self.parent)
            textbox.grid(row=1, column=0, columnspan=4, rowspan=2, sticky=W+E+N+S, in_=self)
            textbox.insert(INSERT, name)
            
           # Y axis scroll bar
           #scrollby = Scrollbar(self, command=textbox.yview)
           # scrollby.grid(row=7, column=5, rowspan=2, columnspan=1, sticky=N+S+E)
           # textbox['yscrollcommand'] = scrollby.set

            tab['id']=tabslen
            tab['btn']=btn
            tab['txtbx']=textbox
            self.tabs[tabslen] = tab
            self.raiseTab(tabslen)

    def raiseTab(self, tabid):
        print("\nTab id: "+str(tabid))
        print("prevtab: "+str(self.curtab))
        if self.curtab!= None and self.curtab != tabid and len(self.tabs)>1:
            self.tabs[tabid]['txtbx'].lift(self)
            self.tabs[self.curtab]['txtbx'].lower(self)
        self.curtab = tabid
        print("curtab: "+str(self.curtab))
        
    


root = Tk()
root.geometry("750x500+100+100")
t = Tabs(root)
root.mainloop()

if __name__ == '__main__':
 main()