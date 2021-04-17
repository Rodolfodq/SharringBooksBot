from datetime import datetime
from model.user import User
from model.book import Book

class Loan():

    def __init__(self, id_loan, User, Book, collect_location):
        now = datetime.now()
        self.id = id_loan
        self.id_user = User.id
        self.id_book = Book.id
        self.begin_date = now.strftime("%d/%m/%Y")
        self.begin_time = now.strftime("%H:%M:%S")
        self.collect_location = collect_location
        self.end_date = ""
        self.end_time = ""
        self.delivery_location = ""
        self.finish = False

    def finish_loan(self, delivery_location):
        now = datetime.now()
        if(not self.finish):
            self.finish = True
            self.end_date = now.strftime("%d/%m/%Y")
            self.end_time = now.strftime("%H:%M:%S")
            self.delivery_location = delivery_location
        else:
            pass

