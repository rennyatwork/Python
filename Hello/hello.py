msg ="Hello world!"
print(msg)
msg.capitalize()
# print("msg.capitalize(): ", msg.capitalize())
print("oi")

print "5 % 2 = ", 5%2

nameList = ["Joe", "Clyde", "Isaac"]

print (nameList)
print (nameList[0])

print ('Interest calculator')
amount = float(input('Principal amount?'))
roi = float(input('Rate of interest?'))
years = int(input('Duration (years)?' ))
total = (amount* pow(1+ (roi/100), years))
interest = total - amount
print('\n Interest = %0.2f' %interest)