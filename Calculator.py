num1 = input("First value " )
operator_sign = input("operation ")
num2 = input("Second value  ")

num1 = int(num1)
num2 = int(num2)
if operator_sign == "+":
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif operator_sign == "-":
    print("{} - {} = {}".format(num1,num2,num1-num2))
elif operator_sign == "*":
    print("{} * {} = {}".format(num1,num2,num1*num2))
elif operator_sign == "/":
    print("{} / {} = {}".format(num1,num2,num1/num2))
elif operator_sign == "%":
    print("{} % {} = {}".format(num1,num2,num1%num2))
else:
    print(" Kindly use the correct operator for calculation ")




