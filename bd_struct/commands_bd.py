from bd_credentials import exec_command

sql_user = "INSERT INTO tb_user (first_name, last_name, celular, password, username) values('Maria', 'Silva', '16992451375', 'admin123', 'silva')"

exec_command(sql_user)