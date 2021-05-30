import os
import shutil
import json
from bd_credentials import exec_select

def export_dados(user):
    os.system("cls")
    sql_tb_user = f"SELECT * FROM tb_user WHERE id_user = {user.id}"
    sql_tb_book = f"SELECT * FROM tb_book WHERE id_owner = {user.id}"
    sql_tb_loan = f"SELECT * FROM tb_loan WHERE id_user = {user.id}"

    try:
        tb_user = exec_select(sql_tb_user)
        tb_book = exec_select(sql_tb_book)
        tb_loan = exec_select(sql_tb_loan)        
        print("DADOS COLETADOS COM SUCESSO.")    
    except:
        print("FALHA NA COLETA OS DADOS.")
        return

    try:
        list_user = user_convert(tb_user)
        list_book = book_convert(tb_book)
        list_loan = loan_convert(tb_loan)       

        print("DADOS CONVERTIDOS COM SUCESSO.")        
    except:
        print("FALHA NO TRATAMENTO DOS DADOS.")
        return
    
    path_files = input("INFORME O LOCAL ONDE O ARQUIVO .ZIP SERÁ SALVO: ")
    path_user = os.path.join(path_files, 'tb_user.json')
    path_book = os.path.join(path_files, 'tb_book.json')
    path_loan = os.path.join(path_files, 'tb_loan.json')

    try:    
        cria_json(path_user, list_user)
        cria_json(path_book, list_book)
        cria_json(path_loan, list_loan)
        print("ARQUIVOS .JSON CRIADOS COM SUCESSO.")
    except FileNotFoundError:
        print(f"CAMINHO INFORMADO: {path_files}, NÃO EXISTE. VERIFIQUE NOVAMENTE.")
        input()
        return
    except:
        print("FALHA AO CRIAR OS ARQUIVOS .JSON.")
        input()
        return

    try:
        path_bakup = move_json(path_files)
    except:
        print("FALHA AO MOVER ARQUIVOS .JSON PARA DIRETORIO BACKUP")
        input()
        return
    
    try:      
        cria_zip(path_bakup, path_files)
        input()
        return        
    except:
        print("FALHA AO CRIAR OS ARQUIVOS ZIP.")
        input()
        return
    


def user_convert(tb_user):
    data = {}
    list_user = []
    for usuario in tb_user:
        data['id_user'] = usuario[0]
        data['first_name'] = usuario[1]
        data['last_name'] = usuario[2]
        data['celular'] = usuario[3]
        data['password'] = usuario[4]
        data['username'] = usuario[5]
        list_user.append(data.copy())
    return list_user

def book_convert(tb_book):
    data = {}
    list_book = []
    for book in tb_book:
        data['id_book'] = book[0]
        data['book_name'] = book[1]
        data['year'] = book[2]
        data['author'] = book[3]
        data['id_owner'] = book[4]
        list_book.append(data.copy())
    return list_book

def loan_convert(tb_loan):
    data = {} 
    list_loan = []
    for loan in tb_loan:
        data['id_loan'] = loan[0]
        data['id_user'] = loan[1]
        data['id_book'] = loan[2]
        if loan[3] != None:
            data['begin_date'] = loan[3].strftime("%m/%d/%Y")
        else:
            data['begin_date'] = loan[3]
        data['colection_location'] = loan[4]
        if loan[5] != None:
            data['end_date'] = loan[5].strftime("%m/%d/%Y")
        else:
            data['end_date'] = loan[5]
        data['delivery_location'] = loan[6]
        data['status'] = loan[7]
        data['id_lender'] = loan[8]
        list_loan.append(data.copy())
    return list_loan

def cria_json(path_file, json_data):
    f = open(path_file, "w", encoding='utf-8')
    json.dump(json_data, f, ensure_ascii=False, sort_keys=True, indent=4)
    f.close()    
    
def move_json(path_files):    
    path_bakup = os.path.join(path_files, "backup_sharring_books")
    os.makedirs(path_bakup, exist_ok=True)
    os.system(f"move {path_files}\\tb*.json {path_bakup}")
    return path_bakup

def cria_zip(path_bakup, path_files):
    path_zip = os.path.join(path_files, "backup_sharring_books")
    shutil.make_archive(path_zip, 'zip', path_bakup)    
    shutil.rmtree(path_bakup)
    print(f"ARQUIVO CRIADO COM SUCESSO: {path_zip}.zip")