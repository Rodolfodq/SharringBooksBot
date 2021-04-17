from model.user import User
from model.book import Book
from model.loan import Loan
import time
joao = User(123, "Joao", "Silva")

code = Book(12, "Clean Code", 2017, "Uncle Bob")

loan = Loan(1, joao, code, "Ribeirão Preto")

print(loan.begin_date)
print(loan.begin_time)

loan.finish_loan("Sertãozinho")
print(loan.end_date)
print(loan.end_time)

time.sleep(10)
loan.finish_loan("Rio Preto")
print(loan.end_date)
print(loan.end_time)