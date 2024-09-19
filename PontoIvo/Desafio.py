from tkinter import*

def apagarDados():
    apagar = open('desafio.txt', 'w', encoding='utf-8')
    apagar.write('')
    apagar.close()
    dados.delete(0,END)

def carregarDados():
    carregar = open('desafio.txt', 'r', encoding='utf-8')
    carregarDados = carregar.read()
    carregar.close()
    lista = carregarDados.split(';')
    for i in lista:
        dados.insert(END, i)

def add():
    salvarInfo = (f'Nome = {t1Nome.get()} | Endereço = {t2Endereco.get()} | CPF = {t3Cpf.get()} | Idade = {t4Idade.get()}')
    salvarDados = open('desafio.txt', 'a', encoding='utf-8')
    salvarDados.write(f'{salvarInfo};')
    salvarDados.close()
    dados.insert(END, salvarInfo)
    t1Nome.delete(0,END)
    t2Endereco.delete(0,END)
    t3Cpf.delete(0,END)
    t4Idade.delete(0,END)

def exibir_dados_para_edicao(event):
    selecionado = dados.curselection()
    if not selecionado:
        return

    visualizar = dados.get(selecionado).split('|')


    t1Nome.delete(0, END)
    t2Endereco.delete(0, END)
    t3Cpf.delete(0, END)
    t4Idade.delete(0, END)

    t1Nome.insert(0, visualizar[0])
    t2Endereco.insert(0, visualizar[1])
    t3Cpf.insert(0, visualizar[2])
    t4Idade.insert(0, visualizar[3])


window = Tk()
window.title('Aula Ivo')
window.geometry('800x600')
    
dados = Listbox(width=80, height=10,)
dados.pack()
dados.place(x=120, y=300)
dados.bind('<<ListboxSelect>>', exibir_dados_para_edicao)


lbl1 = Label(window, text='Nome')
lbl2 = Label(window, text='Endereço')
lbl3 = Label(window, text='CPF')
lbl4 = Label(window, text='Idade')
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl1.place(x=250, y=60)
lbl2.place(x=240, y=110)
lbl3.place(x=250, y=160)
lbl4.place(x=250, y=200)


t1Nome = Entry()
t2Endereco = Entry()
t3Cpf = Entry()
t4Idade = Entry()
t1Nome.place(x=300, y=60)
t2Endereco.place(x=300, y=110)
t3Cpf.place(x=300, y=160)
t4Idade.place(x=300, y=200)


btAdd = Button(window, text='Adicionar', command=add)
btSub = Button(window, text='Apagar', command=apagarDados)
btAdd.pack()
btSub.pack()
btAdd.place(x=250, y=240)
btSub.place(x=400, y=240)



carregarDados()
window.mainloop()