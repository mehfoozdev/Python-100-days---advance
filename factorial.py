num = int(input('Enter a number : '))

p = 1

for a in range(num, 0, 1):
    p = p*a   # p *= a
    
print(f'Factorial of {num} is {p}')