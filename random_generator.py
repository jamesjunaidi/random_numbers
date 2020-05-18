import random

print("Enter the min of the range")
min_num_str = input()

print("Enter the max of the range")
max_num_str = input()

print("Enter how many numbers you want")
nums = input()

min_num = int(min_num_str)
max_num = int(max_num_str)

for i in range(int(nums)):
    number = random.randint(min_num, max_num)
    print(str(number) + ",", end ='')



print(" ")




