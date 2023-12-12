from tkinter import messagebox, ttk
from tkinter import * 

import gui

def adicionaAlbum(x):
   fileAddData = open("db.py","a")
   nomeAlbum= gui.textNomeAlbum.get()
   
   try:
        anoLancamento = int(gui.textAnoLancamento.get())
   except:
      messagebox.showinfo(title="Não é numero",message="Digite um numero inteiro")
   nomeBanda = gui.textNomeBanda.get()
   autorLançamento = gui.simOuNao.get()
   
   fileAddData.write(f"{nomeAlbum}|{anoLancamento}|{nomeBanda}|{autorLançamento}\n")
   gui.textNomeAlbum.delete(0,"end")
   gui.textAnoLancamento.delete(0,"end")
   gui.textNomeBanda.delete(0,"end")
   gui.simOuNao.set("sim")
   fileAddData.close()

def criaTela():
    windows = Toplevel()
    windows.title("Adicionar álbum")
    windows.geometry("700x340")
    windows.configure(background="#111111")
    labelTituloDoPrograma = Label(windows, text="Veja aqui seus álbuns", font="Arial 20",background="#1dd05d",foreground="#000000",width=20,borderwidth=3, relief="ridge").place(x=200,y=20)
    return windows

def coletaDados():
    file = open("db.py", "r")
    apresenta = file.read().split("\n")
    del apresenta[-1]
    listaComElementos= []
    for x in apresenta:
        listaComElementos.append(x.split("|"))
    return listaComElementos

def telaDadosCadastrados(x):
    
    windowsLeitura = criaTela()
    listaComElementos = coletaDados()
    apresentaTudo=ttk.Treeview(windowsLeitura,columns=("NomeAlbum","AnoLancamento","NomeBanda","AlbumLancamento"),show="headings")
    apresentaTudo.column("NomeAlbum",minwidth=80,width=140)
    apresentaTudo.column("AnoLancamento",minwidth=80,width=140)
    apresentaTudo.column("NomeBanda",minwidth=80,width=140)
    apresentaTudo.column("AlbumLancamento",minwidth=80,width=140)
    apresentaTudo.heading("NomeAlbum",text="Nome do album")
    apresentaTudo.heading("AnoLancamento",text="Ano de lançamento")
    apresentaTudo.heading("NomeBanda",text="Nome da Banda/Artista")
    apresentaTudo.heading("AlbumLancamento",text="Lançamento do artista")
    apresentaTudo.place(x=80,y=80)
      
    for (NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento) in listaComElementos:
        apresentaTudo.insert("","end", values=(NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento))

def telaBuscaAlbumNome(x):
    def apresentaBusca(x):
        apresentaTudo=ttk.Treeview(windowsBuscaNome,columns=("NomeAlbum","AnoLancamento","NomeBanda","AlbumLancamento"),show="headings")
        apresentaTudo.column("NomeAlbum",minwidth=80,width=140)
        apresentaTudo.column("AnoLancamento",minwidth=80,width=140)
        apresentaTudo.column("NomeBanda",minwidth=80,width=140)
        apresentaTudo.column("AlbumLancamento",minwidth=80,width=140)
        apresentaTudo.heading("NomeAlbum",text="Nome do album")
        apresentaTudo.heading("AnoLancamento",text="Ano de lançamento")
        apresentaTudo.heading("NomeBanda",text="Nome da Banda/Artista")
        apresentaTudo.heading("AlbumLancamento",text="Lançamento do artista")
        apresentaTudo.place(x=80,y=180)
         
        for (NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento) in listaComElementos:
            if textBusca.get() in NomeAlbum:
               apresentaTudo.insert("","end", values=(NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento))
    windowsBuscaNome = criaTela()
    listaComElementos = coletaDados()
      
    labelBuscaPorNome = Label(windowsBuscaNome, text="Faça uma pesquisa pelo nome:", font="Arial 12",background="#111111",foreground="#f7f7f7").place(x=80, y=110)
    textBusca = Entry(windowsBuscaNome,text="Busca Nome", bd=3,width=25)
    textBusca.place(x=320,y=110)
      
    botaoBuscar = Button(windowsBuscaNome,text="Busca pelo nome", font="Arial 10",background="#1dd05d",foreground="#000000",width=15, 
        borderwidth=3, relief="ridge")
    botaoBuscar.bind('<Button-1>',apresentaBusca)
    botaoBuscar.place(x = 500, y= 110)

def telaBuscaAlbumAno(x):
    def apresentaBusca(x):
        apresentaTudo=ttk.Treeview(windowsBuscaAno,columns=("NomeAlbum","AnoLancamento","NomeBanda","AlbumLancamento"),show="headings")
        apresentaTudo.column("NomeAlbum",minwidth=80,width=140)
        apresentaTudo.column("AnoLancamento",minwidth=80,width=140)
        apresentaTudo.column("NomeBanda",minwidth=80,width=140)
        apresentaTudo.column("AlbumLancamento",minwidth=80,width=140)
        apresentaTudo.heading("NomeAlbum",text="Nome do album")
        apresentaTudo.heading("AnoLancamento",text="Ano de lançamento")
        apresentaTudo.heading("NomeBanda",text="Nome da Banda/Artista")
        apresentaTudo.heading("AlbumLancamento",text="Lançamento do artista")
        apresentaTudo.place(x=80,y=180)
         
        for (NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento) in listaComElementos:
            if momentoDoAno.get() == "Igual a":
               if int(textBusca.get()) == int(AnoLancamento):
                  apresentaTudo.insert("","end", values=(NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento))
            elif momentoDoAno.get() == "Anterior a":
               if int(textBusca.get()) > int(AnoLancamento):
                  apresentaTudo.insert("","end", values=(NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento))
            elif momentoDoAno.get() == "Posterior a":
               if int(textBusca.get()) < int(AnoLancamento):
                  apresentaTudo.insert("","end", values=(NomeAlbum,AnoLancamento,NomeBanda,AlbumLancamento))
    windowsBuscaAno = criaTela()
    listaComElementos = coletaDados()
      
    labelBuscaPorNome = Label(windowsBuscaAno, text="Faça uma pesquisa pelo nome:", font="Arial 12",background="#111111",foreground="#f7f7f7").place(x=80, y=110)
    textBusca = Entry(windowsBuscaAno,text="Busca ano", bd=3,width=25)
    textBusca.place(x=320,y=110)
      
    botaoBuscar = Button(windowsBuscaAno,text="Busca pelo ano", font="Arial 10",background="#1dd05d",foreground="#000000",width=15, 
        borderwidth=3, relief="ridge")
    botaoBuscar.bind('<Button-1>',apresentaBusca)
    botaoBuscar.place(x = 500, y= 125)

    momentoDoAno = StringVar()
    momentoDoAno.set("Anterior a")
    buttonRadioAnterior = Radiobutton(windowsBuscaAno,text="Anterior a",variable=momentoDoAno,value="Anterior a", font="Arial 12",background="#111111",foreground="#f7f7f7")
    buttonRadioAnterior.place(x=200,y=140)
    buttonRadioPosterior = Radiobutton(windowsBuscaAno, text="Posterior a", variable=momentoDoAno, value="Posterior a", font="Arial 12",background="#111111",foreground="#f7f7f7")
    buttonRadioPosterior.place(x=300,y=140)
    buttonRadioIgual = Radiobutton(windowsBuscaAno, text="Igual a", variable=momentoDoAno, value="Igual a", font="Arial 12",background="#111111",foreground="#f7f7f7")
    buttonRadioIgual.place(x=410,y=140)
