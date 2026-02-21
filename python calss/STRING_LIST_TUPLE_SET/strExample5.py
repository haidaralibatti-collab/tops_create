# This program takes a name as input and rearranges it by moving the first letter to the end of the name.
name=input("Enter name:")
ans = name[-1] + name[1:len(name)-1] + name[0]
print(ans)