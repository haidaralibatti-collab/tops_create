
month= input("Enter month name: ")
if month in ("January", "March", "May", "July", "August", "October", "December"):
    print(f"{month} has 31 days")

elif month in ("April", "June", "September", "November"):
    print(f"{month} has 30 days")

elif month in ("February"):
    print(f"{month} has 28 days")

else:
    print("Invalid month name")
    