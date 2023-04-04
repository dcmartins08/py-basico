import tkinter as tk

class Janela:
    def __init__(self,toplevel):
        self.fr1 = tk.Frame(toplevel)
        self.fr1.pack()

raiz = tk.Tk()
raiz.geometry('500x500')
Janela(raiz)
raiz.mainloop()