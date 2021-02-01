phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

print()
print("*****  start section 1 - print dictionary ********")
print()

# print(phonebook)


print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()

print(phonebook["Chris"])  # will print the value, the phonenumber
# print(phonebook["Joes"])  # will yield a key error because no Joe in dictionary

if "Chris" in phonebook:
    print(phonebook["Chris"])
else:
    print("Chris not there")


print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

phonebook["Chris"] = "555-9876"  # changes Chris's phone
phonebook["Joe"] = "555-5632"  # will add Joe to the phonebook
print(phonebook)

print()
print("*****  end section 3 ********")
print()


print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]
print(phonebook)
num_items = len(phonebook)  # yields #things in dictionary

new_dict = {}  # empty dictionary


print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys ********")
print()

for k in phonebook:
    print(phonebook[k])  # prints names of 3 keys... Chris, Katie, Joanne


print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()

for v in phonebook.values():
    print(v) 

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()


for pair in phonebook.items(): #cycles through key and value
    print(pair) #will print a tuple of form ('Chris','553-4242')
    print(type(pair)) #prints <class 'tuple'>


print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using random and converting to list ********")
print()




print()
print("*****  end section 8 ********")
print()
