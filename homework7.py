# დავალება 1

numbers = [5, 10, 15, 20, 25]

sum_numbers = 0

for number in numbers:
    sum_numbers += number

average = sum_numbers / len(numbers)

print("Sum =", sum_numbers)
print("Average =", average)



# დავალება 2



items = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]

unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)


# დავალება 3


from random import randint

numbers = []

for i in range(20):
    numbers.append(randint(-50, 50))

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(numbers)
print(even_numbers)



# დავალება 4



persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Alex', 'White', 42),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:

    first_name = input("Enter name: ")

    if first_name == "stop":
        break

    found_name = False

    for person in persons:
        if person[0] == first_name:
            found_name = True
            break

    if not found_name:
        print("Name not found")
        continue

    last_name = input("Enter surname: ")

    found_person = False

    for person in persons:
        if person[0] == first_name and person[1] == last_name:
            print("Age =", person[2])
            found_person = True
            break

    if not found_person:
        print("Surname not found")
