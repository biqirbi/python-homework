# დავალება 1


def text_info(text):

    count = 0

    for char in text:

        if char.isupper():
            count += 1

    return count, text.upper()


user_text = input("Enter text: ")

uppercase_count, uppercase_text = text_info(user_text)

print("Number of uppercase letters:", uppercase_count)
print(uppercase_text)



# დავალება 2



def camel_to_snake(text):

    result = ""

    for char in text:

        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


variable = input("Enter variable name: ")

print(camel_to_snake(variable))
