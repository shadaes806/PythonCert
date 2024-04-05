print("outside try except else block")

try:
    a = int(input("Enter numerator "))
    b = int(input("Enter numerator "))
    c = a//b
except ZeroDivisionError as err:
    print(err)

else:
    print("The result is",c)
finally:
    print("finally block")

print("over")