# Demonstration of identity operators
num1=12
num2=301
num3=num1
num4=12
num5=num1+num3
print(num1 is num2)
print(num1 is num3)
print(num1 is num4)
print(num1+num3 is num5)
print(id(num1))
print(id(num2))
print(id(num3))
print(id(num4))
print(id(num5))