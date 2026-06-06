# დავალება 1
a = int(input("შეიყვანეთ პირველი კათეტი: "))
b = int(input("შეიყვანეთ მეორე კათეტი: "))

hipotenusa = (a ** 2 + b ** 2) ** 0.5
fartobi = a * b / 2

print("ჰიპოთენუზის სიგრძეა:", hipotenusa)
print("ფართობია:", fartobi)


# დავალება 2
seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_left = seconds % 60

print(hours, "საათი,", minutes, "წუთი,", seconds_left, "წამი")