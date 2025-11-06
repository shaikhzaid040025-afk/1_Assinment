# program to do basic math operations

num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))

add= num1+num2
sub= num1-num2
mul= num1*num2

if num2!=0:
    div =num1/num2
else:
    div ="cannot divide by zero"

print("addition =",add)
print("subtraction =",sub)
print("multiplication =",mul)
print("division =",div)
