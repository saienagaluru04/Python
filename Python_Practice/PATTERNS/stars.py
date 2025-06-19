# 1.Write a python program to print the below pattern - where n value is 5.
# * 
#   * 
#     * 
#       * 
#         * 
n = int(input("Enter n value: "))
stars = 1
spaces = 0
for row in range(1, n + 1):
    for sp in range(1, spaces+1):
        print(' ',end=' ')
    for st in range(1, stars+1):
        print('*', end=' ')
    print()
    spaces += 1

# 2.Write a python program to print the below pattern - where n value is 5.
#        * 
#       * 
#     * 
#   * 
# *
n = int(input("Enter n value : ")) 
spaces = n-1
stars = 1
for row in range(1, n+1):
    for sp in range(1,spaces+1):
        print(' ', end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces -=1

# 3.Write a python program to print the below pattern - where n value is 5.
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
n = int(input("Enter n value : "))
stars = 1
spaces = n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars += 1
    spaces -= 1

# 4.Write a python program to print the below pattern - where n value is 5.
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
n = int(input("Enter n value : "))
stars = 1
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars += 1

# 5.Write a python program to print the below pattern - where n value is 5.
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
n = int(input("Enter n value : "))
stars = 5
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces += 1
    stars -= 1

# 6.Write a python program to print the below pattern - where n value is 5.
# * * * * *
# * * * *
# * * *
# * *
# *
n = int(input("Enter n value : "))
stars = 5
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars -= 1

