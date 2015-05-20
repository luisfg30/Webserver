from tkinter import *
class Tabela(Frame):

    def __init__(self,value_names ,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.value_names=value_names
        print(value_names)
    
        #scrollbar
        self.scrollbar = Scrollbar(self)
        # the table itself
        self.table=SimpleTable(self,self.value_names)
        self.table.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(side=LEFT, fill=Y)
        self.table.yscrollcommand = self.scrollbar.set
        self.scrollbar.config(command=self.table.yview)

 

        
    
    
class SimpleTable(Canvas):
    def __init__(self, parent,value_names):
        self.rows=0
        self.columns=len(value_names)
        # use black background so it "peeks through" to 
        # form grid lines
        Canvas.__init__(self, parent, background="black")
        self._widgets = []
        self.current_row=0
        
        for j in range(self.columns):
            self.grid_columnconfigure(j, weight=1)

        #add first line 
        new_row = []
        for j in range(self.columns):
            label = Label(self, text=value_names[j],font=("Verdana 9 bold"),borderwidth=0, width=len(value_names[j]))
            label.grid(row=self.current_row, column=j, sticky="nsew", padx=1, pady=1)
            new_row.append(label)
        self._widgets.append(new_row)
        self.current_row+=1
        self.rows+=1

    def set_cell(self, i, j, value):
        widget = self._widgets[i][j]
        widget.configure(text=value)
    
    def set_row(self,i,values):
        for j in range(len(values)):
            widget = self._widgets[i][j]
            widget.configure(text=values[j])   
            
    def insert_row(self,values):
        self.current_row+=1
        self.rows+=1
        new_row = []
        for j in range(len(values)):
            label = Label(self, text=values[j],borderwidth=0, width=10)
            label.grid(row=self.current_row, column=j, sticky="nsew", padx=1, pady=1)
            new_row.append(label)
        self._widgets.append(new_row)    



        


