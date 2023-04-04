import tkinter as tk
class janela:
    def __init__(self, toplevel):
        self.fr1 = tk.Frame(toplevel)
        self.fr1.pack()

        self.texto=tk.Label(self.fr1, text='Clique para ficar background amarelo' )
        self.texto['width']=26
        self.texto['height']=3
        self.texto.pack()

        self.botaoverde=tk.Button(self.fr1,text='Clique', command=self.muda_cor)
        self.botaoverde['background']='green'
        self.botaoverde.pack()


        self.botao=tk.Button(self.fr1,text='imprimir', command=self.abrijanela)
        self.botao['background']='green'
        self.botao.pack()

        self.campos = tk.Entry()
        self.campos.pack()

    
        
        
    def muda_cor(self):
        # Muda a cor do botao!
            if self.botaoverde['bg']=='green':
                self.botaoverde['bg']='yellow'
                self.texto['text']='Clique para ficar verde'
            else:
                self.botao['bg']='green'
                self.texto['text']='Clique para ficar amarelo'

    
    def imprimir(self):
        print('#####')
        print(self.campos.get())

    def abrijanela(self):
        jn = tk.Toplevel()
        jn.title('teste nova janela')
        jn.geometry('350x350')

raiz = tk.Tk()
raiz.geometry('350x350')
janela(raiz)
raiz.mainloop()