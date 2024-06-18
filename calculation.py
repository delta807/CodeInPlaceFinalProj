# A program that calculates the expenses for an overseas trip with friends.

def main():
    friends_list = list_of_users()
    prompt = """
Record new transaction?
(y) or (n)
"""
# start of calculator sequence
    while True:
        add_new_transc = str(input(prompt))
        if add_new_transc == 'n':
            continue # goes back to beginning of loop and waits for new input

        elif add_new_transc == 'y':
            show_registered_usr(friends_list)

            # gets bill amt
            expense = get_valid_expense()

            # gets name of payor
            payor = get_valid_payor(friends_list)

            # contains info on who pays who
            # key: A owes B
            # value: amount to pay B
            exp_dict = {}

            # ask how users want to split the bill
            prompt1 = "How do you want to split: (e)qually or (d)ifferently\n"
            how_to_split = get_valid_type(prompt1)

            # split bill equally
            if how_to_split == 'e':
                amt_per_pax = expense / len(friends_list) # divide expense by num of users
                rounded_amt = round(amt_per_pax, 2) # round amt to 2 d.p.
                # store owed amt in dict
                for user in friends_list:
                    if user != payor:
                        key = str(user) + ' owes ' + str(payor)
                        exp_dict[key] = rounded_amt

            # split by differing proportions
            elif how_to_split == 'd':
                for user in friends_list:
                    if user != payor:
                        print("Amount", user, "owes", payor +": ")
                        amt_owed = get_valid_split(expense) # gets specific amt owed
                        key = str(user) + ' owes ' + str(payor)
                        exp_dict[key] = amt_owed

            clear_terminal()
            print(exp_dict)

def list_of_users():
    # get list of friends
    user_list = []

    num_of_user = get_valid_int()
    for i in range(num_of_user): 
        user = input("Register a person: ")
        user_list.append(user)

    return user_list

def get_valid_expense():
    while True:
        try:
            expense = float(input("Enter expense amt: "))

            #conditional checks
            if expense <= 0:
                print("Amount cannot less than zero. Try again..")
            else:
                break

        except ValueError:
            print("Not a valid float. Try again..")
    
    return expense

def get_valid_int():
    while True:
        try:
            num = int(input('How many people to split with: '))

            #conditional checks
            if num <= 0:
                print("Not more than zero. Try again..")

            else:
                break

        except ValueError:
            print("Not a whole number. Try again..")
    
    return num

def get_valid_payor(friends_list):
    # ensure that payor name exists in list of frens
    while True:
        payor = str(input("Enter who paid: "))
        if payor in friends_list: 
            break
        else:
            print("Invalid user. Try again..")

    return payor

def clear_terminal():
    # creates 20 newline at terminal
    for i in range(20):
      print('\n')

def show_registered_usr(friends_list):
    # clears terminal and prints list of frens
    clear_terminal()
    print(friends_list)

def how_to_split(expense, payor, friends_list):
    # contains info on who pays who
    # key: A owes B
    # value: amount to pay B
    exp_dict = {}

    # ask how users want to split the bill
    prompt1 = "How do you want to split: (e)qually or (d)ifferently\n"
    how_to_split = get_valid_type(prompt1)

    # split bill equally
    if how_to_split == 'e':
        amt_per_pax = expense / len(friends_list) # divide expense by num of users
        rounded_amt = round(amt_per_pax, 2) # round amt to 2 d.p.
        # store owed amt in dict
        for user in friends_list:
            if user != payor:
                key = str(user) + ' owes ' + str(payor)
                exp_dict[key] = rounded_amt

    # split by differing proportions
    elif how_to_split == 'd':
        for user in friends_list:
            if user != payor:
                print("Amount", user, "owes", payor +": ")
                amt_owed = get_valid_split(expense) # gets specific amt owed
                key = str(user) + ' owes ' + str(payor)
                exp_dict[key] = amt_owed

def get_valid_type(prompt):
    valid_list = ['e', 'd']
    inval_response = "Invalid response. Try again.."

    while True:
        try:
            type = str(input(prompt))

            if type not in valid_list:
                print(inval_response)
            else:
                break

        except ValueError:
            print(inval_response)

    return type

def get_valid_split(expense):
    inval_response = "Invalid response. Try again.."
    out_of_range = 'Amt out of range. Try again..'

    while True:
        try:
            amount = float(input())

            if amount < 0 or amount > expense:
                print(out_of_range)
            else:
                break

        except ValueError:
            print(inval_response)

    return amount


if __name__ == '__main__':
    main()
