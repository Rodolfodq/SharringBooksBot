#from user import User
import os 
from bd_credentials import exec_select

def list_my_books(user):
    os.system("cls")
    sql = f"SELECT * FROM tb_book WHERE id_owner = {user.id} ORDER BY id_book"
    livros = (exec_select(sql))
    for livro in livros:
        print(f"ID: {livro[0]}\nNome: {livro[1]}\nAno: {livro[2]}\nAutor: {livro[3]}\n")

def list_all_books(user):
    os.system("cls")
    sql = f"""SELECT 
                us.first_name, us.last_name, 
                bk.book_name, bk.author, bk.year,
                ln.coletion_location, ln.status
                FROM tb_loan AS ln
                LEFT JOIN tb_book AS bk
                ON ln.id_book = bk.id_book
                LEFT JOIN tb_user AS us
                ON ln.id_user = us.id_user
                WHERE ln.status = 'DISPONIVEL' AND ln.id_user != {user.id}"""
    livros = (exec_select(sql))
    if len(livros) > 0:
        for livro in livros:
            print(f"Dono do livro: {livro[0]} {livro[1]}")
            print(f"Nome do livro: {livro[2]}\nAno: {livro[4]}\nAutor: {livro[3]}")
            print(f"Local para coleta: {livro[5]}\nStatus: {livro[6]}\n")
    else:
        print("Não há nenhum livro disponível para empréstimo no momento.")

def lista_book(id, usuario):
    sql = f"SELECT * FROM tb_book WHERE id_book = {id} and id_owner = {usuario.id}"
    livro = (exec_select(sql))
    return livro

def lista_book_disponivel():
    sql = f"SELECT * FROM tb_loan WHERE status = 'DISPONIVEL'"
    livros = (exec_select(sql))
    for livro in livros:
        #print(f"ID: {livro[0]}\nNome: {livro[1]}\nAno: {livro[2]}\nAutor: {livro[3]}\n")    
        print(livro)

def lista_book_disponível_user(user):
    sql = f"""SELECT bk.id_book, bk.book_name, bk.year, bk.author, bk.id_owner 
                FROM tb_book AS bk 
                LEFT JOIN tb_loan AS ln
                ON bk.id_book = ln.id_book
                WHERE bk.id_owner = {user.id} AND ln.id_book IS NULL;"""
    livros = exec_select(sql)
    if len(livros) == 0:
        print("Você não possui nenhum livro disponível para empréstimo!")
        return False
    else:
        print("SEUS LIVROS DISPONÍVEIS PARA EMPRÉSTIMO:\n")
        for livro in livros:
            print(f"ID: {livro[0]}\nNome: {livro[1]}\nAno: {livro[2]}\nAutor: {livro[3]}\n")
        return True    
    