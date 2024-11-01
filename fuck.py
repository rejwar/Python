ma

def add_numbers(a,b):
    num1=a
    num2=b

    sum=num1+num2
     sub=num1*num2
      div=num1/num2

    return {"sum":sum,"sub":sub,"div" :div}

result =add_numbers(5,7)+60
print(result)