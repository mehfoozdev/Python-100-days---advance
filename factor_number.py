num = int(input('Enter a number : '))
a=1

for a in range(1, num+1):
    if num % a == 0:
        print(a)