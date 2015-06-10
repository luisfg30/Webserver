from tkinter import *
import JanelaInicial


window = Tk()
window.geometry("400x200")
window.title("Janela Inicial")        
        
app = JanelaInicial.JanelaInicial(master=window)
app.mainloop()     