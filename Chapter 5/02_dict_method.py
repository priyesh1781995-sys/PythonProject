marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

#print(marks.items())       # This will give list of keys-value-pairs

#print(marks.keys())        # This will give keys of marks, jo LHS mein hote hai une keys bolte hai aur jo RHS mein hote hai unhe values bolte hai

#print(marks.values())      # This will print values of marks, e.g. RHS side wale list

#marks.update({"Harry": 99}) # This will update marks of Harry, because dictionary is mutable. 
#print(marks)                # This will print updated marks

#marks.update({"Harry": 99, "Renuka": 100})   # This will add another student Renuka also
#print(marks)

#print(marks.get("Harry"))    # This will fetch Harry's marks
#print(marks["Harry"])        # This will also fetch Harry's marks

print(marks.get("Harry2"))    # This will return none
print(marks["Harry2"])        # This will give error

