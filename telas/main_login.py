from tkinter import *  
from tkinter import messagebox as mbox
# from typing import Sequence
import sys
import tkinter
sys.path.insert(0,'..\\')

import menu.login
import telas.tela_cadastro

class FramePrincipal(Frame):

    def __init__(self, master=None):
        super().__init__()
        self.master.geometry("400x400")
        self.master.title("Sharring Books - Login")
        self.master.resizable(False, False)
        self.pack()

        self.frame1 = Frame(bg="#008B8B", height=60)
        self.frame1.pack(fill=X)

        self.titulo = Label(self.frame1)
        self.titulo["text"] = "Login"
        self.titulo["bg"] = "#008B8B"
        self.titulo["fg"] = "#FFFFFF"
        self.titulo["font"] = "Helvetica 16 bold"
        self.titulo.pack(side=TOP, ipady=15)

        self.frame2 = Frame(bg="#FFFFFF", height=40)
        self.frame2.pack(fill=X)
        self.lbl1 = Label(self.frame2, text="Usuário: ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl1.pack(side=LEFT, ipadx=10, ipady=10)

        self.usuario = Entry(self.frame2, width=30, bg="#dedede", font=("Helvetica", 12))
        self.usuario.pack(side=LEFT)
        self.usuario.focus_set()

        self.frame3 = Frame(bg="#FFFFFF", height=40)
        self.frame3.pack(fill=X)
        self.lbl2 = Label(self.frame3, text="Senha:   ", bg="#FFFFFF", font=("Helvetica", 12))
        self.lbl2.pack(side=LEFT, ipadx=10, ipady=10)

        self.password = Entry(self.frame3, show='*', width=30, bg="#dedede", font=("Helvetica", 12))
        self.password.pack(side=LEFT)

        self.frame4 = Frame(bg="#FFFFFF", height=40)
        self.frame4.pack(fill=X)    

        self.btn_login = Button(self.frame4, text="Login", width=10)  
        self.btn_login.pack(side=LEFT, padx=12)  

        self.btn_cancel = Button(self.frame4, text="Limpar", width=10)
        self.btn_cancel.pack(side=LEFT, padx=12)

        self.btn_cadastro = Button(self.frame4, text="Cadastro", width=10)
        self.btn_cadastro.pack(side=LEFT, padx=12)

        self.btn_login.config(command=self.user_login_tela)
        self.btn_cancel.config(command=self.limpar_campos)
        self.btn_cadastro.config(command=self.cadastrar_usuario)

    def user_login_tela(self):
        usuario = self.usuario.get()    
        password = self.password.get()                
        response = menu.login.user_login_tela(usuario, password)
        if(response):
            mbox.showinfo("Sucesso", f"Usuário: \n{response.first_name} {response.last_name}")
        else:
            mbox.showinfo("Falha no login", "Credenciais inválidas!")

    def limpar_campos(self):
        self.usuario.delete(0, "end")
        self.password.delete(0, "end")
        self.usuario.focus_set() 

    def cadastrar_usuario(self):      
        telas.tela_cadastro.tela_para_cadastro()



app = FramePrincipal()
app.mainloop()        