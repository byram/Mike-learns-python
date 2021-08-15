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
