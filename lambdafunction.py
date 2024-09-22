
# def is_even(number):
#     return number%2==0
numbers=[2,3,4,1,3,5,67,7,3,6]
# #filter(function,iterable)
# filter_numbers=filter(is_even,numbers)
# filter_numbers_list=list(filter_numbers)
# print(filter_numbers_list
filter_numbers=filter(lambda x:x%2==0,numbers)

print(list(filter_numbers))