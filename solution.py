#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)



num = int(input("enter a number? \n"))

list_range = list(range(1,num+1))

divisor_list=[]
for x in list_range:
    if num % x == 0:
        divisor_list.append(x)

print(divisor_list)

#can also be done in one line

print([x for x in list_range if num % x == 0 ])
