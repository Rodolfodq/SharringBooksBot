import psycopg2 as pg

def exec_command(sql):
    try:
        con = pg.connect(
            database="db_sharring_books",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432"
        )       

        cur = con.cursor()
        cur.execute(sql)        
        con.commit()
        con.close()
        return True
    except Exception as erro:
        print(erro)
        return False


def exec_select(sql):
    try:
        con = pg.connect(
            database="db_sharring_books",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432"
        )        

        cur = con.cursor()
        cur.execute(sql)
        linhas = cur.fetchall()
        return linhas
    except Exception as erro:
        print(erro)
    
