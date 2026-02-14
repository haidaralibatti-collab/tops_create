#Assignment Operators
num=int(input("Enter value"))
num=num+5
print(num)
#Using shorthand assignment operators
num+=5
print(num)
num/=5
print(num)
num-=5
print(num)
num*=5
print(num)


#Using shorthand assignment operators with formatted output
num=int(input("Enter value"))
# Initialize num with user input
print(f"{num}", end=" ")
num+=5
print(f"+=5 === {num}")
# Initialize num with user input
print(f"{num}", end=" ")
num-=5
print(f"-=5 === {num}")
print(f"{num}", end=" ")
num*=5
print(f"*=5 === {num}")
print(f"{num}", end=" ")
num/=5
print(f"/=5 === {num}")
print(f"{num}", end=" ")
num%=5
print(f"%=5 === {num}")
print(f"{num}", end=" ")
num//=5
print(f"//=5 === {num}")
print(f"{num}", end=" ")
num**=5
print(f"**=5 === {num}")
