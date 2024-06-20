# contains class
 
from database import *

class Transaction:
    def __init__(self, description, expense, payor, splitAmt):
        self.description = description
        self.expense = expense
        self.payor = payor
        self.splitAmt = splitAmt

    def __repr__(self): 
        return f"Transaction('{self.description}', {self.expense}, '{self.payor}', {self.splitAmt})" 
    
    def __str__(self): 
        return f"Description: {self.description}\nExpense: {self.expense}\nPayor: {self.payor}"
    
    @property 
    def fulldetails(self):
        return f"Description: {self.description}\nExpense: {self.expense}\nPayor: {self.payor}\n Split: {self.splitAmt}"
    
    @fulldetails.setter
    def fulldetails(self, friends_list):
        pass

    @fulldetails.deleter
    def fulldetails(self):
        print(f"Transaction - {self.description} removed!")
        self.description = None
        self.expense = None
        self.payor = None
        self.splitAmt = None

    def save_to_db(self):
        with conn:
            c.execute("INSERT INTO transactions VALUES (:id, :description, :expense, :payor, :owe)", 
                  {'id': id, 'description': self.description, 'expense': self.expense, 'payor': self.payor, 'owe': self.splitAmt})
            conn.commit()

    @staticmethod
    def load_from_db():
        transactions_list = []
        with conn:
            c.execute('SELECT * FROM transactions')
            all_details = c.fetchall()
            for detail in all_details:
                transaction = {
                    "description": detail[1],
                    "expense": detail[2],
                    "payor": detail[3],
                    "split": detail[4]
                    }
                transactions_list.append(transaction)
        return transactions_list
    