# python converter

weight = float(input("Eneter Your weight :"))
Unit = input("kilogram or pounds ? (k & l)")

if  unit == "k" :
    weight = weight *2.5 
    unit ="lbs"

elif unit == "l" :
     weight = weight / 2.5
     unit = "kgs."

else :
     print(f"{unit } was not valid " )
     print (f" Your weight is {weight }{unit }" )23445