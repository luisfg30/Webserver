

from tkinter import *

class Tabela(Frame):
    def __init__(self, master,value_names,table_width,table_height):
        Frame.__init__(self, master)
        self.table_height=table_height
        self.table_width=table_width
        self.pack(side="top", fill="x")
        self.rows=0
        self.columns=len(value_names)
        self.value_names=value_names
 
        self._widgets = []
        self.current_row=0
        
        self.canvas = Canvas(self,width=table_width,height=self.table_height)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

        vscrollbar = Scrollbar(self)
        vscrollbar.grid(row=0, column=1, sticky=N+S)
        hscrollbar = Scrollbar(self, orient=HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky=E+W)

        self.canvas.yscrollcommand=vscrollbar.set,
        self.canvas.xscrollcommand=hscrollbar.set

        vscrollbar.config(command=self.canvas.yview)
        hscrollbar.config(command=self.canvas.xview)


        self.frame = Frame(self.canvas,bg="DarkGrey")

        new_row = []
        for j in range(self.columns):
            label = Label(self.frame, text=self.value_names[j],font=("Verdana 9 bold"),borderwidth=0, width=len(self.value_names[j]))
            label.grid(row=self.current_row, column=j, sticky="nsew", padx=1, pady=1)
            new_row.append(label)
        self._widgets.append(new_row)
        self.current_row+=1
        self.rows+=1
        
        self.canvas.create_window(0, 0, anchor=NW, window=self.frame)
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        
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
            label = Label(self.frame, text=values[j],borderwidth=0, width=10)
            label.grid(row=self.current_row, column=j, sticky="nsew", padx=1, pady=1)
            new_row.append(label)
        self._widgets.append(new_row)
        self.canvas.create_window(0, 0, anchor=NW, window=self.frame)
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
