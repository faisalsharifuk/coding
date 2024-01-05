# Reverse a string using for loop max_index (not slicing)
my_string = "Hello"
reversed_string = ""
max_index = len(my_string) - 1
for i in range(max_index, -1, -1):
    reversed_string += my_string[i]
print(reversed_string)


# while loop
my_number = 0
while my_number < 6:
    my_number += 1
    if my_number == 3:
        continue
    print(my_number)


# for loop
num = 0
while(num != -1):
    num_list = [1, 2, 3, 4, 5]
    found = False
    num = int(input("Input a number from 1 to 10 and find out if it's in our list:"))
    if num<1 or num>10:
        print("Number out of range")
    else:
        for number in num_list:
            if num == number:
                found = True
                break
        print(f'List contains {num}: {found}')


# for loop
for i in range(1,10):
    if i < 3:
        print(i)


# for loop
for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} * {y} = {x*y}")
    print("")
