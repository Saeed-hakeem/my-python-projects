def greatNum(numbers):       #parameteriuzed function
    greater = numbers[0]     # Initialize largest with the first element
    for num in numbers:
        if num > greater:
            greater = num
    return greater
Numlist = [100, 200, 500, 3500, 5000]
greater_number = greatNum(Numlist)
print("The greater number in numlist list is:", greater_number)


def repNum(numbers):       #parameteriuzed function
    repeated = numbers[0]     # Initialize rep with the first element
    for num in numbers:
        if num > 2:
            repeated = num
    return repeated

my_list = [100, 200, 100, 500, 3500, 5000]
repeated_number = repNum(my_list)
print("repeated number:", repeated_number)

print(my_list)


#exercise 3
Numtuple = (100, 200, 500, 3500, 5000)
mylist = list(Numtuple)
mylist[1]=1000
Numtuple = tuple(mylist)
print(Numtuple)



