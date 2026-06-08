# დავალება  1

# sentence = input("შეიყვანეთ წინადადება: ")
# word1 = input("რომელი სიტყვა უნდა ჩანაცვლდეს? ")
# word2 = input("რით უნდა ჩანაცვლდეს? ")

# new_sentence = sentence.replace(word1, word2)

# print("შედეგი:")
# print(new_sentence)

# დავალება 2

sentence = input("შეიყვანეთ წინადადება: ")

words = sentence.split()

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("ყველაზე გრძელი სიტყვაა:", longest_word)


# დავალება 3


word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("სიტყვები ანაგრამებია")
else:
    print("სიტყვები არ არის ანაგრამა")