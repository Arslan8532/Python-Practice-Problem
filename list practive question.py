# reverse a list
#usig negative slicing to reverse a list
#create a list
numbers=[]
#insert elements in list
for i in range(0,11):
    numbers.append(i)
print('print the complete list')
print(numbers)
# print the reverse elements of list

print(numbers[::-1])
print(numbers[-1::-1])
numbers.sort(reverse=True)
print(numbers)
#find the maximum element of list

max_element=max(numbers)
print('the maximum element is ')
print(max_element)
#find minimum element in the list

min_element=min(numbers)
print('the minimum element is ')
print(min_element)

#remove duplicate from the list
#create a new list
list_number=[1,2,3,4,1,2,3,6,7]
unique_list=[]
for num in list1:
    if num not in unique_list:
        unique_list.append(num)
print('list with no duplicate',unique_list)