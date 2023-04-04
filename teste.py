from tkinter import * 

class janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()

        self.texto=Label(self.fr1, text='Clique para ficar background amarelo' )
        self.texto['width']=26
        self.texto['height']=3
        self.texto.pack()

        self.botaoverde=Button(self.fr1,text='Clique', command=self.muda_cor)
        self.botaoverde['background']='green'
        self.botaoverde.pack()


        self.botao=Button(self.fr1,text='imprimir', command=self.imprimir)
        self.botao['background']='green'
        self.botao.pack()

        self.campos = Entry()
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



raiz = Tk()
raiz.geometry('350x350')
janela(raiz)
raiz.mainloop()