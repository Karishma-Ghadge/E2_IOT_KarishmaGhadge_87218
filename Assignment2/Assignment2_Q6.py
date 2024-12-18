def concatenate_lists(list1, list2):

    result = []

    for a in list1:
        for b in list2:
            result.append(a + b)
    return result

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output = concatenate_lists(list1, list2)
print(output)