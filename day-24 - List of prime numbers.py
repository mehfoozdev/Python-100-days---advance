# List of Prime Numbers in a Given Range
start = int(input('Enter the starting number : '))
end = int(input('Enter the ending number : '))

for num in range(start, end+1):
    for a in range(2, num):
        if num % a == 0 :
            break
    else:
        print(num, " is a Prime Number")
    
    
