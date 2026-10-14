print("---calculator----")
print("enter operand A")
a = float(input())
print("enter operand B")
b = float(input())
print("enter operation(+,-,*,/)")
op = input()
if op == "+":
    print("result:", a + b)
elif op == "-":
    print("result:", a - b)
elif op == "*":
    print("result:", a * b)
elif op == "/":
    if b == 0:
        print("error")
    else:
        print("result:", a / b)
else:
    print("invalid operation")