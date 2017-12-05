print("\nprogram starts here \n\n")
n = int(input("Enter value of n - "))
x = int(input("Enter value of x - "))
y = int(input("Enter value of y - "))
z = int(input("Enter value of z - "))

print("Checking which no. is greatest ")

print("\n\n")


if n >= x and n >= y and x >= z :

    print(n,"is greatest ")
    print("\nFinish")

elif x >= n and x >= y and x >= z :

    print(x, "is greatest")
    print("\nFinish")

elif y >= n and y >= x and y >= z :

    print(y, "is greatest")
    print("\nFinish")

else :
    print(z,"is greatest ")
    print("\nFinish")


print("\n\nBye Bye \n\n")

