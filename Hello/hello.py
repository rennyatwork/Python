msg ="Hello world!"
print(msg)
msg.capitalize()
# print("msg.capitalize(): ", msg.capitalize())
print("oi")

print ("5 % 2 = ", 5%2)

nameList = ["Joe", "Clyde", "Isaac"]
positionList = ["DBA", "Dev", "SA", "QA"]

mergedList = [nameList, positionList]
print (mergedList)

print("max mergedList")
print(max(mergedList))

print (nameList)
print (nameList[0])

monTuple =(1,2,3,4)
# monTuple[0]=11 #ERROR! tuple object does not support item assignment
newList=list(monTuple)
newList[3]=5


#list
print(newList) # list: [1,2,3,4]
newTuple = tuple(newList)

#tuple
print(newTuple)  # tuple (1,2,3,4)

#dictionary
monDic={"k1":"fulano", "k2": 33, 3:"bla bla"}
print(monDic)

print ('Interest calculator')
amount = float(input('Principal amount?'))
roi = float(input('Rate of interest?'))
years = int(input('Duration (years)?' ))
total = (amount* pow(1+ (roi/100), years))
interest = total - amount
print('\n Interest = %0.2f' %interest)