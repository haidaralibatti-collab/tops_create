# convert country name into upper case
lst_country=['india','usa','uk','canada']
for i in lst_country:
    print(i.upper())
print(lst_country[1])   

print(lst_country)
print(lst_country[1:])
print(lst_country[0][2])
#convert contry name into upper case if country name is having more then 5 letters
for i in lst_country:
    if len(i)>5:
        print(i.upper())
