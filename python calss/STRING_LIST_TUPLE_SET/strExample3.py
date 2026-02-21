# Write a python program to count the number of a in the name.
name=input("Enter name:")
count=0
for i in name:
    if i=='a' or i=='A':
        count+=1
print(f"{name} have {count} no of a")

        
 