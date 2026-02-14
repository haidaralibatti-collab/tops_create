age= int(input("Enter Age "))
weight= int(input("Enter Weight "))
if age>18:
    if weight>50:
        print("You are eligible to donate blood")
    else:
        print("Due to under weight user can not donate blood")
else:
    print("Not eligible to donate blood")