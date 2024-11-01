def multiplication_table(n):
    for i in range(1,10):
        print("{} * {} = {}".format(n,i,n*i))

n = input("enter a number (0 to exit):")
n =int(n)

while n !=0:
 multiplication_table(n)
 print(" ")
 n =input("Enter a number (0 to exit):")
 n = int(n)



 