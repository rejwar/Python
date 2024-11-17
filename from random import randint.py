from random import randint

guessnumber = int(input("Enter the number :"))
randomnuber =randint(1,5)


if guessnumber == randomnuber:
    print("You won")
   
else:

    print("You have lost ")

    print("Random number is ",randomnuber)