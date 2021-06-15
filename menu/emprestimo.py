from user import User
from book import Book
from loan import Loan
import os 
from datetime import datetime
from bd_credentials import exec_command, exec_select
from lista_books import list_my_books, list_all_books, lista_book, lista_book_disponivel

def pegar_novo_emprestimo(usuario, id_loan, livros):
    now = datetime.now()
    for livro in livros:
        if str(livro[3]) == id_loan:
            sql = f"""UPDATE tb_loan
                        SET id_lender = {usuario.id}, 
                        status = 'EMPRESTADO', 
                        begin_date = '{now.strftime("%d/%m/%Y")}'
                        WHERE id_loan = {id_loan}"""
            result = exec_command(sql)
            if result:
                ("Livro pego emprestado com sucesso.")
                input()
                return
            else:
                ("Falha ao pegar livro emprestado.")
                input()
                return
    print(f"ID {id_loan} não é valido!")
    input()

def disponibilizar_livro(usuario):    
    id_livro = int(input("INFORME O ID DO LIVRO QUE SERÁ DISPONIBILIZADO: "))
    local = input("INFORME O LOCAL ONDE O LIVRO SERÁ DISPONIBILIZADO: ")
    livro = lista_book(id_livro, usuario)
    
    if(len(livro) > 0):
        novo_loan = Loan(0, usuario.id, livro[0][0], local, 'DISPONIVEL')
        sql_loan = f"INSERT INTO tb_loan (id_user, id_book, begin_date, coletion_location, status) values('{usuario.id}', '{novo_loan.id_book}', null, '{novo_loan.collect_location}', '{novo_loan.status}')"
        try:
            exec_command(sql_loan)
            print("LIVRO DISPONIBILIZADO COM SUCESSO!")
        except:
            print("FALHA AO DISPONIBILIZAR LIVRO.")
    else:
        print("ID ESCOLHIDO NÃO É VÁLIDO!")

def lista_livro_emprestimo(usuario):
    os.system("cls")
    sql = f"""SELECT bk.book_name, bk.author, bk.year, ln.id_loan, ln.id_book, ln.coletion_location  
                FROM tb_loan AS ln
                LEFT JOIN tb_book AS bk
                ON ln.id_book = bk.id_book
                WHERE ln.id_lender IS NULL AND ln.id_user != {usuario.id}"""
    livros = exec_select(sql)
    if len(livros) > 0:
        print("LIVROS DISPONÍVEIS PARA EMPRESTIMO: \n")
        for livro in livros:
            print(f"ID: {livro[3]}\nNome livro: {livro[0]}\nAutor: {livro[1]}\nAno de lançamento: {livro[2]}\nLocal para coleta: {livro[5]}\n\n")
        return True, livros
    else:
        print("Não há livros disponíveis para empréstimo.")
        input()
        return False