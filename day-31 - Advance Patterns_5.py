n = int(input('Enter a numbers of rows : '))

# for a in range(1, n+1):
#     for b in range(1, n+1): 
#         if a == b or a+b == n+1 : #if a == b or a+b == n+1 or a==1 or a==n or b==1 or b==n:
#             print('*', end='')
#         else:
#             print(' ', end=' ') 
    
#     print()

for a in range(1, n+1):
    for b in range(1, n+1): 
        if (a == b) or (a+b == n+1) or (a ==1 ) or (a == n) or (b == 1) or (b == n):
            print('*', end=' ')
        else:
            print(' ', end=' ') 
    
    print()