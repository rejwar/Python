def weekday(n):
    match n :
        case 0 : return "Monday"
        case 1 : return "Tuesday"
        case 2 : return "Wednesday"
        case 3 : return "Thursday"
        case 4 : return "Friday"
        case 5 : return "Saturday"
        case 6 : return "Sunday"
        case _ : return "wrong day"
print(weekday(3))
print(weekday(5))
