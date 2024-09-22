import random
random_number=random.randint(1,19)
print(random_number)
#find random in list
number=[2,4,1,4,6,6,52,2]
random_number=random.choice(number)
print(random_number)
#shuffle list elements
random.shuffle(number)
print(number) 
