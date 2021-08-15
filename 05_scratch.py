not not 49 % 7

notfloat = int(input("Which integer? "))

notnumber = int(input("Which integer? "))


test_list = [1, 3, 5, 6, 7, 0, 2]
test_list

test_list[-3:] + test_list[:-3]

sorted(test_list, reverse=True)
test_list

test_list.sort(reverse=True)
test_list

# Sort list of lists by the 2nd element in each sub-list
test_list2 = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
def second_sort(list1):
    return list1[1]

test_list2.sort(key=second_sort)
print(test_list2)
# Success!!


# Tuples
x = (1, 2, 4)
sorted(x)

# z contains y, a mutable list
y = [1, 2]
z = (1, 2, y)
print(z)

# z changes when the elements of y change
y[:] = [4, 6]
print(z)

y = [1, 2]
z = (1, 2, y)

# z does NOT change when y is reassigned to an entire new list
y = [4, 6]
print(z)
# At this point, z no longer relies on y

# Tuple of tuples
a = (1, 2, 3)
b = (a, 5, 7)
print(b)

a = (8, 9, 10)
print(b)
# b is unaffected by a change in a, since a was a tuple (and must be immutable from the perspective of b)
b = (a, 5, 7)
print(b)
# b is recreated with the new a active, so it makes a new tuple with the new version of a. This isn't mutation, but complete reassignment.


# Breaking up strings
word_list = list("Hello")
word_tuple = tuple("World")
# Also works with set(), although the default sort order is hard to figure out
word_set = set("Hello World")
sorted(word_set)

# Should have 6 elements
len(set([1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)]))

set1 = set([1, 2, 3])
set1
set1.add(7)
set1
set1.add(2)
set1
# Adding an existing element to a set doesn't give an error, and doesn't change the set