# Реализовать программу, которая находит самое длинное слово в предложении, введенном пользователем.

user_data = input().split()
longest_word = ""
for el in user_data:
    if len(el) > len(longest_word):
        longest_word = el
print(longest_word)
