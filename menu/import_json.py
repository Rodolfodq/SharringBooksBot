import os
import json
from re import escape
from cadastro_livro import novos_livros_json
import urllib.request, urllib.error

def json_import_livros_arquivo(user):
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

def json_import_livros_url(user):
    os.system("cls")
    url = input("Informe a URL do arquivo Json: ")
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode(response.headers.get_content_charset())
        json_books = json.loads(data)
        novos_livros_json(user, json_books)
    except urllib.error.HTTPError as e:
        print(f"Falha na importação do Json: {e}")
        input()


