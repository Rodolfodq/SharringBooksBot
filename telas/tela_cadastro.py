from tkinter import *  
from tkinter import messagebox as mbox
# from typing import Sequence
import sys
sys.path.insert(0,'..\\')

import menu.cadastro

class FrameCadastro(Frame):

    def __init__(self, master=None):
        super().__init__()
        self.master.geometry("600x600")
        self.master.title("Sharring Books - Cadastro")
        self.master.resizable(False, False)
        self.pack()

        self.frame_cadastro = Frame(bg="#008B8B", height=60)
        self.frame_cadastro.pack(fill=X)

        self.titulo = Label(self.frame_cadastro)
        self.titulo["text"] = "Cadastro"
        self.titulo["bg"] = "#008B8B"
        self.titulo["fg"] = "#FFFFFF"
        self.titulo["font"] = "Helvetica 16 bold"
        self.titulo.pack(side=TOP, ipady=15)

        self.frame2 = Frame(bg="#FFFFFF", height=40)
        self.frame2.pack(fill=X)
        self.lbl1 = Label(self.frame2, text="Nome:              ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl1.pack(side=LEFT, ipadx=10, ipady=10)

        self.nome = Entry(self.frame2, width=30, bg="#dedede", font=("Helvetica", 12))
        self.nome.pack(side=LEFT)
        self.nome.focus_set()

        self.frame3 = Frame(bg="#FFFFFF", height=40)
        self.frame3.pack(fill=X)
        self.lbl2 = Label(self.frame3, text="Sobrenome:         ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl2.pack(side=LEFT, ipadx=10, ipady=10)

        self.sobrenome = Entry(self.frame3, width=30, bg="#dedede", font=("Helvetica", 12))
        self.sobrenome.pack(side=LEFT)

        self.frame4 = Frame(bg="#FFFFFF", height=40)
        self.frame4.pack(fill=X)
        self.lbl3 = Label(self.frame4, text="Nome de Usuário:   ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl3.pack(side=LEFT, ipadx=10, ipady=10)

        self.user_name = Entry(self.frame4, width=30, bg="#dedede", font=("Helvetica", 12))
        self.user_name.pack(side=LEFT)

        self.frame5 = Frame(bg="#FFFFFF", height=40)
        self.frame5.pack(fill=X)
        self.lbl4 = Label(self.frame5, text="Celular:           ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl4.pack(side=LEFT, ipadx=10, ipady=10)

        self.celular = Entry(self.frame5, width=30, bg="#dedede", font=("Helvetica", 12))
        self.celular.pack(side=LEFT)

        self.frame6 = Frame(bg="#FFFFFF", height=40)
        self.frame6.pack(fill=X)
        self.lbl5 = Label(self.frame6, text="Senha:             ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl5.pack(side=LEFT, ipadx=10, ipady=10)

        self.password = Entry(self.frame6, show="*", width=30, bg="#dedede", font=("Helvetica", 12))
        self.password.pack(side=LEFT)

        self.frame7 = Frame(bg="#FFFFFF", height=40)
        self.frame7.pack(fill=X)
        self.lbl6 = Label(self.frame7, text="Confirmar Senha:   ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl6.pack(side=LEFT, ipadx=10, ipady=10)        

        self.password_confirm = Entry(self.frame7, show="*", width=30, bg="#dedede", font=("Helvetica", 12))
        self.password_confirm.pack(side=LEFT)

        self.frame8 = Frame(bg="#FFFFFF", height=40)
        self.frame8.pack(fill=X) 

        self.btn_cadastro = Button(self.frame8, text="Login", width=10)  
        self.btn_cadastro.pack(side=LEFT, padx=12)
        self.btn_cadastro.config(command=self.cadastro)

        self.btn_limpar = Button(self.frame8, text="Limpar", width=10)  
        self.btn_limpar.pack(side=LEFT, padx=12)
        self.btn_limpar.config(command=self.limpar_campos)


    def cadastro(self):
        name = self.nome.get()
        last_name = self.sobrenome.get()
        name_user = self.user_name.get()
        phone = self.celular.get()
        pass1 = self.password.get()
        pass2 = self.password_confirm.get()

        if(name == "" or last_name == "" or phone == "" or pass1 == "" or pass2 == ""):
            mbox.showinfo("Falha no cadastro", "Todos os campos são obrigatórios!")
            return 
        if(pass1 == pass2):
            result = menu.cadastro.cadastro_usuario_tela(name, last_name, name_user, phone, pass1)
            if(result):
               mbox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            else:
                mbox.showinfo("Falha no cadastro", "Falha ao cadastrar usuário!")   
        else:
            mbox.showinfo("Falha no cadastro", "As senhas não são as mesmas!")

    def limpar_campos(self):
        self.nome.delete(0, "end")
        self.sobrenome.delete(0, "end")
        self.user_name.delete(0, "end")
        self.celular.delete(0, "end")
        self.password.delete(0, "end")
        self.password_confirm.delete(0, "end")
        self.nome.focus_set()

        



def tela_para_cadastro():
    app = FrameCadastro()
    #app.mainloop() 

app = FrameCadastro()
app.mainloop() 