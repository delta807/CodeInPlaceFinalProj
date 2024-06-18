import math

user_list = []

def clear_terminal():
    for i in range(20):
      print('\n')
      
# get list of friends
num_of_user = int(input('How many people to split with: '))
for i in range(num_of_user): 
    user = input("Register a person: ")
    user_list.append(user)

clear_terminal()
print(user_list)

# activate functions
while True:
    prompt = """
Record new transaction?
(y) or (n)
"""

    update_transc = str(input(prompt))
    if update_transc == 'n':
        continue

    elif update_transc == 'y':
        # exp amt
        expense = float(input("Enter expense amt: "))

        # payor
        while True:
            payor = str(input("Enter who paid: "))
            if payor in user_list:
                break
            else:
                print("Invalid user. Try again..")

        # to split
        exp_dict = {}

        # ask how they want to split
        prompt1 = "How do you want to split: (e)qually or (d)ifferently\n"
        how_to_split = input(prompt1)

        if how_to_split == 'e':
            # split equally
            amt_per_pax = expense / len(user_list)
            rounded_amt = round(amt_per_pax, 2)
            for user in user_list:
                if user != payor:
                    key = str(user) + ' owes ' + str(payor)
                    exp_dict[key] = rounded_amt

        elif how_to_split == 'd':
            # split by differing proportions
            for user in user_list:
                if user != payor:
                    print("Amount", user, "owes", payor +": ")
                    value = float(input())
                    key = str(user) + ' owes ' + str(payor)
                    exp_dict[key] = value

        clear_terminal()
        print(exp_dict)
        break




