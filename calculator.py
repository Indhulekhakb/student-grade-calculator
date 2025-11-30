num1=int(input())
num2=int(input())
op=input()
if op == "+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op=="/":
    if num2 == 0:
        print("Not defined")
    else:
        print(num1/num2)
elif op == "//":
    if num2 == 0:
        print("Not defined")
    else:
        print(num1//num2)
elif op == "%":
    if num2 == 0:
        print("Not defined")
    else:
        print(num1%nu2)
elif op == "**":
    if num2==0:
        print("Not defined")
    else:
        print(num1**num2)
else:
    print("wrong operator")