def check_number(number):
    if number>0:
        print("the number is positive")
    elif number<0:
        print("the number is negative")
    else:
        print("the number is zero")
number=int(input("enter nunber"))
result=check_number(number)
print(result)