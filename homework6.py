try:
    age = int(input("შეიყვანეთ ასაკი: "))

    if age < 0:
        raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")

except ValueError as e:
    if str(e) == "ასაკი არ შეიძლება იყოს უარყოფითი":
        print(f"Error: {e}")
    else:
        print("შეიყვანეთ მხოლოდ რიცხვი!")

else:
    if age < 18:
        print("არასრულწლოვანი")
    else:
        print("სრულწლოვანი")
