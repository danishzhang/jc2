dictionary = {"England" : "London", 
              "France" : "Paris", 
              "Germany" : "Berlin"}

# To add another value into the dictionary
dictionary["Indonesia"] = "Jakarta"

# The value of the key is updated
dictionary["England"] = "Brimingham"

# key = input("Enter a key: ")
# if key in dictionary:
#     print(dictionary[key])
# else:
    # print("Not found")

# To print all the entry in the dictionary
for key in dictionary:
    print(key, ":", dictionary[key])


print(dictionary.clear())