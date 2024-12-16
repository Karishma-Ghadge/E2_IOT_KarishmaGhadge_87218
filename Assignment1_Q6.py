#function to calculate the factorial of the given number
fact = 1
def function1(num):
    print(f"num = {num}")
    global fact
    if num < 0:
        print(f"The number is negative,please enter the positive number")
    elif num == 0:
        print(f"The number is equal to zero")
    else:    
        i = 1
        while i <= num:
            fact = fact * i
            i = i + 1
    print(f"Factorial : {fact}")
function1(5)            