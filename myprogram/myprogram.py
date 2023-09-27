import sys

numbers = []
words = []

while True:
    user_input = input("Enter a number or word (0 to end for numbers, END to end for words): ")

    if user_input == '0':
        break
    elif user_input == 'END':
        break
    elif user_input.isdigit():
        numbers.append(int(user_input))
    else:
        words.append(user_input)

print("Numbers in ascending order:", sorted(numbers))
print("Numbers in descending order:", sorted(numbers, reverse=True))
print("Words in ascending order:", sorted(words))
print("Words in descending order:", sorted(words, reverse=True))
