# დავალება 1


weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi < 19:
    print("You are underweight")

elif bmi <= 25:
    print("You are normalweight")

else:
    print("You are overweight")



# დაველება 2


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print("Invalid operator")

print("Result =", result)


# დავალება 3


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Please enter different numbers")

else:

    if num1 > num2 and num1 > num3:
        print("Largest number is", num1)

    elif num2 > num1 and num2 > num3:
        print("Largest number is", num2)

    else:
        print("Largest number is", num3)