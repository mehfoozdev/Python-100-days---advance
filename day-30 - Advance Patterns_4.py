n = int(input('Enter a numbers of rows : '))

for a in range(n, 0, -1):
    for b in range(a): 
        print("*", end='') 
    
    for c in range(2*(n-a)):
        print(" ", end='')
    
    for d in range(a):
        print('*', end='')
        
    print()
    
for a in range(2, n+1):
    for b in range(a): 
        print("*", end='') 
    
    for c in range(2*(n-a)):
        print(" ", end='')
    
    for d in range(a):
        print('*', end='')
        
    print()


#Ulta
# for a in range(n-1,0,-1):
#     for b in range(n-a): 
#         print(' ', end=' ') 
    
#     for c in range(2 * a - 1):
#         print("*", end=' ')
#     print()
    
