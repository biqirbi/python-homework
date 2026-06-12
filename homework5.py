try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = number1 / number2

except ValueError:
    print("Please enter a valid number!")

except ZeroDivisionError:
    print("You can't divide by zero!")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("Result =", result)

finally:
    print("პროგრამა დასრულდა")