# დავალება 1

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)


# დავალება 2


for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")


 # დავალება 3


price = 50

while price > 0:

    print("Amount due:", price)

    money = int(input("Insert bill: "))

    if money == 5 or money == 10 or money == 20:
        price -= money

    else:
        print("Insert a valid bill")

print("Change owed:", abs(price))