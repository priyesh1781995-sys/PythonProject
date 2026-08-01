#Q6.Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use key as their names. Assume that the names are unique.

d = {}    # This is an empty dictionary

name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})                # This will update dictionary
name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})                # This will update dictionary
name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})                # This will update dictionary
name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})                # This will update dictionary
name = input("Enter friends name: ")
lang = input("Enter language name: ")

d.update({name:lang})                # This will update dictionary

print(d)


