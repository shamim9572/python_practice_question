#tuple = ("Apple", "banana", "Book", "car")

#print(list)

# if i check the length of tuple
# print(len(list))

# tuple = ("apple",)
# print(type(tuple))

# NOT a tuple
# tuple = ("apple")
# print(type(tuple))

# Change the tuple value

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
