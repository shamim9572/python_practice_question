set1 = {'a', 'b', 'c'}
set2 = {1, 2, 4, 6}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}


set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

newSet = set1.union(set2,set3,set4)
print(newSet)