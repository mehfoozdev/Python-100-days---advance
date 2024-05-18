#Sum of Series

x = int(input('Enter a number x : '))
n = int(input('Enter a number n: '))
s = 0
f = 1

for a in range(1, n+1):
    f *= a
    s += x**a/f
print(f'Factorial {f} and sum {round(s, 2)}')



# def f(x,l=[]):

#     for i in range(x):

#         l.append(i*i)

#     print(l)

# f(3)

#Find largest number;

# n1 = int(input("Enter an number 1 : "))
# n2 = int(input("Enter an number 2 : "))
# a = n3 = int(input("Enter an number 3 : "))

# if (n1>n2) and (n2>n3):
#     print(f'{n1} is greater than {n2} and {n3}')
# elif(n1<n2) and (n2<n3):
#     print(f"{n3} is geather than {n1} and {n2}")
# elif(n2>n1) and (n2>n3):
#     print(f"{n2} is geather than {n1} and {n3}")
# else:
#     print('invalid input')


#sum of list
# a = [3,4,5,6,7,10]
# sum_a = 0

# for i in a:
#     sum_a += i
#     print(i, sum_a)
# print("sum of numbers is : ", sum_a)

# print("Sum of list old : ", sum(a))    
    