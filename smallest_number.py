# creating a program for smallest number
print('\n\nA Program to Finding a smallest  number\n\n')

x = int(input('enter the value of x- '))
y = int(input('enter the value of y- '))
z = int(input('enter the value of z- '))
t = int(input('enter the value of t- '))
    
if x<=y and x<=z and x<=t : 
        print('\nx is the smallest number\n')

elif y<=z and y<=x and y<=t :
        print('\ny is the smallest number\n')

elif z<=x and z<=y and z<=t :
        print('\nz is the smallest number\n')

else :
        print('\nt is the smallest number\n')


print('\n\nProgram ends here\n\n')
