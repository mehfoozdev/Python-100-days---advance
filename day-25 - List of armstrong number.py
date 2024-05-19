# List of Armstrong Numbers

# List of Prime Numbers in a Given Range
# n = int(input('Enter the starting number : '))
# end = int(input('Enter the ending number : '))

for num in range(100, 1000):
    a = num
    s = 0
    
    while a>0:
        d = a % 10
        s = s + d ** 3
        a = a // 10
    
    if s == num:
        print(f"{num} is Armstring number")