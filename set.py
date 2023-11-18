set1 = {'apple','banana','cherry','guava','papaya','lichi'}
print(type(set1))
# access set item
print('apple' in set1)
# add item
set1.add('coconut')
print(set1)
# add set
set2 = {'mango','graps','pineapple'}
set1.update(set2)
print(set1)
# add iterable
set3 = ['kiwi']
set1.update(set3)
print(set1)
# remove item
set1.remove('apple')
print(set1)
s = set1.pop() #another way 
print(s)
print(set1)
