#importando as bibliotecas necessarias
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
#pillow é a biblioteca que possibilita manipular imagens
from PIL import ImageTk, Image
#importando o crud
from sqlite.CRUDalunos import *


#cores
preto = '#000000' #preto
branco = '#FFFFFF' #branco
cinza = '#e5e5e5' #cinza claro
verde = '#00a050' #verde limão
azulbb = '#89CFF0' # Azul bebê
vermelho = '#880808' #Vermelho Sangue
azulcorn = '#6495ED' # Azul Cornflower
azulcinza = "#263238" # Azul acizentado escuro

#criando a janela

jan = Tk()
jan.title("Escola")
jan.geometry('720x620')
jan.configure(background=branco)
jan.resizable(width=FALSE, height=FALSE)
#estilização
style = Style(jan)
style.theme_use("clam")

#dividirei a tela em 4 partes: 1.um cabeçalho com titulo; 2.um com os botões de cadastro e adição; 3.um com o formulario necessario
#para operações e 4. a tabela que mostra as informações dos alunos 

#Parte 1 da janela: Cabeçalho
logo = Frame(jan, width=850, height=52, bg=azulbb)
logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
#Imagem e nome
logoimg = Image.open('img/student.png')
logoimg = logoimg.resize((50,50))
logoimg = ImageTk.PhotoImage(logoimg)

logolabel = Label(logo, image=logoimg, text="Cadastro de Alunos/Notas", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=azulbb, fg=branco)
logolabel.place(x=0, y=0)
#linha de divisão
ttk.Separator(jan, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)
#Parte 2 da janela: Botões
botoes = Frame(jan, width=850, height=65, bg=branco)
botoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)
#Criação dos botões de cadastro
cadastro = Image.open('img/add.png')
cadastro = cadastro.resize((18, 18))
cadastro = ImageTk.PhotoImage(cadastro)

cadastrobtn = Button(botoes,command=lambda:controle('cadastro'), image=cadastro, text="Cadastrar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=branco, fg= preto)
cadastrobtn.place(x=10, y=30)
#Criação dos botões de update
editar = Image.open('img/update.png')
editar = editar.resize((18, 18))
editar = ImageTk.PhotoImage(editar)

#Criação botão de deletar
delete = Image.open('img/delete.png')
delete = delete.resize((18, 18))
delete = ImageTk.PhotoImage(delete)
#criação botão ver
ver = Image.open('img/ver.png')
ver = ver.resize((18, 18))
ver = ImageTk.PhotoImage(ver)

def controle(i):
    #apaga tudo da pag para apresentar ocadastro
    if i == 'cadastro':
        for widget in botoes.winfo_children():
            widget.destroy
        for widget in forms.winfo_children():
            widget.destroy
        for widget in tab.winfo_children():
            widget.destroy()
        #puxando a função cadastro
        cadastra()
        


#linha de divisão
ttk.Separator(jan, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)
#Parte 3 da janela: Formularios
forms = Frame(jan, width=850, height=200, bg=branco)
forms.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

#Parte 4 da janela: Tabela de infos
tab = Frame(jan, width=850, height=180, bg=branco)
tab.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

#função de cadastro de alunos
def cadastra():
#criando a tela de cadastro
    #criando a função que vai cadastrar os alunos
    def novo_aluno():
        matricula = ematricula.get()
        nome = enome.get()
        idade = eidade.get()
        sexo = esexo.get()
        n1 = en1.get()
        n2 = en2.get()
        n3 = en3.get()
        
        try:
            n1 = float(n1)
            n2 = float(n2)
            n3 = float(n3)
        except ValueError:
                messagebox.showerror('Erro', 'As notas devem ser números')
                return

        
        #lista pra receber e mandar pro bd
        lista = [matricula, nome, idade, sexo, n1, n2, n3]
        #verificação dos campos
        for i in lista:
            if i =='':
                messagebox.showerror('Erro', 'Preencha todos os dados')
                return
            #caso tudo certo, insirir no bd
            cria_aluno(lista)
            #mensagem de sucesso
            messagebox.showinfo('Sucesso!','Dados cadastrados com sucesso')
            #limpando as entradas
            ematricula.delete(0,END)
            enome.delete(0,END)
            eidade.delete(0,END)
            esexo.delete(0,END)
            en1.delete(0,END)
            en2.delete(0,END)
            en3.delete(0,END)
            #chamando a tabela atualizada
            mostrar_alunos()
    #Função de atualização dos dados do aluno
    def atualizar_aluno():
        try:
            tree_itens = tree_alunos.focus()
            tree_dic = tree_alunos.item(tree_itens)
            tree_lista = tree_dic['values']
            
            valormatricula = tree_lista[0]
            
            ematricula.delete(0,END)
            enome.delete(0,END)
            eidade.delete(0,END)
            esexo.delete(0,END)
            en1.delete(0,END)
            en2.delete(0,END)
            en3.delete(0,END)
            
            #inserindo os valores já cadastrados
            ematricula.insert(0,tree_lista[0])
            enome.insert(0,tree_lista[1])
            eidade.insert(0,tree_lista[2])
            esexo.insert(0,tree_lista[3])
            en1.insert(0,tree_lista[4])
            en2.insert(0,tree_lista[5])
            en3.insert(0,tree_lista[6])
        
            def update():
                matricula = ematricula.get()
                nome = enome.get()
                idade = eidade.get()
                sexo = esexo.get()
                n1 = en1.get()
                n2 = en2.get()
                n3 = en3.get()

                try:
                    n1 = float(n1)
                    n2 = float(n2)
                    n3 = float(n3)
                except ValueError:
                    messagebox.showerror('Erro', 'As notas devem ser números')
                    return

                # Lista para receber e mandar pro BD
                lista = [matricula, nome, idade, sexo, n1, n2, n3]
                # Verificação dos campos
                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', 'Preencha todos os dados')
                        return
                # Atualizar no BD
                atualiza_aluno(lista)
                # Mensagem de sucesso
                messagebox.showinfo('Sucesso!', 'Dados atualizados com sucesso')
                # Limpando as entradas
                ematricula.delete(0, END)
                enome.delete(0, END)
                eidade.delete(0, END)
                esexo.delete(0, END)
                en1.delete(0, END)
                en2.delete(0, END)
                en3.delete(0, END)
                # Chamando a tabela atualizada
                mostrar_alunos()
                # Destruindo o botão
                btnatualizarifo.destroy()

            btnatualizarifo = Button(forms, anchor=CENTER, command=update, image=editar, text="ATUALIZAR INFOS", width=85, overrelief=RIDGE, compound=LEFT, font=('Ivy 7 bold'), bg=azulcorn, fg=branco)
            btnatualizarifo.place(x=600, y=150)
        except IndexError:
            messagebox.showerror('ERROR', 'Selecione um aluno cadastrado')
    
    #função de deletar aluno
    def deletar_aluno():
        try:
            tree_itens = tree_alunos.focus()
            tree_dic = tree_alunos.item(tree_itens)
            tree_lista = tree_dic['values']
            
            valormatricula = tree_lista[0]
            
            #deletando no bd
            deleta_aluno(valormatricula)
            # Mensagem de sucesso
            messagebox.showinfo('Sucesso!', 'Aluno deletado com sucesso')
            #atualizando tabela com aluno deletado
            mostrar_alunos()
        except IndexError:
            messagebox.showerror('ERROR', 'Selecione um aluno cadastrado')
        
            
    #matricula
    fmatricula = Label(forms, text="Matricula do aluno: *", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fmatricula.place(x=4, y=10)
    ematricula = Entry(forms, width=45, justify='left', relief='solid')
    ematricula.place(x=7, y=40)
    #nome
    fnome = Label(forms, text="Nome do aluno: *", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fnome.place(x=4, y=70)
    enome = Entry(forms, width=45, justify='left', relief='solid')
    enome.place(x=7, y=100)
    #idade
    fidade = Label(forms, text="Idade: *", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fidade.place(x=4, y=130)
    eidade = Entry(forms, width=15, justify='left', relief='solid')
    eidade.place(x=7, y=160)
    #sexo
    #seletor de genero
    fsexo = Label(forms, text="Sexo:*", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fsexo.place(x=190, y=130)
    esexo = ttk.Combobox(forms, width=12, font=('Ivy 8 bold'))
    esexo['values'] = ('Masculino', 'Feminino', 'Outro')
    esexo.place(x=190, y=160)
    #nota 1
    fn1 = Label(forms, text="Nota 1: *", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fn1.place(x=306, y=10)
    en1 = Entry(forms, width=20, justify='left', relief='solid')
    en1.place(x=309, y=40)
    #nota 2
    fn2 = Label(forms, text="Nota 2: *", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fn2.place(x=306, y=70)
    en2 = Entry(forms, width=20, justify='left', relief='solid')
    en2.place(x=309, y=100)
    #nota 3
    fn3 = Label(forms, text="Nota 3: *", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    fn3.place(x=306, y=130)
    en3 = Entry(forms, width=20, justify='left', relief='solid')
    en3.place(x=309, y=160)
    #linha de separação
    separa = Label(forms, relief=GROOVE, text='h', height=100, anchor=NW, font=('Ivy 1'), bg=preto, fg=preto)
    separa.place(x=450, y=10)
    separa = Label(forms, relief=GROOVE, text='h', height=100, anchor=NW, font=('Ivy 1'), bg=azulbb, fg=preto)
    separa.place(x=450, y=10)
    
    #botões de edição
    btnsalvar = Button(forms, command=novo_aluno , anchor=CENTER, image=cadastro, text="SALVAR", width=65, overrelief=RIDGE, compound=LEFT, font=('Ivy 7 bold'), bg=verde, fg=branco)
    btnsalvar.place(x=470, y=112)
    
    btndeletar = Button(forms, command=deletar_aluno, anchor=CENTER, image=delete, text="DELETAR", width=65, overrelief=RIDGE, compound=LEFT, font=('Ivy 7 bold'), bg=vermelho, fg=branco)
    btndeletar.place(x=470, y=140)
    
    btnatualizar = Button(forms, anchor=CENTER,command=atualizar_aluno, image=editar, text="ATUALIZAR", width=65, overrelief=RIDGE, compound=LEFT, font=('Ivy 7 bold'), bg=azulcorn, fg=branco)
    btnatualizar.place(x=470, y=170)
    
    btnver = Button(forms, anchor=CENTER, image=ver, text="VER", width=65, overrelief=RIDGE, compound=LEFT, font=('Ivy 7 bold'), bg=branco, fg=preto)
    btnver.place(x=600, y=170) 
    #Tabela
    #Função para mostrar a tabela de alunos
    def mostrar_alunos():
        tabela = Label(tab, text="Tabela de Alunos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
        tabela.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # criando a treeview com barras de rolagem duplas
        list_header = ['Matricula', 'Nome', 'Idade', 'Sexo', 'Nota 1', 'Nota 2', 'Nota 3', 'Media', 'Situação']

        df_list = []

        global tree_alunos

        tree_alunos = ttk.Treeview(tab, selectmode="extended", columns=list_header, show="headings")
        # barra de rolagem vertical
        vsb = ttk.Scrollbar(tab, orient="vertical", command=tree_alunos.yview)
        # barra de rolagem horizontal
        hsb = ttk.Scrollbar(tab, orient="horizontal", command=tree_alunos.xview)

        tree_alunos.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_alunos.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        tab.grid_rowconfigure(0, weight=12)

        # Larguras e âncoras das colunas
        colunas_largura = {
            'Matricula': 80,
            'Nome': 150,
            'Idade': 50,
            'Sexo': 60,
            'Nota 1': 60,
            'Nota 2': 60,
            'Nota 3': 60,
            'Media': 60,
            'Situação': 100
        }

        for col in list_header:
            tree_alunos.heading(col, text=col.title(), anchor=NW)
            tree_alunos.column(col, width=colunas_largura[col], anchor=NW)

        # Exemplo de dados para teste
        df_list = ve_aluno()

        for item in df_list:
            tree_alunos.insert('', 'end', values=item)

    # Chamando a função para mostrar a tabela
    mostrar_alunos()

#loop de inicialização
cadastra()
jan.mainloop()