from datetime import datetime
from user import User
from book import Book

class Loan():

    def __init__(self, id_loan, id_user, id_book, collect_location, status):
        now = datetime.now()
        self.id = id_loan
        self.id_user = id_user
        self.id_book = id_book
        self.begin_date = ''
        #self.begin_time = now.strftime("%H:%M:%S")
        self.collect_location = collect_location
        self.end_date = ""
        self.end_time = ""
        self.delivery_location = ""
        self.status = status


