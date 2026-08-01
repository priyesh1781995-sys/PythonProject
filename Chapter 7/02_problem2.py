#Q2.Write a program to greet all the persons name stored in a list 'l' and which starts with S.
#   l = ["Harry","Soham","Sachin","Rahul"]


l = ["Harry","Soham","Sachin","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}") 

        
