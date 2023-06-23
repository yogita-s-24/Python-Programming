#Day-11
# Dictionaries are used to store data values in Key:value pairs
# we used {} for dictionary 

# Syntax :

# dictionary_name = { key1 : value1, key2 : value2, ......}

#Example :


phoneBook = {
    "Dolly" : "1234567890",
    "Anu" : "9876543210",
    "Avinash" : "21323422222",
    "Pooja" : "878975457"
}
# print(phoneBook)
#print(phoneBook["Pooja"])
print("Anu =",phoneBook["Anu"])

# Output : Anu = 9876543210

#Example 2:

phoneBook = {
    "Dolly" : "1234567890",
    "Anu" : "9876543210",
    "Avinash" : "21323422222",
    "Pooja" : "878975457"
}
print(phoneBook.get("Avinash"))

#get() method is used to read the value

# Output : 21323422222

#Example 3:

phoneBook = {
    "Dolly" : "1234567890",
    "Anu" : "9876543210",
    "Avinash" : "21323422222",
    "Pooja" : "878975457"
}

name = input("Enter name to find mob no :")
mobile = phoneBook.get(name)
print("Mobile Number :",mobile)

# Output : 
# Enter name to find mob no :Pooja
# Mobile Number : 878975457


#Example : 5

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses.keys())

#Output : dict_keys(['C', 'C++', 'Python', 'DSA', 'ICP', 'ICGP'])


#Example : 6

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses.values())

#Output : dict_values(['499', '499', '499', '999', '999', '10,000'])


#Adding new Key

#Example : 7

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses)
courses["Java"] = "499"
print(courses)

#Output : 
# {'C': '499', 'C++': '499', 'Python': '499', 'DSA': '999', 'ICP': '999', 'ICGP': '10,000'}
# {'C': '499', 'C++': '499', 'Python': '499', 'DSA': '999', 'ICP': '999', 'ICGP': '10,000', 'Java': '499'}


# for Update value

#Example : 8

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses)
courses["Python"] = "999"
print(courses)

#Output : 
# {'C': '499', 'C++': '499', 'Python': '499', 'DSA': '999', 'ICP': '999', 'ICGP': '10,000'}
# {'C': '499', 'C++': '499', 'Python': '999', 'DSA': '999', 'ICP': '999', 'ICGP': '10,000'}


# for clear element

#Example : 9

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000",
    'Java': '499'
}
print(courses)
courses.clear()
print(courses)

# Output : {'C': '499', 'C++': '499', 'Python': '499', 'DSA': '999', 'ICP': '999', 'ICGP': '10,000', 'Java': '499'}
#{}