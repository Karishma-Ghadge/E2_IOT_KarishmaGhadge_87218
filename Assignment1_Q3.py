#To find the maximum of three numbers using function


def function1(num1,num2,num3):
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")
    print(f"num3 = {num3}")
    max = 0
    if (num1 > num2) & (num1 > num3):
        print(f"num1 is the greatest of the given three numbers")
        max = num1
    elif (num1 < num2) & (num2 > num3):
        print(f"num2 is the greatest of the given three numbers")
        max = num2
    elif (num1 < num3) & (num3 >num2):
        print(f"num3 is the greatest of the given numbers")
        max = num3
    else:
        print(f"All the given numbers are equal")
        max = num1
    print(f"The maximum number is : {max}")

function1(234,56,12)  
              
