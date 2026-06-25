# დავალება 1


from faker import Faker
import random

fake = Faker()


def generate_student(student_id: int) -> dict:
    return {
        "ID": student_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": random.randint(18, 80)
    }



# დავალება 2


from faker import Faker
import random

fake = Faker()


def generate_student(student_id: int) -> dict:
    return {
        "ID": student_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": random.randint(18, 80)
    }


def generate_students(count: int) -> list:
    students = []

    for i in range(1, count + 1):
        students.append(generate_student(i))

    return students


print(generate_students(5))