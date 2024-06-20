# A program that calculates the expenses for an overseas trip with friends.

from transaction import *
from database import *

def main():
    setup_database()
    friends_list = list_of_users()
    transactions = Transaction.load_from_db()
    
    while True:
        action = input("Choose an action: (n)ew transaction, (v)iew transactions, (e)dit transaction, (r)emove transaction, (s)ummary, (q)uit\n").strip().lower()
        
        if action == 'n':
            print(friends_list)
            process_transaction(friends_list, transactions)
        elif action == 'v':
            list_transactions(transactions)
        elif action == 'e':
            edit_transaction(transactions, friends_list)
        elif action == 'r':
            remove_transaction(transactions)
        elif action == 's':
            show_summary(transactions)
        elif action == 'q':
            break
        else:
            print("Invalid input. Please choose one of the above options.")

def list_of_users():
    user_list = []
    print("Enter the names of friends (type 'done' when finished):")
    while True:
        name = input("Name: ").strip()
        if name.lower() == 'done':
            break
        if name:
            user_list.append(name)
    clear_terminal()
    print("Friends List:", user_list)
    return user_list

def process_transaction(friends_list, transactions_list):
    transaction_description = input("Enter the transaction description: ").strip()
    # get bill amt
    expense = get_valid_expense()
    # gets payor name
    payor = get_valid_payor(friends_list)
    # contains {who owes payor: amt owed}
    exp_dict = split_expense(expense, payor, friends_list)
    
    transaction = Transaction(transaction_description, expense, payor, exp_dict)
    transactions_list.append(transaction)
    transaction.save_to_db()
    
    clear_terminal()
    print("Transaction recorded:", transaction)

def list_transactions(transactions):
    # list all recorded transactions
    if not transactions:
        print("No transactions found.")
        return
    for id, transaction in enumerate(transactions):
        print(f"{id}: {transaction}")
    print()

def edit_transaction(transactions, friends_list):
    list_transactions(transactions)
    transaction_id = get_valid_transaction_id(len(transactions))
    if transaction_id is not None:
        transaction = transactions[transaction_id]
        transaction.edit_transaction(friends_list)
        with conn:
            c.execute('''UPDATE transactions SET 
                      description = :description,
                      expense = :expense, 
                      payor = :payor, 
                      split = :split 
                      WHERE id = :id''', {'id': id, 'description': transaction.description, 'expense': transaction.expense, 'payor': transaction.payor, 'split': transaction.splitAmt})         
            conn.commit()
    else:
        print("Invalid transaction ID.")

def remove_transaction(transactions):
    list_transactions(transactions)
    transaction_id = get_valid_transaction_id(len(transactions))
    if transaction_id is not None:
        transaction = transactions.pop(transaction_id)
        with conn:
            c = conn.cursor()
            c.execute('DELETE FROM transactions WHERE id = ?', (transaction_id + 1,))
            conn.commit()
        print("Transaction removed successfully.")
    else:
        print("Invalid transaction ID.")

def get_valid_transaction_id(max_id):
    while True:
        try:
            transaction_id = int(input("Enter the transaction ID to edit/remove: "))
            if 0 <= transaction_id < max_id:
                return transaction_id
            else:
                print("Invalid ID. Please enter a valid transaction ID.")
        except ValueError:
            print("Invalid response. Please enter a number.")

def show_summary(transactions):
    summary = {}
    for transaction in transactions:
        for key, value in transaction.split.items():
            if key in summary:
                summary[key] += value
            else:
                summary[key] = value
    
    if not summary:
        print("No debts recorded.")
        return
    
    print("Summary of who owes who money:")
    for key, value in summary.items():
        print(f"{key}: {value}")
    print()

def clear_terminal():
    # creates 20 newline at terminal
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
