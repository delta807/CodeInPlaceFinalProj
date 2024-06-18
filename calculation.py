import math

"""    
user1 = 'john'
user2 = 'perry'
user3 = 'mike'

user_list = [user1, user2, user3]"""

user_list = []

# get list of friends
num_of_user = int(input('How many people to split with: '))
for i in range(num_of_user): 
    user = input("Register a person: ")
    user_list.append(user)

print(user_list)

# activate functions
while True:
    prompt = """
Record new transaction?
(y) or (n)
"""

    update_transc = str(input(prompt))
    if update_transc == 'y':
        break


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
            exp_dict[key] = amt_per_pax

elif how_to_split == 'd':
    # split by differing proportions
    for user in user_list:
        if user != payor:
            print("Amount", user, "owes", payor +": ")
            value = float(input())
            key = str(user) + ' owes ' + str(payor)
            exp_dict[key] = value


print(exp_dict)





