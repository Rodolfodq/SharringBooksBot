from bd_credentials import exec_command

sql_user = """CREATE TABLE tb_user(
                    id_user serial,
                    first_name varchar(50),
                    last_name varchar(50),
                    celular varchar(11),
                    CONSTRAINT pk_tb_user PRIMARY KEY(id_user));"""

sql_book = """CREATE TABLE tb_book(
                    id_book serial,                    
                    book_name varchar(50),
                    year integer,
                    author varchar(50),
                    CONSTRAINT pk_tb_book PRIMARY KEY(id_book));"""

sql_loan = """CREATE TABLE tb_loan(
                    id_loan serial,
                    id_user integer,
                    id_book integer,
                    begin_date DATE,
                    coletion_location varchar(70),
                    end_date DATE,
                    delivery_location varchar(70),
                    status varchar(15),
                    CONSTRAINT pk_tb_loan PRIMARY KEY(id_loan),
                    CONSTRAINT fk_tb_user_tb_user FOREIGN KEY(id_user) REFERENCES tb_user(id_user),
                    CONSTRAINT fk_tb_book_tb_book FOREIGN KEY(id_book) REFERENCES tb_book(id_book));"""

sql_alter_user = """ALTER TABLE tb_user
                        ADD COLUMN password VARCHAR(12);"""

sql_alter_user_name = """ALTER TABLE tb_user
                            ADD COLUMN username VARCHAR(12);"""

sql_alter_user_id_owner = """ALTER TABLE tb_book
                            ADD COLUMN id_owner integer;"""

sql_alter_book_owner = """ALTER TABLE tb_book ADD CONSTRAINT fk_tb_user_tb_user
                            FOREIGN KEY(id_owner) REFERENCES tb_user(id_user)
                            ;"""

sql_alter_loan_lender = """ALTER TABLE tb_loan
                            ADD COLUMN id_lender integer;"""

sql_alter_loan_id_lender = """ALTER TABLE tb_loan ADD CONSTRAINT fk_tb_user_tb_loan
                            FOREIGN KEY(id_lender) REFERENCES tb_user(id_user)
                            ;"""

sql_alter_book_name = """ALTER TABLE tb_book ALTER COLUMN book_name TYPE varchar(150)"""

#exec_command(sql_user)
#exec_command(sql_book)
#exec_command(sql_loan)
#exec_command(sql_alter_user)
#exec_command(sql_alter_user_name)
#exec_command(sql_alter_user_id_owner)
#exec_command(sql_alter_book_owner)
#exec_command(sql_alter_loan_lender)
#exec_command(sql_alter_loan_id_lender)
#exec_command(sql_alter_book_name)