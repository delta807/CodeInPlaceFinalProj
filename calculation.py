# A program that calculates the expenses for an overseas trip with friends.

# clears mess at terminal
def clear_terminal():
    for i in range(20):
      print('\n')

def show_registered_usr():
    clear_terminal()
    print(user_list)

# get list of friends
user_list = []
num_of_user = int(input('How many people to split with: '))
for i in range(num_of_user): 
    user = input("Register a person: ")
    user_list.append(user)

show_registered_usr()

# start of calculator sequence
while True:

    prompt = """
Record new transaction?
(y) or (n)
"""

    update_transc = str(input(prompt))
    if update_transc == 'n':
        continue # goes back to beginning of loop and waits for new input

    elif update_transc == 'y':
        show_registered_usr()

        # gets bill amt
        expense = float(input("Enter expense amt: "))

        # gets name of payor
        while True:
            payor = str(input("Enter who paid: "))
            if payor in user_list: # ensures that payor is valid
                break
            else:
                print("Invalid user. Try again..")

        # contains info on who pays who
        # key: A owes B
        # value: amount to pay B
        exp_dict = {}

        # ask how users want to split the bill
        prompt1 = "How do you want to split: (e)qually or (d)ifferently\n"
        how_to_split = input(prompt1)

        # split bill equally
        if how_to_split == 'e':
            amt_per_pax = expense / len(user_list) # divide expense by num of users
            rounded_amt = round(amt_per_pax, 2) # round amt to 2 d.p.
            # store owed amt in dict
            for user in user_list:
                if user != payor:
                    key = str(user) + ' owes ' + str(payor)
                    exp_dict[key] = rounded_amt

        # split by differing proportions
        elif how_to_split == 'd':
            for user in user_list:
                if user != payor:
                    print("Amount", user, "owes", payor +": ")
                    value = float(input()) # gets specific amt owed
                    key = str(user) + ' owes ' + str(payor)
                    exp_dict[key] = value

        clear_terminal()
        print(exp_dict)





