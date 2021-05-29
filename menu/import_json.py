import os
import json
from cadastro_livro import novos_livros_json

def json_import_livros(user):
    os.system("cls")
    path_json = input("Informe o caminho completo do arquivo Json: ")
    try:
        with open(path_json, "r", encoding="utf-8") as json_file:
            json_books = json.load(json_file)
        print("Arquivo json importado com sucesso!")    
        novos_livros_json(user, json_books)
    except FileNotFoundError:
        print("Caminho informado não é valido!")
        input()
    except PermissionError:
        print("Houve um erro de permissão de leitura. Tente novamente.")
        input()
    except:
        print("Erro ao importar arquivo. Tente novamente.")
        input()

