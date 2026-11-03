#solution 1 using | operator

dict1 = {"john":89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter":78}

print (dict1 | dict2)

#solution 2 using && operator

dict1 = {"john":89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter":78}

print ({**dict1,**dict2})

# solution 3 using copy()  and update () method

dict1 = {"john":89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter":78}

dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)

