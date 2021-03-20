x = int(input("Please enter the first integer:"))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')
a = float(input("Enter the marks"))
if a < 40:
    print('Fail')
elif a >= 40:
    a = 50
    print('D')
elif a >= 50:
    a = 60
    print('C')
elif a >= 60:
    a = 70
    print('B')
elif a >= 70:
    a = 100
    print('A')
else:
    print('Invalid Entry')

