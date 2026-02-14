age= int(input("Enter Age "))
license= input("Do you have driving license ")
if age>18:
    if license=="Yes":
        print("User is eligible for license")
    else:
        print("User is not eligible for license , User doesn't have driving license")
        