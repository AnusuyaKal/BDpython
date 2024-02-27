# def reverse_string(s):
#     reversed_str = ""
#     for i in range(len(s) - 1, -1, -1):
#         reversed_str += s[i]
#     return reversed_str

# # Test the function
# original = "Hello, world!"
# reversed = reverse_string(original)
# print("Original string:", original)
# print("Reversed string:", reversed)

# str1 = "Hello Python"

# def reversestr(strr):
#     the_string = ""
#     for i in strr:
#         the_string += i
#     return the_string

# print(reversestr(str1))

# from collections import OrderedDict

# def list_to_set_with_order(lst):
#     return list(OrderedDict.fromkeys(lst))

# lst = [1, 1, 2, 5, 5, 3, 6, 2, 1, 1, 3, 7, 5, 5, 3]
# my_set = list_to_set_with_order(lst)
# print(my_set)



# lst = [1, 1, 2, 5, 5, 3, 6, 2, 1, 1, 3, 7, 5, 5, 3]
# def remove_duplicate(lst):
#     return list(dict.fromkeys(lst))

# print(remove_duplicate(lst))


def remove_duplicates(lst):
    result = []
    seen = {}
    for num in lst:
        if num not in seen:
            result.append(num)
            seen[num] = True
    return result

lst = [1, 1, 2, 5, 5, 3, 6, 2, 1, 1, 3, 7, 5, 5, 3]
result = remove_duplicates(lst)
print(result)