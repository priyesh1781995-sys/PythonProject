
for i in range(100):
    if( i== 34):
        break         # Exit the loop right now
    print(i)



for i in range(100):
    if( i== 34 ):
        continue      # Skip this iteration. Iteration means value of i, yani yah 34 ko skip kar dega
    print(i)

# Another example 
for i in range(4):
    print("printing")
    if i == 2:        # if i is 2, the iteration is skipped
        continue
    print(i)

