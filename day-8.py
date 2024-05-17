a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))

if a == b and b==c:
    print('Triangle is Equilater')
elif a == b or b == c or c == a:
    print("Trianlge is Isosceles")
else:
    print("Triangle is Scalene") 