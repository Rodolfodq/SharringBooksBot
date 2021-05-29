import os
from bd_credentials import exec_command, exec_select
from datetime import datetime


def devolver_livro(id_loan):
    now = datetime.now()
    delivery_location = input("Informe o local onde o livro foi devolvido: ")
    sql = f"""UPDATE tb_loan
                SET status = 'DEVOLVIDO', 
                end_date = '{now.strftime("%d/%m/%Y")}',
                delivery_location = '{delivery_location}'
                WHERE id_loan = {id_loan}""" 
    retorno = exec_command(sql)
    if retorno:
        print("Livro devolvido com sucesso!")
    else:
        print("Falha ao devolver livro.")
    
    sql_loan = f"""SELECT id_user, id_book FROM tb_loan WHERE id_loan = {id_loan}"""
    new_loan = exec_select(sql_loan)

    id_user = new_loan[0][0]
    id_book = new_loan[0][1]
    
    sql_insert_loan = f"""INSERT INTO tb_loan(id_user, id_book, begin_date, coletion_location, status)
                        VALUES({id_user}, {id_book}, null, '{delivery_location}', 'DISPONIVEL')"""
    result = exec_command(sql_insert_loan)
    return result

def lista_livros_devolucao(user):
    os.system("cls")
    sql = f"""SELECT bk.book_name, bk.author, bk.year, ln.id_loan, ln.id_user, ln.id_book
                FROM tb_loan AS ln
                LEFT join tb_book AS bk
                ON ln.id_book = bk.id_book
                WHERE ln.id_lender = {user.id} AND ln.status = 'EMPRESTADO'"""
    livros = exec_select(sql)
    if len(livros) > 0:
        print("Livros que você ainda não devolveu: \n")        
        for livro in livros:
            print(f"ID: {livro[3]}\nNome livro: {livro[0]}\nAutor: {livro[1]}\nAno: {livro[2]}")        
                
        return True
    else:
        print("Você não possui nenhum livro para devolução.")
        input()
        return False

