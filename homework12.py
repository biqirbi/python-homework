# დავალება 1

def transaction_fee(func):

    def wrapper(balance, amount):

        total = amount + 1

        if balance < total:
            return "Error: Not enough balance!"

        return func(balance, total)

    return wrapper


@transaction_fee
def transaction(balance: int, amount: int) -> int:
    return balance - amount


print(transaction(100, 30))
print(transaction(20, 30))



# დავალება 2


def count_calls(func):

    count = 0

    def wrapper():

        nonlocal count

        count += 1

        print(f"Function was called {count} times")

        return func()

    return wrapper


@count_calls
def hello():
    print("Hello")


hello()
hello()
hello()
hello()