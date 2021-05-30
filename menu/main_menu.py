import os
from user import User
from login import user_login
from cadastro import cadastro_usuario, update_usuario
from cadastro_livro import novo_livro, update_book
from lista_books import list_my_books, list_all_books, lista_book_disponível_user
from emprestimo import disponibilizar_livro, pegar_novo_emprestimo, lista_livro_emprestimo
from devolver import devolver_livro, lista_livros_devolucao
from sobre import sobre_trabalho
from import_json import json_import_livros_arquivo, json_import_livros_url
from exporta_dados import export_dados

import sys
sys.path.insert(0,'..\\')


def exibe_menu_login():
    os.system("cls")
    print("""
    SHARRING BOOKS
    [01] REALIZAR LOGIN
    [02] CADASTRAR NOVO USUARIO
    [00] Sair
    """)

def exibe_menu_principal(usuario):
    os.system("cls")
    print(f"""
    SHARRING BOOKS    
    Bem-vindo, {usuario.first_name}.
    [02] CADASTRAR NOVO USUARIO
    [03] CADASTRAR NOVO LIVRO
    [04] LISTAR MEUS LIVROS
    [05] LISTAR TODOS LIVROS DISPONIVEIS
    [06] DISPONIBILIZAR UM LIVRO
    [07] PEGAR LIVRO EMPRESTADO
    [08] DEVOLVER UM LIVRO
    [09] IMPORTAR ARQUIVO JSON DOS SEUS LIVROS
    [10] IMPORTAR JSON DOS SEUS LIVROS A PARTIR DE UMA URL 
    [11] ATUALIZAR DADOS DO USUÁRIO
    [12] ATUALIZAR DADOS DE UM LIVRO
    [13] SOBRE
    [99] EXPORTAR SEUS DADOS EM JSON
    [00] Sair
    """)

lista_menu = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13' '99']
exibe_menu_login()
while(True):
    try:    
        opt = input("OPCAO: ")
        if opt == '01':
            usuario_logado = user_login()
            if(usuario_logado):
                exibe_menu_principal(usuario_logado)
        elif opt == '02':
            cadastro_usuario()        
            usuario_logado = user_login() 
        elif(opt == '00'):
            os.system("cls")
            print("Sistema finalizado com sucesso.")
            exit()     
        if(usuario_logado):
            exibe_menu_principal(usuario_logado)
            if(opt == '02'):
                cadastro_usuario()
                exibe_menu_login() 
            elif(opt == '03'):
                novo_livro(usuario_logado)
                exibe_menu_principal(usuario_logado)
            elif(opt == '04'):
                list_my_books(usuario_logado)
                input()
                exibe_menu_principal(usuario_logado)
            elif(opt == '05'):
                list_all_books(usuario_logado)            
                input()
                exibe_menu_principal(usuario_logado)
            elif(opt == '06'):
                result = lista_book_disponível_user(usuario_logado)
                if result:
                    disponibilizar_livro(usuario_logado)
                input()
                exibe_menu_principal(usuario_logado)
            elif(opt == '07'):
                result = lista_livro_emprestimo(usuario_logado)            
                if result:
                    id_loan = input("Infome o ID do livro que você irá pegar emprestado: ")
                    pegar_novo_emprestimo(usuario_logado, id_loan)                
                exibe_menu_principal(usuario_logado)            
            elif(opt == '08'):
                result = lista_livros_devolucao(usuario_logado)
                if result:
                    id_loan = input("Infome o ID do livro que você irá devolver: ")
                    result_devolucao = devolver_livro(id_loan)
                    if result_devolucao:
                        exibe_menu_principal(usuario_logado)
                else:
                    os.system("cls")
                    exibe_menu_principal(usuario_logado)
            elif(opt == '09'):
                json_import_livros_arquivo(usuario_logado)
                exibe_menu_principal(usuario_logado)
            elif(opt == '10'):
                json_import_livros_url(usuario_logado)
                exibe_menu_principal(usuario_logado)
            elif(opt == '11'):
                update_usuario(usuario_logado)
                exibe_menu_principal(usuario_logado)
            elif(opt == '12'):
                update_book(usuario_logado)
                exibe_menu_principal(usuario_logado)
            elif(opt == '13'):
                sobre_trabalho()
                input()
                exibe_menu_principal(usuario_logado)
            elif(opt == '99'):
                export_dados(usuario_logado)
                exibe_menu_principal(usuario_logado)
            elif(opt == '00'):
                os.system("cls")
                print("Sistema finalizado com sucesso.")
                exit()
            elif(opt not in lista_menu):
                print("Esta não é uma opção válida. Tente novamente.")
                input()
                os.system("cls")
                exibe_menu_principal(usuario_logado)      
        else:
            #usuario_logado = user_login()  
            exibe_menu_login()
    except KeyboardInterrupt:
        print("\nSistema finalizado com sucesso.")
        exit()
