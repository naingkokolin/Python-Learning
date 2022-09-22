from argparse import MetavarTypeHelpFormatter
from cgi import print_arguments
from mailcap import findmatch


mylist = ['apple', 'orange', 'pineapple']
print(mylist)

if "apple" in mylist:
    print(True)
else:
    print(False)

mylist.append("lemond")   # add an item at the end of list
print(mylist)

a=mylist.index("orange")  # return index no if there is item in list
print(a)

findmypineapple=mylist.index("pineapple", 0, 3)
print(findmypineapple)

mylist.insert(1,"strawberry")
print(mylist)

mylist.sort()
print(mylist)

mylist.clear()
print(mylist)