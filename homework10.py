# დავალება 1


def sum_numbers(count=5):

    total = 0

    for i in range(count):
        number = int(input("Enter a number: "))
        total += number

    return total


print(sum_numbers())


# დაველება 2



def split_numbers(*args):

    odd = []
    even = []

    for number in args:

        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return odd, even


odd_numbers, even_numbers = split_numbers(
    1,2,3,4,5,6,7,8,9,10
)

print("Odd:", odd_numbers)
print("Even:", even_numbers)


# დავალება 3



def count_words(sentence):

    sentence = sentence.lower()

    sentence = sentence.replace(".", "")

    words = sentence.split()

    result = {}

    for word in words:

        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


text = input("Enter sentence: ")

print(count_words(text))



# დავალება 4



cheap_products = list(
    filter(
        lambda product: product["price"] < 100,
        products
    )
)

print(cheap_products)




# დავალება 5



def sum_recursive(number):

    if number == 1:
        return 1

    return number + sum_recursive(number - 1)


print(sum_recursive(5))