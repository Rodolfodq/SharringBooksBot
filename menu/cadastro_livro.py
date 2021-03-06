from user import User
from book import Book
import os 
from bd_credentials import exec_command
from lista_books import list_my_books

def novo_livro(user):
    os.system("cls")
    try:
        book_name = input("INFORME O NOME DO LIVRO: ")
        year = int(input("INFORME O ANO DA EDIÇÃO: "))
        author = input("INFORME O AUTOR: ")

        new_book = Book(0, book_name, year, author, user.id)

        sql_user = f"INSERT INTO tb_book (book_name, year, author, id_owner) values('{new_book.name}', '{new_book.year}', '{new_book.author}', '{user.id}')"

        exec_command(sql_user)
        print("Livro inserido com sucesso!")
        input()
    except:
        print("Falha ao inserir livro. Tente novamente")
        input()

def novos_livros_json(user, json_books):
    print(f"Importando {len(json_books)} livros para o banco de dados.")
    try:
        for book in json_books:
            new_book = Book(0, book['book_name'], book['year'], book['author'], user.id)
            sql_user = f"INSERT INTO tb_book (book_name, year, author, id_owner) values('{new_book.name}', '{new_book.year}', '{new_book.author}', '{user.id}')"
            exec_command(sql_user)
        print("Importação finalizada com sucesso")
        input()
    except:
        print("Falha na importação dos livros.")
        input()

def update_book(user):
    os.system("cls")
    list_my_books(user)
    book_id = input("INFORME O ID DO LIVRO QUE SERÁ ATUALIZADO: ")

    try:
        book_name = input("INFORME O NOME DO LIVRO: ")
        year = int(input("INFORME O ANO DA EDIÇÃO: "))
        author = input("INFORME O AUTOR: ")       

        sql_book = f"""UPDATE tb_book
                        SET 
                        book_name = '{book_name}',
                        year = '{year}',
                        author = '{author}'
                        WHERE id_book = '{book_id}' and id_owner = '{user.id}'"""

        exec_command(sql_book)
        print("Livro atualizado com sucesso!")
        input()
    except:
        print("Falha ao atualizar livro. Tente novamente")
        input()

