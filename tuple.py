# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("naingkokolin", 21, False, 21)
name, age, stillSingle, girlFriAge = mytuple

print(name)
print(age)
print(stillSingle)
print(girlFriAge)

counter = mytuple.count(21)
print(counter)

print(mytuple.index("naingkokolin"))

mylist = list(mytuple)
print(type(mylist))

my_tuple = tuple(mylist)
print(type(my_tuple))