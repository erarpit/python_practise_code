print("\n\n\nprogram starts here \n")
print('program to check wheather  number is odd or even\n\n')
x = int(input('enter the number - '))
y = int(input('enter the number - '))

if ( x%2 == 0 ) :
    
    if ( y%2 == 0 ) :

        print("\nBoth ",x," and ",y," are even")

    else :

        print("%d is even and %d is odd"%(x,y))


else:

    if ( y%2 == 0 ):

        print(x,"is odd and ",y,"is even")
    else :
        print(x,"is odd and ",y,"is also odd")

print("\n\n\nProgram ends here\n\n\n")
