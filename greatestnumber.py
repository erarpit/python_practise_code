print('largest number among four numbers')

x =  int(input("enter the value of x - "))
y =  int(input("enter the value of y - "))
z =  int(input("enter the value of z - "))
t =  int(input("enter the value of t - "))

if x>=y and x>=z and x>=t :
    print('x is the greatest number')
elif y>=z and y>=t and y>=x :
    print('y is the gratest number')
elif z>=x and z>=y and z>=t :
    print('z is the greatest number')
else :
    print('t is the greatest number')

