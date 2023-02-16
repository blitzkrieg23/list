# List is a collection which is ordered and changeable. Allows duplicate members.

# list = ["abc", 21, True, 40.5, "male"]  #--list with various data types


fruits = ["🍎","🍍","🍋"]

print(fruits[0]) # access individual list
print(fruits[-1]) # get the last element

fruits.append("🍊")
print(fruits)
print(len(fruits))     

# Loop through a list
"""
people = ["John","Michael","Kyle"]

people.sort() # sort the list
people.sort(reverse = True) # reverse sort

for x in people:
    print(x)

"""