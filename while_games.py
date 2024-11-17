secret_number = 5 
guess_count =1 
guess_limit =3

while guess_count<guess_limit:
    user_guess_number = int(input("Guess>"))

    guess_count +=1

    if user_guess_number ==secret_number:
    
     print("You won !!")
     break
else:
   print ("You lose !")