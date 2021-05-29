from user import User
import os 
import getpass
from bd_credentials import exec_command

import sys
sys.path.insert(0,'..\\')

def cadastro_usuario():
    os.system("cls")
    print("SHARRING BOOKS - CADASTRO DE USUÁRIO: ")
    nome = input("INFORME O PRIMEIRO NOME: ")
    sobrenome = input("INFORME O SOBRENOME: ")
    username = input("INFORME SEU USERNAME: ")
    celular = input("INFORME O CELULAR: ")
    password1 = getpass.getpass("INFORME A SENHA DE ACESSO: ")
    password2 = getpass.getpass("CONFIRME A SENHA DE ACESSO: ")
    while(password1 != password2):
        print("AS SENHAS DEVEM SER AS MESMAS, TENTE NOVAMENTE!\n")
        password1 = getpass.getpass("INFORME A SENHA DE ACESSO: ")
        password2 = getpass.getpass("CONFIRME A SENHA DE ACESSO: ")

    novo_user = User(0, nome, sobrenome, celular, password1, username)

    sql_user = f"INSERT INTO tb_user (first_name, last_name, celular, password, username) values('{novo_user.first_name}', '{novo_user.last_name}', '{novo_user.celular}', '{novo_user.password}', '{novo_user.username}')"

    exec_command(sql_user)

def cadastro_usuario_tela(nome, sobrenome, username, celular, password):
    try: 
        novo_user = User(0, nome, sobrenome, celular, password, username)
        sql_user = f"INSERT INTO tb_user (first_name, last_name, celular, password, username) values('{novo_user.first_name}', '{novo_user.last_name}', '{novo_user.celular}', '{novo_user.password}', '{novo_user.username}')"
        exec_command(sql_user)
        return True
    except:
        return False
