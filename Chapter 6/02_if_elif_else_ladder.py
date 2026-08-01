a = int(input("Enter your age: "))

# If Elif Else ladder

if(a>=18):
    print("You are above the age of consent")    #The space before this line is called indendent,it means you are inside if
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("You are below the age of consent") 


print("End of program") 