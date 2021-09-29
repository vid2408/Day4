a=5
b=0

try:
    print("resource open")
    print(a/b)

except ZeroDivisionError as e:
    print("Hey you can not divide a number by zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong...")

finally:
    print("resource closed")