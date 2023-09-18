import math

#1
def maximum():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    
    if a > b  and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)

#2
def medium():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    if (a > b and a < c) or (a > c and a < b):
        print(a)
    elif (b > a and b < c) or (b > c and b < a):
        print(b)
    elif (c > a and c < b) or (c > b and c < a):
        print(c)
    elif a == b or a == c or b == c:
        print('error')

#3
def multiple():
    a = int(input('a: '))
    b = int(input('b: '))

    if a % b == 0:
        print('victory')
    else:
        print('defeat')
        print(a % b)

#4
def location():
    x = int(input('x: '))
    y = int(input('y: '))

    if x > 0 and y > 0:
        print('1')
    elif x > 0 and y < 0:
        print('4')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    else:
        print('center')

#5
def triangle():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    if a < b+c and b < a+c and c < a+b:
        print('yes')
    else:
        print('no')

#6
def circle():
    x = int(input('x: '))
    y = int(input('y: '))

    r = int(input('r: '))

    if math.sqrt(x**2 + y**2) <= r:
        print('yes')
    else:
        print('no')

#7
def square():
    print('1 - rectangle\n2 - triangle\n3 - circle')
    choice = int(input('? '))

    if choice == 1:
        a = int(input('a: '))
        b = int(input('b: '))

        square = a*b
        print(square)
    elif choice == 2:
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))

        p = (a+b+c) / 2
        square = math.sqrt(p * (p-a)*(p-b)*(p-c))
        print(round(square, 2))
    elif choice == 3:
        r = int(input('r: '))

        square = math.pi * r**2
        print(round(square, 2))

#8
def year():
    year = int(input('year: '))

    if year % 4 == 0:
        if year % 100 != 0:
            print('yes')
        else:
            if year % 400 == 0:
                print('yes')
            else:
                print('no')
    else:
        print('no')

#9
def shot():
    shotRange = float(input('range: '))

    if shotRange > 28 and shotRange < 30:
        print('ПОПАЛ')
    elif shotRange >= 30:
        print('ПЕРЕЛЕТ')
    elif shotRange > 0 and shotRange <= 28:
        print('НЕДОЛЕТ')
    else:
        print('НЕ БЕЙ ПО СВОИМ')

#10
def uravnenie():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    d = (b**2) - (4*a*c)

    if d < 0:
        print('no results')
    elif d == 0:
        x = round((-b) / (2*a), 2)
        print(f'x = {x}')
    else:
        x1 = round((-b + math.sqrt(d)) / (2*a), 2)
        x2 = round((-b - math.sqrt(d)) / (2*a), 2)

        if x1 == x2:
            print(f'x1 = x2 = {x1}')
        else:
            print(f'x1 = {x1}\nx2 = {x2}')
