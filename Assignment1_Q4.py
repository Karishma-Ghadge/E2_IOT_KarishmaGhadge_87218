num = int(input("Enter 4 digit number : "))

orignal = num
rem = 0
rev = 0

units = num % 10;       
num = num // 10;

tens = num % 10;      
num = num // 10;

hundreds = num % 10;     
num = num // 10;

thousands = num % 10; 

print("Face value of number : ")
print(f"{thousands}  {hundreds}  {tens}  {units}")

print("Place value of number : ")
print(f"{thousands}000  {hundreds}00  {tens}0  {units}")

while orignal != 0:
    rem = orignal % 10
    rev = rev * 10 + rem
    orignal = orignal // 10

print("Reversal of number : ")
print(rev) 