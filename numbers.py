#Numbers
a=10
print (a) 

my_income =1000
tax_rate= 0.5
my_taxes= my_income * tax_rate
print(my_taxes)

#comment 
print (a) #comment 

#Strings 
'Hello World '
"I'm a computer"
mystring= 'Hello World!'
print(mystring[0]) #H
print(mystring[2:]) # llo World!
print(mystring[:3]) # Hel
print(mystring[0:5])# Hello
print(mystring[::]) # Hello World!
print(mystring[::2])# HloWrd
print(mystring[::5])# HloWrd


#Slicing 
mystring ='Hello World'
# x =mystring.upper() # upper case 
x=mystring.capitalize()
x= mystring.split('l')
print(x)
#print formating
A= 'Item one :{x} Item Two : {y}'.format(x='apples', y='oranges')
print (A)

#lists 

myList= ['a','b','c','d']
#myList = ['Hellow World',1,2,3,4,5,6,48.35,True, 'ABC',[1,2,3]]
print(myList)
#length
print(len (myList))
print ('before reassignment:')
print (myList)
# Add New Item 
myList[0]='NEW ITEM'
print("after reassignment:")
print(myList)
#append
myList.append("new Item")
print(myList)
#pop Methord 
item = myList.pop(1)
print(myList)
print(item)

#Reverse 

myList.reverse()
print (myList)

#Sort 
myNewList= [4,2,3,5,1]
myNewList.sort()
print(myNewList)
#list comprehension 
matrix =[[1,2,3],[4,5,6], [7,8,9]]
first_col=[row [0] for row in matrix]
print (first_col)

#Dictionaries 

my_stuff= {"key1":123, 'key2': 'value2', 'key3': {'123':[1,2,'grabMe']}}
print (my_stuff['key3'] ['123'][2].upper())
#Adding an item in dictionary 
my_Meals= { 'lunch':'Pizza', 'bfast':'Otmeal'}
my_Meals['lunch']= 'pasta'
my_Meals['dinner']= 'Rice'
print(my_Meals ['lunch'])

print (my_Meals)


# Booleans 
True 
False
# Tuples 
t=(1,2,3)
print(t[0])
myList = ['a',True, 123]
#print (myList)
myList[0]='NEW'
print (myList)


#SETS

x= set()
x.add(1)
x.add(2)
x.add(4)
x.add(.45)
x.add(2)
print(x)