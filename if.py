#  if文

age = 23
age_alcohol = 20
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drive beer but you can drive only if you have a driver's licence")

if not 0 < age < 120:
    print("The value is invalid!")

# Challenge1
balance = 300000
withdraw = 23000
balance_limit = 1000000
if balance > withdraw:
    balance = balance-withdraw

    print("Your new balance is{}".format(balance))
else:
    print("You don't have money")

# Challenge2
if withdraw > balance_limit:
    print("The withdrawal limit {}".format(balance_limit))
elif balance > withdraw:
    balance = balance-withdraw

    print("Your new balance is{}".format(balance))
else:
    print("You don't have money")


