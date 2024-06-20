# A program that calculates the expenses for an overseas trip with friends.

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
    

def main():
    friends_list = list_of_users()
    prompt = "Record new transaction?\n(y) or (n)\n"

    # start of calculator sequence
    while True:
        add_new_transaction = str(input(prompt)).strip().lower()
        if add_new_transaction == 'n':
            continue # goes back to beginning of loop and waits for new input
        elif add_new_transaction == 'y':
            print(friends_list)
            process_transaction(friends_list)

def process_transaction(friends_list):
    bill_description = input("Enter a description for the transaction: ").split()
    # gets bill amt
    expense = get_valid_expense()
    # gets name of payor
    payor = get_valid_payor(friends_list)
    # exp_dict containing amt owed
    expense_dict = split_expense(expense, payor, friends_list)

    transaction = Transaction(bill_description, expense, payor, expense_dict)

    clear_terminal()
    print("Transaction recorded successfully", transaction.fulldetails)

def split_expense(expense, payor, friends_list):
    # contains info on who pays who
    # key: A owes B, value: amount to pay B
    exp_dict = {}

    # ask users how they want to split the bill
    prompt1 = "How do you want to split: (e)qually or (d)ifferently\n"
    split_type = get_valid_type(prompt1)

    # split bill equally
    if split_type == 'e':
        amt_per_pax = round(expense / len(friends_list), 2) # divide expense by num of users
        # store owed amt in exp_dict
        for user in friends_list:
            if user != payor:
                exp_dict[f"{user} owes {payor}"] = amt_per_pax # fstring allows optimised formatting such as this, reducing the need for ',' and '+'

    # split by differing proportions
    elif split_type == 'd':
        remaining_expense = expense # so that amt_owed won't be > remaining exp
        for user in friends_list:
            if user != payor:
                print(f"Amount {user} owes {payor}:")
                amt_owed = get_valid_split(remaining_expense) # gets specific amt owed
                exp_dict[f"{user} owes {payor}"] = amt_owed
                remaining_expense -= amt_owed
    return exp_dict
                
def list_of_users():
    # get list of friends
    user_list = []
    print("Enter names of friends (type 'done' when finished): ")
    while True:
        name = input("Name: ").strip()
        if name.lower() == 'done':
            break
        else:
            user_list.append(name)
    clear_terminal()
    print("Friend list: ", user_list)
    return user_list

def get_valid_expense():
    while True:
        try:
            expense = float(input("Enter bill amount: "))
            #conditional checks
            if expense > 0:
                return expense
            else:
                print("Amount must be more than zero. Try again..")
        except ValueError:
            print("Invalid amount. Please enter a number.")

def get_valid_payor(friends_list):
    # ensure that payor name exists in list of frens
    while True:
        payor = input("Enter who paid: ")
        if payor in friends_list: 
            return payor
        else:
            print("Invalid user. Please choose from registered users.")

def get_valid_type(prompt):
    valid_list = ['e', 'd']
    while True:
        type = input(prompt).strip().lower()
        if type in valid_list:
            return type
        else:
            print("Invalid response. Try again..")

def get_valid_split(expense):
    while True:
        try:
            amount = float(input())
            if 0 <= amount <= expense:
                return amount
            else:
                print("Amount out of range. Please enter a valid amount.")
        except ValueError:
            print("Invalid response. Please enter a number")

def clear_terminal():
    # creates 20 newline at terminal
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
