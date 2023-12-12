from tkinter import * 

import domain

def main():
   windows = Tk()
   windows.title("Adicionar álbum")
   windows.geometry("530x390")
   windows.configure(background="#111111")
   
   labelTituloDoPrograma = Label(windows, text="Adicionador de álbum", font="Arial 20",background="#1dd05d",foreground="#000000",width=20, 
         borderwidth=3, relief="ridge").place(x=100,y=20)

   labelNomeAlbum = Label(windows, text="Nome do álbum: ", font="Arial 12",background="#111111",foreground="#f7f7f7").place(x=50,y=70)
   textNomeAlbum = Entry(windows,text="Nome Album", bd=3)
   textNomeAlbum.place(x=320,y=70)
   print(type(textNomeAlbum))
   labelAnoLancamento = Label(windows, text="Ano de lançamento: ", font="Arial 12",background="#111111",foreground="#f7f7f7").place(x=50,y=100)
   textAnoLancamento = Entry(windows,text="Ano Lançamento", bd=3)
   textAnoLancamento.place(x=320,y=100)

   labelNomeBanda = Label(windows, text="Nome da banda/artista: ", font="Arial 12",background="#111111",foreground="#f7f7f7").place(x=50, y=130)
   textNomeBanda = Entry(windows,text="Nome Banda", bd=3)
   textNomeBanda.place(x=320,y=130)

   labelAlbumLancamento = Label(windows, text="O álbum é o lançamento do artista: ", font="Arial 12",background="#111111",foreground="#f7f7f7").place(x=50, y = 160)

   simOuNao = StringVar()
   simOuNao.set("sim")
   buttonRadioNao = Radiobutton(windows,text="Sim",variable=simOuNao,value="sim", font="Arial 12",background="#111111",foreground="#f7f7f7")
   buttonRadioNao.place(x=320,y=160)
   buttonRadioSim = Radiobutton(windows, text="Não", variable=simOuNao, value="nao", font="Arial 12",background="#111111",foreground="#f7f7f7")
   buttonRadioSim.place(x=380,y=160)

   botaoEnviar = Button(windows,text="Enviar novo álbum", font="Arial 13",background="#1dd05d",foreground="#000000",width=20, 
         borderwidth=3, relief="ridge")
   botaoEnviar.bind('<Button-1>', domain.adicionaAlbum)
   botaoEnviar.place(x = 154, y= 220)

   abrirJanelaLer = Button(windows,text="Todas as pastas", font="Arial 13",background="#1dd05d",foreground="#000000",width=20, 
         borderwidth=3, relief="ridge")
   abrirJanelaLer.bind('<Button-1>', domain.telaDadosCadastrados)
   abrirJanelaLer.place(x = 154, y= 260)

   abrirJanelaBuscaNome = Button(windows,text="Buscar pasta pelo nome", font="Arial 13",background="#1dd05d",foreground="#000000",width=20, 
         borderwidth=3, relief="ridge")
   abrirJanelaBuscaNome.bind('<Button-1>', domain.telaBuscaAlbumNome)
   abrirJanelaBuscaNome.place(x = 154, y= 300)

   abrirJanelaBuscaAno = Button(windows,text="Buscar pasta pelo ano", font="Arial 13",background="#1dd05d",foreground="#000000",width=20, 
         borderwidth=3, relief="ridge")
   abrirJanelaBuscaAno.bind('<Button-1>', domain.telaBuscaAlbumAno)
   abrirJanelaBuscaAno.place(x = 154, y= 340)

   windows.mainloop()
if __name__ == "__main__":
   main()