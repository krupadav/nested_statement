a = int(input('Enter the 1st side:'))
b = int(input('Enter 2nd side:'))
c = int(input('Enter 3rd side:'))
if (a + b + c) == 180:
    if (a == 90) or (b == 90) or (c == 90):
        if (a == b) or (b == c) or (a == c):
            print('Isosceles right triangle')
        else:
            print('Right angle triangle')
    elif a == b == c:
        print('Equilateral triangle')
    elif (a == b) or (b == c) or (a == c):
        print('Isosceles triangle')
    else:
        print('Skelen triangle')
else:
    print('not a valid triangle')
