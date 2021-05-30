from user import User
import os 
import getpass
from bd_credentials import exec_select
import sys
sys.path.insert(0,'..\\')


def user_login():
    os.system("cls")

    print("SHARRING BOOKS - LOGIN: ")
    username = input("INFORME O USERNAME: ")
    password = getpass.getpass("INFORME A SENHA DE ACESSO: ")

    sql = f"SELECT * FROM tb_user WHERE username = '{username}'"

    result_login = exec_select(sql) 
    if(len(result_login) == 0):
        print("Usuário não encontrado!")
        input()
        return False
    elif(len(result_login) == 1):        
        if(password == result_login[0][4]):            
            usuario = User(result_login[0][0], result_login[0][1], result_login[0][2], result_login[0][3], result_login[0][4], result_login[0][5])
            print(f'Bem-vindo, {usuario.first_name}')
            return usuario
        else:
            input()
            print("SENHA INCORRETA!")
    else:
        print("Falha na autenticação!")
        input()
        return False

def user_login_tela(username, password):   

    sql = f"SELECT * FROM tb_user"

    result_login = exec_select(sql) 
    if(len(result_login) == 0):
        print("Usuário não encontrado!")
        return False
    elif(len(result_login) >= 1):
        for resultado in result_login:
            if(password == resultado[4] and username == resultado[5]):            
                usuario = User(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                print(f'Bem-vindo, {usuario.first_name}')
                return usuario
    else:
        print("Falha na autenticação!")
        return False        
