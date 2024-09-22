#with using a list comprehension
numbers=[]
for i in range(0,15,2):
    numbers.append(i)
     
print(numbers)
#using list comprehension
numbers=[i**2 for i in range(0,12)]
print(numbers)

#another example

numbers=[x for x in range(1,11)]
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print('hj')
desending_order=sorted(numbers,reverse=True)
print(desending_order)
print('print the whole list')
numbers.sort()
print(numbers)
numbers.remove(10)
print(numbers)
remove_element=numbers.pop(8)
print('the remove element is',remove_element)
print(numbers)
print(type(numbers))

#without using a list comprehension

list1=[]
for i in range(0,11):
    list1.append(i**2)
print(list1)

#using list comprehension means functional style coding

list2=[item**2 for item in range(0,11)]
print(list2)

#using a generator expression
squares_gen = (x**2 for x in range(5))
print(squares_gen)
#iterate square_gen
print('Print the value of squares_gen using for loop  num is a iterator')
for num in squares_gen:
    print(num)



#find the sum of elements in list
sum=0
numbers=[2,4,5,76,8,785]
for i in numbers:
    sum+=i
print(sum)

#using for loop to reverse the string
name='arslan'
reverse_string=name[::-1]
print(reverse_string)