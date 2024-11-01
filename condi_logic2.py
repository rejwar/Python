year = input("year:")
year = int(year)

if year % 4 ==0 :
    if year % 100 ==0:
        if year % 400 == 0:
          print(year,"This is leapyear")
        
        else:
            print(year,"This is not leap year")
    else:
        print(year, "This is leap year")
else:
    print(year,"This is not leap year")

